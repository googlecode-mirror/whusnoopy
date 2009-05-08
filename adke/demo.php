<?php
header("Content-Type: text/html; charset=utf-8");

if (isset($_GET['doc']))
  $doc_prefix = $_GET['doc'];
else
  $doc_prefix = 'dospy';

if (isset($_GET['p']))
  $cp = $_GET['p'];
else
  $cp = 15;

$doc_file = $doc_prefix.".xml";
$ads_file = $doc_prefix.".ads$cp";

$doc = new DOMDocument();
$doc->load( $doc_file );

$ads = new DOMDocument();
$ads->load( $ads_file );
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
  $banner_ads = $ads->getElementsByTagName( "banner" );
  if ( $banner_ads->length > 0 ) {
    echo "<div class=\"gat\">Banner Ads</div>\n";
    echo "<div class=\"gab\">\n";
    $keywords = $banner_ads->item(0)->getElementsByTagname( "keyword" );
    foreach ( $keywords as $banner_ad ) {
      $keyword = $banner_ad->nodeValue;
      echo "$keyword ";
    }
    echo "</div>\n";
  }
?>
</div>
<div id="bar">
  <a href="http://whusnoopy.vicp.net:25001/adke/">Advertising Keywords Extraction Demo</a>
</div>

<div id="main" align="left">

<div id="right">
<?php
  $sidebar_ads = $ads->getElementsByTagName( "sidebar" );
  if ( $sidebar_ads->length > 0 ) { 
    echo "<div class=\"gat\">Sidebar Ads</div>";
    echo "<div class=\"gab\">\n";
    $keywords = $sidebar_ads->item(0)->getElementsByTagName( "keyword" );
    foreach ( $keywords as $sidebar_ad ) {
      $keyword = $sidebar_ad->nodeValue;
      echo "$keyword <br />\n";
    }
    echo "</div>\n";
  }
?>
<div class="gat">Navigate</div>
<div class="gab">
Input the post No. you want to go and click Go!.
<center>
<form method="get" name="demogo" action="demo.php">
<div class="sqs">
  <input type="submit" value="Go!" class="button"/>
  <input value="<?php echo $cp==15?$cp:$cp+1; ?>" name="p" size="4" class="sqi" />
  <input type="hidden" value="<?php echo "$doc_prefix"; ?>" name="doc" />
</div>
</form>
</center>
or click the Post No. on the top-left of each post.
</div>
</div>

<div id="left">

<?php
$posts = $doc->getElementsByTagName( "post" );
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
  echo "<span class=\"pno\"><a href=\"demo.php?doc=$doc_prefix&p=$post_id\">$post_id</a></span>\n";
  echo "$title\n";
  echo "</div>\n";
  
  echo "<div class=\"pb\">\n";

  $refs = $post->getElementsByTagName( "ref" );
  $ref_no = $refs->item(0)->getAttribute( "id" );
  if ( $ref_no != 0 ) {
    $ref = $refs->item(0)->nodeValue;
    if ( strlen($ref) == 0 ) {
      echo "<div class=\"sref\"><span class=\"sreft\">Refer</span> to <a href=\"#post_$ref_no\">$ref_no#</a></div>\n";
    } else {
      echo "<div class=\"rt\">Quote from <a href=\"#post_$ref_no\">$ref_no#</a></div>\n";
      echo "<div class=\"rb\">$ref</div>\n";
    }
  }

  $bodys = $post->getElementsByTagName( "body" );
  $body = $bodys->item(0)->nodeValue;

  $body = str_replace("\n", "<br />\n", $body);
  echo "$body\n";

  $pads = $ads->getElementsByTagName( "p$post_id" );
  if ( $pads->length > 0 ) {
    echo "<div class=\"spa\">";
    echo "<span class=\"spat\">Ads for Post $post_id</span>";
    foreach ( $pads as $pad ) {
      $keyword = $pad->nodeValue;
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
