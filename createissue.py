#!/usr/bin/env python3

import json
import sys
import os
import re
import requests

from urllib.parse import quote
from time import sleep

GITHUB_REPO = "LEXUGE/LEXUGE-comment"
GH_TOKEN = ""

s = requests.Session()

def startup():
    global GH_TOKEN
    try:
        GH_TOKEN=sys.argv[1]
    except:
        sys.exit()

def delete_string_in_file(path,string):
    line=None
    lines=[]
    t=0
    with open(path) as fd:
        for line in fd:
            if (line.startswith(string))and(t==0):
                t=1
                continue
            else:
                lines+=line
    fd.close()
    fd=open(path,"w+")
    for line in lines:
        fd.write(line)
    fd.close()
    print("Delete string successful!")

def fix_issueid_in_file(path,correct_id):
    id="issueid: "+str(correct_id)+"\n"
    delete_string_in_file(path,"issueid: ")
    fd=open(path,'r+')
    content = fd.read()
    pos=[m.start() for m in re.finditer(re.escape("---"),content)][1]
    content = content[:pos]+id+content[pos:]
    fd.close()
    fd=open(path,'w+')
    fd.write(content)
    fd.close()
    print("fix id successful")

def github_list_issues():
    title2ids = {}
    page_num=0
    per_page=30
    token = GH_TOKEN
    headers = {'Authorization': "token " + token}
    while 1:
        page_num+=1
        url = 'https://api.github.com/repos/%s/issues?page=%d&per_page=%d' % (GITHUB_REPO,page_num,per_page)
        resp = s.get(url, headers=headers)
        content = json.loads(resp.content.decode('utf-8'))
        for issue in content:
            title2ids[issue["title"]] = int(issue["number"])
        if len(content)<per_page:
            break
    return title2ids

def github_create_issue(subject, message):
  token = GH_TOKEN
  data = {'title': subject, 'body': message}
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues' % GITHUB_REPO
  resp = s.post(url, headers=headers, data=json.dumps(data))
  content = json.loads(resp.content.decode('utf-8'))
  return content["number"]

def github_close_issue(subject):
  token = GH_TOKEN
  data = {'state': "closed"}
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues/%s' % (GITHUB_REPO,subject)
  resp = s.patch(url, headers=headers, data=json.dumps(data))
  content = json.loads(resp.content.decode('utf-8'))
  return content["number"]

def extract_title(path):
  title, issueid = None, None
  with open(path) as fd:
    for line in fd:
      if line.startswith("title: "):
        title = line[len("title: "):-1].strip(' "')
      if line.startswith("issueid: "):
        issueid = int(line.replace("issueid: ","").strip('"'))
    return path, issueid ,title

def find_title():
  for root, dirs, files in os.walk("_posts"):
    for filename in files:
      if filename.endswith(".markdown"):
        filepath = os.path.join(root, filename)
        yield extract_title(filepath)

def main():
  counter = 0
  counter2 = 0
  startup()
  title2ids = github_list_issues()
  print("These are all the title and the id on repo %s,check it and continue." % GITHUB_REPO)
  print(title2ids)
  input()
  for path, issueid ,title in find_title():
    sleep(2)
    counter2+=1
    print("No."+str(counter2)+" Processing File path:"+path)
    counter+=1
    if title == None:
      print("ERROR: file %s don't have title" % path)
      continue
    if title in title2ids:
      if issueid == None:
        print("WARN: file %s should have issueid %s" % (path, title2ids[title]))
        fix_issueid_in_file(path, title2ids[title])
        print(" ")
        continue
      if issueid != title2ids[title]:
        print("ERROR: file %s with title %s have id %s mismatch github id %s .Try to fix it." % (path, title,issueid, title2ids[title]))
        fix_issueid_in_file(path,title2ids[title])
        print(" ")
        continue
    if not (title in title2ids):
        if issueid !=None:
            print("WARN: file %s 's issueid is only available in local,Try to upload the issueid." % (path))
            message = "This issue is reserved for %s.Try to search it in https://lexuge.github.io !" % (title)
            delete_string_in_file(path,"issueid: ")
            newissueid = github_create_issue(title, message)
            fix_issueid_in_file(path,newissueid)
            print(" ")
            continue
    if issueid == None:
      message = "This issue is reserved for %s.Try to search it in https://lexuge.github.io !" % (title)
      newissueid = github_create_issue(title, message)
      fix_issueid_in_file(path,newissueid)
      print("%s :issueid: %s" % (path, newissueid))
      title2ids[title] = newissueid
      continue
    print("Nothing to process.")
    counter-=1
    print(" ")

  for titles in title2ids:
      temp=0
      closeissueid=0
      for path, issueid ,title in find_title():
          if title==titles:
            temp=1
      if temp==0:
          counter+=1
          closeissueid=github_close_issue(title2ids[titles])
          print("%s closed with issueid %s" %(titles,closeissueid))
  print("Processed "+str(counter)+" file(s)")

if __name__ == '__main__':
  main()
