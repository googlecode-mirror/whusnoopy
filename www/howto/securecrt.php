<?php include("../header.php") ?>
<title>SecureCRT 安装配置教程</title>
<meta name="Description" content="如何安装配置 SecureCRT" />
<?php include("../bar.php") ?>
<?php include("../right.php") ?>

  <div id="left">
 <div style="width:100%">

<a name="auth"></a>
<div class="pt">测试机信任关系建立</div>
<div class="pb">
<pre>先在需要加入信任关系列表的机器上运行如下命令
<div class="code">ssh-keygen -b 1024 -t rsa</div>
可以生成自己的公钥在
<div class="code">~/.ssh/id_rsa.pub</div>
内, 将此文件的内容附加到每一台需要和此机器建立信任关系的如下文件末尾即可
<div class="code">~/.ssh/authorized_keys</div>
推荐的方法是先在每台机器上生成自己的公钥, 然后将这些公约合并成一个文件, 再将这个合并的文件拷贝至每台机器的 ~/.ssh/authorized_keys 即可</pre>
</div>

<a name="vimrc"></a>
<div class="pt">Vim 配置脚本 .vimrc</div>
<div class="pb">
<pre>根据自己喜好可以进行额外修改, 放在 ~/.vimrc 即可 :)
vimrc 的语法规则是用双引号作为行注释开始, 类似 C/C++ 里的 // 注释
<div class="code">"set nocompatible " 非 vi 兼容模式
syntax on " 色彩高亮
set number " 显示行数
set ruler " 显示当前位置于右下角
set backspace=2 " 设置 backspace 模式为标准
set showmatch " 显示配对括号
set incsearch " 增量查找
set hlsearch
set ai " 自动缩进
set si " 智能缩进
set cindent " C 风格缩进
set tabstop=4 " Tab 宽度
set softtabstop=4 " Tab 宽度
set shiftwidth=4 " Tab 宽度
set expandtab " 输入的 tab(\t) 均不保持为 tab 而转换为空格
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,sjis,euc-kr,ucs-2le,latin1 "字符编码
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%04l,%04v][%p%%]\ [LEN=%L] " 状态栏格式
set laststatus=2 " 一直显示状态栏

" 插入模式切换
map &lt;F9&gt; :set paste!&lt;BAr&gt;set paste?&lt;CR&gt;

" 多 Tab 时翻页
map &lt;silent&gt; &lt;F11&gt; :tabprevious&lt;CR&gt;
imap &lt;silent&gt; &lt;F11&gt; &lt;Esc&gt;:tabprevious&lt;CR&gt;gi

map &lt;silent&gt; &lt;F12&gt; :tabnext&lt;CR&gt;
imap &lt;silent&gt; &lt;F12&gt; &lt;Esc&gt;:tabnext&lt;CR&gt;gi
</div></pre>
</div>

<div class="pt">SecureCRT 图文教学</div>
<div class="pb">
  以下为全文图片, 里面涉及的链接为
  <ul>
  <li> <a href="http://yewen.us/ftp/Software/SecureCFX_6.5.3.7z">SecureCRT 6.5.3 绿色版</a>
  <li> <a href="http://yewen.us/ftp/Software/7z918_9.20.0.0.exe">7zip x86 9.20</a>
  <li> <a href="http://yewen.us/ftp/TempSpace/monaco_win.ttf">Monaco 字体</a>
  <ul>
</div>

<div class="pt">SecureCRT 图文教学</div>
<div class="pb">
  <img src="img/scrt01.png"><br />
  <img src="img/scrt02.png"><br />
  <img src="img/scrt03.png"><br />
  <img src="img/scrt04.png"><br />
  <img src="img/scrt05.png"><br />
</div>

 </div> 
  </div>

<?php include("../footer.php") ?>

