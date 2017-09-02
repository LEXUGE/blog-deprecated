var reaction_fa = {
  "+1": "thumbs-o-up",
  "-1": "thumbs-o-down",
  "laugh": "smile-o",
  "hooray": "gift",
  "confused": "frown-o",
  "heart": "heart-o"
};

function email_toggle(i) {
  // Email toggle
  $("#article"+i+" > .email-hidden-toggle > a").on("click", function (e){
    e.preventDefault();
    $("#article"+i+" > .email-hidden-reply", this.parent).toggle();
  });
}

function loadComments(data,textStatus, jqXHR,comment_id,page_id,page_num) {
  for (var i=0; i<data.length; i++) {
    var cuser = data[i].user.login;
    var cuserlink = data[i].user.html_url;
    var clink = data[i].html_url;
    var cbody = data[i].body_html;
    var cavatarlink = data[i].user.avatar_url;
    var cdate = new Date(data[i].created_at);
    var dopts = { month: 'short', day: 'numeric', year: 'numeric' }
    var reactions = data[i].reactions;
    var creactions = "";
    if(reactions){
      for(reactionkey in reaction_fa){
        if(reactions[reactionkey] > 0) {
            creactions += '<i class="fa fa-'+ reaction_fa[reactionkey]+'"></i>' + reactions[reactionkey] + "&nbsp;";
        }
      }
    }
    $("#comments").append(
     '<div class="post-header bg-{{site.default_post_color}}"><hr><h4><a class="post-link" href="'
     + cuserlink + '" style="display:inline">' + cuser + '</a>'+'<small style="display:inline">'
     + '&nbsp; left a comment on '+cdate.toLocaleDateString("en", dopts) +'</small>'
     + '&nbsp;' + creactions + '</h4>'
     + '</div><article id="article'+i+'" class="markdown-body"  style="white-space: pre-wrap;">' + cbody + '</article>');
     email_toggle(i);
  }
  // Comments Pagination
  console.log("data.length: "+data.length);
  console.log("per page num: "+page_num);
  if (data.length === page_num)
  {
      $("#gh-load-comments").attr("onclick", "DoGithubComments("+ comment_id+","+(page_id + 1) + ");");
      $("#gh-load-comments").show();
  }
  else
  {
      $("#gh-load-comments").hide();
  }
}

function DoGithubComments(comment_id,page_id)
{
  if (page_id === undefined)
        page_id = 1;
  page_num = 30;
  $.ajax("https://api.github.com/repos/LEXUGE/LEXUGE-comment/issues/"+comment_id+"/comments?page="+page_id+"&per_page="+page_num, {
    headers: {Accept: "application/vnd.github.squirrel-girl-preview.full+json"},
    dataType: "json",
    success: function(msg,textStatus,jqXHR){
      loadComments(msg,textStatus, jqXHR,comment_id,page_id,page_num);
   },
  });
}
