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
  <a href="http://www.polyu.edu.hk" target="_blank"><img src="../polyu.jpg" alt="The Hong Kong Polytechnic University"></a><br />
</div>
<div id="bar">
  <a href="/">HOME</a>
  <a href="http://whusnoopy.vicp.net:25001/adke/adke.php">Advertising Keywords Extraction Demo</a>
</div>

<div id="main" align="left">

<center>
<div class="pb">
Input an url you want to see, or view the sample <a href="http://whusnoopy.vicp.net:25001/adke/adke.php?url=http://whusnoopy.vicp.net:25001/adke/thread-3376942-1-1.html">dospy</a><br /> 
<form method="post" name="demogo" action="">
 <div class="sq" style="width:640px">
  <input type="submit" value="Go!" class="button"/>
  <input value="" title="URL" size="88" name="url" maxlength="256" class="sqi" />
 </div>
</form>
</div>
</center>

<hr size="0" />
<?php
  if (!empty($_POST)) {
    $url = $_POST["url"];
    $command = "python /home/cswenye/snoopy/adke/py/test.py ".$url;
    system($command);
    echo '<iframe width="100%" height="640" src="demo.php?p=1" frameborder="0"></iframe>';
  }
?>
</div>

<div id="ft">
  <hr width=979 size=0 />
  Copyright &copy; 2009 Wen YE, Department of Computing, The Hong Kong Polytechnic University. All rights reserved.<br />
  Please <a href="mailto:cswenye@comp.polyu.edu.hk" >contact me</a> if you have any suggestion.<br /><br />
</div>

</center>
</body>
</html>

