from urllib import urlencode

html_template = """
<link href="/moin_static182/pyar/tweet/jquery.tweet.css" media="all" rel="stylesheet" type="text/css"/>
<div class="widget_list">
<script language="javascript" src="/moin_static182/pyar/jquery.js" type="text/javascript"></script>
<script language="javascript" src="/moin_static182/pyar/tweet/jquery.tweet.js" type="text/javascript"></script> 
<script type='text/javascript'>
    $(document).ready(function(){
        $(".tweet").tweet({
            username: "%s",
            avatar_size: 32,
            count: 10,
            loading_text: "Cargando tweets..."
        });
    });
</script> 
<div class="tweet"></div>  
</div>
"""

def macro_Twitter(macro, _kwargs={}):
#    params = urlencode(_kwargs)

  #  _kwargs.update(dict(
  #      source="embed",
  #  ))
  #  params2 = urlencode(_kwargs)
    user = _kwargs['usuario']
    html = html_template % (user)
    return macro.formatter.rawHTML(html)
