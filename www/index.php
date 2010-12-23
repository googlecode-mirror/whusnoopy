<?php include("header.php") ?>
<title>yewen's Homepage</title>
<meta name="Description" content="Services of yewen" />
<?php include("bar.php") ?>

<?php include("right.php") ?>
 
  <div id="left">
 <div style="width:100%">

<div class="pt">[INFO] 本站说明</div>
<div class="pb">
本站为 FCR (Rank) 组内临时服务器, ftp 可以通过 <a href="<?php echo $ftpdir?>" target="_blank">http://yewen.us/ftp/</a> 访问
</div>

<a name="update_vim"></a>
<div class="pt"><span class="pno">WORK</span> 测试机更新 vim 版本<span class="time">2010-11-23 13:10</span></div>
<div class="pb">
<pre>
去 vim 的官网下载 <a href="ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2">vim7.3 源码</a>, 解压后在目录里执行
<div class="code">./configure --prefix=/home/work/local/vim
make
make install</div>
完了后, 会有 ~/local/vim/bin/ 这个目录, 然后在 .bashrc 里加这么两行
<div class="code">alias vim="/home/work/local/vim/bin/vim"
alias vimdiff="/home/work/local/vim/bin/vimdiff"</div>
或者最简单的方法, fcr 的同学, 直接从 ai-fcr-test06 把 ~/local/ 整个目录 scp -r 到自己机器上同目录即可
该目录包含 vim 和 python 的更新
bash 脚本也可以拷贝同一台机器上的 .bashrc, 同时强力推荐该机器上的 .toprc .vimrc .screenrc 等配置
<div class="code">scp -r work@ai-fcr-test06.ai01:~/local/ ~/
scp work@ai-fcr-test06.ai01:~/.bashrc ~/
scp work@ai-fcr-test06.ai01:~/.toprc ~/
scp work@ai-fcr-test06.ai01:~/.screenrc ~/
scp work@ai-fcr-test06.ai01:~/.vimrc ~/</div>
<pre>
</div>

<div class="pt">[BUZZ] 界面风格扩展为适应 1280px 宽度<span class="time">2010-11-19 20:07</span></div>
<div class="pb">
考虑到现在公司内最低的分辨率大多都是 X201i 的 1280*800, 所以扩展本站适应宽度为 1280px.<br />
<br />
CSS 浏览器兼容现状:
<ul>
 <li>测试支持: Chrome, IE8+
 <li>没有完整测试: Firefox
 <li>明确不支持: IE6
</ul>
</div>

<div class="pt">[WORK] 已更新 SecureCRT 使用教程<span class="time">2010-11-10</span></div>
<div class="pb">
请猛击<a href="<?php echo $rootdir?>/howto/securecrt.php">这里</a>访问.
</div>

<div class="pt">[WORK] MinGW with GCC 4.5.0, G++ 4.5.0, gdb 7.2</div>
<div class="pb">
下载地址: <a href="<?php echo $ftpdir?>/Software/MinGW_gcc4.5.0_g++4.5.0_gdb7.2.7z" target="_blank">http://yewen.us/ftp/Software/MinGW_gcc4.5.0_g++4.5.0_gdb7.2.7z</a><br />
下载完成后将其解压在 C:\MinGW, 然后在环境变量里加入 C:\MinGW\bin 即可
</div>

 </div> 
  </div>

<?php include("footer.php") ?>

