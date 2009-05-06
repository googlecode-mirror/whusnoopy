<?php
header("Content-Type: text/html; charset=utf-8");

if (isset($_GET['xmlfile']))
  $xml_file = $_GET['xmlfile'];
else
  $xml_file = 'dospy.xml';

$doc = new DOMDocument();
$doc->load( $xml_file );
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
  $banner_ads = $doc->getElementsByTagName( "banner_ads" );
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
<div id="bar">Advertising Keywords Extraction Demo</div>

<div id="main" align="left">

<div id="right">
<?php
  $sidebar_ads = $doc->getElementsByTagName( "sidebar_ads" );
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
</div>

<div id="left">

<?php
$posts = $doc->getElementsByTagName( "post" );
foreach( $posts as $post ) {
  echo "<div class=\"pt\">\n";
  $post_id = $post->getAttribute( 'id' );

  $date_times = $post->getElementsByTagName( "date_time" );
  $date_time = $date_times->item(0)->nodeValue;
  
  $titles = $post->getElementsByTagName( "title" );
  $title = $titles->item(0)->nodeValue;

  echo "<a name=\"post_$post_id\"></a>";
  echo "<div class=\"time\">$date_time<span class=\"pno\">$post_id#</span></div>\n";
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

  $ads = $post->getElementsByTagName( "ads" );
  if ( $ads->length > 0 ) {
    echo "<div class=\"spa\">";
    echo "<span class=\"spat\">Ads for Post $post_id</span>";
    foreach ( $ads as $ad ) {
      $keyword = $ad->nodeValue;
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