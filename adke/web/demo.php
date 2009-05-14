<?php
header("Content-Type: text/html; charset=utf-8");

if (isset($_GET['doc']))
  $doc = $_GET['doc'];
else
  $doc = 'dospy.xml';

$doc_file = '/home/cswenye/adke/data/'.$doc;

if (isset($_GET['p']))
  $cp = $_GET['p'];

$domdoc = new DOMDocument();
$domdoc->load( $doc_file );

$posts = $domdoc->getElementsByTagName( "post" );
$sp = $posts->length;
if ($cp > $sp) {
  $cp = $sp;
}
$ads = $domdoc->getElementsByTagName( "tads" )->item($cp-1);
$banner_ads = $ads->getElementsByTagName( "banner" )->item(0);
$sidebar_ads = $ads->getElementsByTagName( "sidebar" )->item(0);
$pads = $ads->getElementsByTagName('pads');
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Ads Keywords Extraction Demo</title>
<meta name="Description" content="Ads Keywords Extraction Demo" />
<link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<center>

<div id="hd">
<?php
  if ( $banner_ads->hasChildNodes() > 0 ) {
    echo "<div class=\"gat\">Banner Ads</div>\n";
    echo "<div class=\"gab\">\n";
    $keywords = $banner_ads->getElementsByTagname( "kw" );
    foreach ( $keywords as $banner_ad ) {
      $keyword = $banner_ad->nodeValue;
      echo "$keyword ";
    }
    echo "</div>\n";
  }
?>
</div>
<div id="bar">
  <a href="/">HOME</a>
  <a href="http://whusnoopy.vicp.net:25001/adke/">Advertising Keywords Extraction Demo</a>
</div>

<div id="main" align="left">

<div id="right">
<div class="pt">Navigate</div>
<div class="pb">
Input the post No. and click Go!, or click the Post No. on the top-left of each post.<br />
<br />
<a href="<?php echo 'http://bbs.dospy.com/'.substr($doc, 0, $doc->length-3).'html'?>">Origin Post</a><br />
</div>
<center>
<form method="get" name="demogo" action="demo.php">
<div class="sqs">
  <input type="submit" value="Go!" class="button"/>
  <input value="<?php echo $cp==$sp?$cp:$cp+1; ?>" name="p" size="4" class="sqi" />
  <input type="hidden" value="<?php echo "$doc"; ?>" name="doc" />
</div>
</form>
<br />
<br />
<br />
</center>
<?php
  if ( $sidebar_ads->hasChildNodes() > 0 ) {
    echo "<div class=\"gat\">Sidebar Ads</div>";
    echo "<div class=\"gab\">\n";
    $keywords = $sidebar_ads->getElementsByTagName( "kw" );
    foreach ( $keywords as $sidebar_ad ) {
      $keyword = $sidebar_ad->nodeValue;
      echo "$keyword <br />\n";
    }
    echo "</div>\n";
  }
?>
</div>

<div id="left">

<?php
foreach( $posts as $post ) {
  $post_id = $post->getAttribute( 'id' );

  if ($post_id > $cp)
    break;

  $date_times = $post->getElementsByTagName( "date_time" );
  $date_time = $date_times->item(0)->nodeValue;
  
  $titles = $post->getElementsByTagName( "title" );
  $title = $titles->item(0)->nodeValue;

  echo "<a name=\"post_$post_id\"></a>\n";
  echo "<div class=\"pt\">\n";
  echo "<div class=\"time\">$date_time</div>\n";
  echo "<span class=\"pno\"><a href=\"demo.php?doc=$doc&p=$post_id\">$post_id</a></span>\n";
  echo "$title\n";
  echo "</div>\n";
  
  echo "<div class=\"pb\">\n";

  $refs = $post->getElementsByTagName( "ref" );
  foreach ( $refs as $ref ) {
    $ref_no = $ref->getAttribute( "id" );
    if ( $ref_no != 0 ) {
      $ref_body = $ref->nodeValue;
      if ( strlen($ref_body) == 0 ) {
        echo "<div class=\"sref\"><span class=\"sreft\">Refer</span> to <a href=\"#post_$ref_no\">$ref_no#</a></div>\n";
      } else {
        echo "<div class=\"rt\">Quote from <a href=\"#post_$ref_no\">$ref_no#</a></div>\n";
        echo "<div class=\"rb\">$ref_body</div>\n";
      }
    }
  }

  $bodys = $post->getElementsByTagName( "body" );
  $body = $bodys->item(0)->nodeValue;

  $body = str_replace("\n", "<br />\n", $body);
  echo "$body\n";

  $pad = $pads->item( $post_id-1 );
  if ( $pad->hasChildNodes() ) {
    echo "<div class=\"spa\">";
    echo "<span class=\"spat\">Ads for Post $post_id</span>";
    $kws = $pad->getElementsByTagname( "kw" );
    foreach ( $kws as $kw ) {
      $keyword = $kw->nodeValue;
      echo "$keyword ";
    }
    echo "</div>\n";
  }

  echo "</div>\n\n";
}
?> 

</div>
</div>

<div id="ft">
  <hr width=979 size=0 />
  Copyright &copy; 2009 Wen YE, Department of Computing, The Hong Kong Polytechnic University. All rights reserved.<br />
  Please <a href="mailto:cswenye@comp.polyu.edu.hk" >contact me</a> if you have any suggestion.<br /><br />
</div>

</center>
</body>
</html>
