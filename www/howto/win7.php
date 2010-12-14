<?php include("../header.php") ?>
<title>Win7/Office2010 安装使用教程</title>
<meta name="Description" content="如何安装激活 Windows 7 和 Office 2010" />
<?php include("../bar.php") ?>
<?php include("../right.php") ?>

  <div id="left">
 <div style="width:100%">

<div class="pt"><span class="pno">I</span> Win 7 安装使用简要说明<span class="time">2010-11-19 19:18</span></div>
<div class="pb">
<pre>
本说明基于 Win7 Pro x86 chs, 需要的文件可以在 <a href="http://yewen.us/ftp/Win7_rtm_with_loader/">ftp 的 Win7 目录</a>下找到.
安装百度内部准入需要的<a href="http://yewen.us/ftp/Software/Norton_32_jiaohu.exe">杀毒软件</a>和<a href="http://yewen.us/ftp/Software/Baidu_BNAC_Setup.exe">准入系统</a> (非百度内无需使用)
安装 X201i 的<a href="http://yewen.us/ftp/Software/X201i_Drivers/Ethernet%5b6irf24ww_732%5d.exe">网卡驱动</a>后, 用 <a href="http://yewen.us/ftp/Software/X201i_Drivers/systemupdate40-2009-10-19.exe">System Update</a> 自动下载所有驱动
<a href="http://yewen.us/ftp/Software/">Software</a> 下提供了其他一些常用软件, <a href="http://yewen.us/ftp/Office2010_rtm_zh-cn_with_kms/">ftp 的 office 目录</a> 下提供了 Office 2010 Pro 和其激活工具
</pre>
</div>

<a name="win7"></a>
<div class="pt"><span class="pno">II</span> Windows 7 安装, 激活及使用技巧</div>
<div class="pb">
<pre>
本文以 ThinkPad X201i 安装为基准, 其他机器可以参考, 驱动部分自行替代即可.

================
PART I. 安装
================
a. U 盘安装
  先下载微软官方的 U 盘制作工具 (<a href="http://yewen.us/ftp/Win7_rtm_with_loader/Windows7-USB-DVD-tool.exe">Windows7-USB-DVD-tool.exe</a>) 并安装
  安装完成后使用这个工具把 iso 格式的 Win7 安装文件 (如 <a href="http://yewen.us/ftp/Win7_rtm_with_loader/cn_windows_7_professional_x86_dvd_x15-65790.iso">Win7 Pro Cn x86</a>, 公司的 X201i 带这个正版序列号) 刻录至 4G 或以上大小的 U 盘
  开机前插入 U 盘, 开机按 F12 选 U 盘启动 (不同的机器按的键可能不一样, ThinkPad 都是 F12), 然后就跟传统安装没任何区别了

b. 硬盘安装
  见 <a href="http://yewen.us/ftp/Win7_rtm_with_loader/%e7%a1%ac%e7%9b%98%e6%a0%bc%e5%bc%8f%e5%8c%96%e5%ae%89%e8%a3%85Win7%e5%9b%be%e7%89%87%e6%95%99%e7%a8%8b.jpg">硬盘格式化安装Win7图片教程.jpg</a>

c. 注意事项
  1. 推荐格式化系统盘安装, 即选 [全新安装], 并格式化 C 盘
  2. 安装时的用户名请不要和域用户名一致, 原因加域部分解释
  3. 安装时输序列号的过程直接跳过

================
PART II. 加域
================
a. 加域前的准备
  加域前不推荐做任何软件安装或驱动更新, 因为域帐户是个完全独立的帐户, 很多软件对多帐户支持不好
  因为加域需要连着公司的有线, 所以先保证能上网, 已经识别出网卡驱动的请跳过
  X201i 的网卡驱动 Win7 不带, 请先安装官方驱动 (x86 的请下载 <a href="http://yewen.us/ftp/Software/X201i_Drivers/Ethernet%5b6irf24ww_732%5d.exe">Ethernet[6irf24ww_732].exe</a>)

b. 加域
  在桌面或开始菜单的 [计算机] 上点右键, 选 [属性], 在 [计算机名称, 域和工作组设置] 部分选 [更改设置], 点 [网络 ID] 进入加域向导
  中间一直按要求输入公司的用户名/密码和域名 (internal.baidu.com, 可能会强制大写) 即可
  切记最后一步要把用户选为 [管理员]
  按提示重启后完成加域, 用域帐号 (internal.baidu.com\yourname) 登陆即可
  如果安装时的用户名和域用户名一样, 域用户的目录会带个 INTERNAL, 很不好看, 所以建议两者分开

c. 准入
  下载杀毒软件 (<a href="http://yewen.us/ftp/Software/Norton_32_jiaohu.exe">Norton</a>) 和准入 (<a href="http://yewen.us/ftp/Software/Baidu_BNAC_Setup.exe">BNAC</a>), 在安装文件上点右键, 选 [以管理员身份运行] 安装
  安装完成后重启, 准入时认证方式选 [DOMAIN], 并在设置里勾上三个勾, 以后开机自动准入

================
PART III. 激活
================
  如果是带 Win7 授权的 X201i, 直接输入机器底部 COA 标签上的序列号即可
  否则请下载 <a href="http://yewen.us/ftp/Win7_rtm_with_loader/Windows%207%20Loader.zip">Win7 Loader</a> 自行研究, 盗版的东西不推荐...

================
PART IV. 驱动
================
  让 Win7 自动更新就可以找到绝大部分驱动
  ThinkPad 各机型可以安装 <a href="http://yewen.us/ftp/Software/X201i_Drivers/systemupdate40-2009-10-19.exe">System Update</a> 来自动下载所需驱动和软件, 还是右键用管理员模式运行

================
PART V. 系统优化
================
a. 关闭 UAC
  前面说安装软件需要右键运行都是因为这个用户帐户权限控制 (类似 Ubuntu 的 sudo), 觉得不爽的可以改
  在开始菜单输 "UAC", 直接回车打开, 推荐调低一级即可, 这样软件安装还是右键管理员权限运行, 其他的普通使用可以正常用, 系统也安全
  如果对自己的操作习惯有自行, 直接拉到最低关闭也行
b. 系统还原 (还要关么?)
  在桌面或开始菜单的 [计算机] 上点右键, 选 [属性] 里的 [系统保护], 在里面修改
  个人不推荐关闭
c. 关闭休眠
  关闭休眠到硬盘 (Hibernate), 为硬盘节省等同内存大小的空间, 睡眠模式 (Sleep) 建议保留
  开始菜单输 "cmd", 在上面点右键 [以管理员模式运行], 输 "powercfg /h off", 回车即可
d. 关闭移动设备自动播放
  在控制面板里搜 "auto play", 进 "自动播放", 去掉 "为所有媒体和设备使用自动播放" 的勾
e. 取消字体限制
  如果不取消这个限制, 在很多程序里会发现可选字体莫名其妙的就少了非常多
  在控制面板里搜 "Font", 进 "更改字体设置", 去掉 "根据语言设置隐藏字体" 的勾
f. 修改电源选项
  在控制面板里搜 "Power", 进 "电源选项"
  在 "选择关闭盖子的功能" 里, 均选择 "不采取任何操作"
  在 "更改计算机睡眠时间" 里, 接通电源时选 "从不"
g. 关闭鼠标休眠唤醒
  在控制面板里搜 "mouse", 进 "更改鼠标设置"
  在 "硬件" 页里选中鼠标点 "属性", 在 "常规" 页里点 "改变设置", 在 "电源管理" 页把 "允许此设备唤醒计算机" 的勾去掉
h. 显示文件扩展名
  在任意一个文件夹里, 按 alt 键, 在出来的工具栏里点 "工具", 进 "文件夹选项", 在 "查看" 页里去掉 "隐藏已知文件类型的扩展名" 的勾
i. 安装打印机
  在任意一个文件夹的地址栏输 "\\172.22.2.19", 双击 "Input BW Printer-默认使用" 即可自动安装打印机驱动
  如果是 64 位系统, 需要单独下载驱动: <a href="http://yewen.us/ftp/Software/Canon_Printer_UFR_II_Driver_270_Win_x64_ZH/">Canon Printer UFR II Driver win7 x64</a>

================
PART VI. 软件
================
x. 如无特意说明, 安装时均在安装文件上点右键选 [以管理员模式运行], 这样不容易出问题, 特别是文件关联什么的.
a. 7zip. 装好后选文件关联时, 也用管理员模式运行, 这样右键菜单啥的都对了.
b. Daemon Tools. 需要先装 <a href="http://yewen.us/ftp/Software/SPTDinst-v172-x86.exe">SPTD 1.72</a>, 保证和 X201i 的硬件兼容 (x64 请下载 <a href="http://yewen.us/ftp/Software/SPTDinst-v172-x64.exe">SPTD 1.72 x64</a>)
c. Office 2010. 见 <a href="#office">Office 2010 安装教程</a>

========================
APPENDIX I. 小提示
========================
a. 鼠标拖拽窗口标题栏到桌面上沿快速最大化, 拖到桌面左右两侧快速半屏最大化, 拖回中间还原
b. Win+P 进行多显示器切换 (接外接显示器或投影仪时很方便, 会自动调整分辨率)
c. Win+X 进入移动设置, 可以调整一堆和笔记本有关的设置
d. 在任务栏上按住图标向上推可以和右键一样调出 JumpList, 向上推这个动作可以更好衔接调出 JumpList 后的操作
e. 修改记事本字体设置, 改为 fixedsys 这个默认字体
f. 装 System Update 更新驱动
g. 鼠标设置, 打字时隐藏指针, 去掉勾

</pre>
</div>

<a name="office"></a>
<div class="pt"><span class="pno">III</span> Office 2010 安装教程</div>
<div class="pb">
<pre>
================
PART I. 安装
================
使用虚拟光驱加载 <a href="http://yewen.us/ftp/Office2010_rtm_zh-cn_with_kms/%5bOffice2010%e7%ae%80%e4%bd%93%e4%b8%ad%e6%96%87%e5%a4%a7%e5%ae%a2%e6%88%b7%e7%89%88_32%e4%bd%8dx86%5d.SW_DVD5_Office_Professional_Plus_2010_W32_ChnSimp_MLF_X16-52528.iso">Office_2010_Pro_x86_chs.iso</a>, 或用解压软件直接解压, 运行里面的 setup.exe 即可
  (如果是 Win7 推荐点右键, 选 [使用管理员模式运行])

在出来的第一个界面里选 [自定义], 勾选自己需要的组件并设定好个人信息后, 点 [现在安装]
  (推荐 Word/Excel/PowerPoint/OneNote/Visio Viewer 和通用组件, 如在公司内用, 再加 Outlook)

================
PART II. 激活
================
关闭杀毒软件, 使用 <a href="http://yewen.us/ftp/Office2010_rtm_zh-cn_with_kms/mini-KMS_Activator_v1.2_Office2010_VL_ENG.rar">mini-KMS_Activator_v1.2_Office2010_VL_ENG.rar</a> 里的 [mini-KMS] 完成激活

1. 右键点 mini-KMS_Activator_v1.2_Office2010_VL_ENG.exe, 以管理员身份运行
    出现提示窗口: did you run the program as administrator? 选 [是]

2. 在 mini-kms 窗口, 点 [install/uninstall kmservice] 按钮, 出现窗口提示:
        kmservice will be installed on your computer.continue? (y/n):
    输入 y, 等出现提示: press any key to exit..., 回车

3. 在 mini-kms 窗口, 按 [activation office 2010 VL] 按钮
    等出现 press any key to exit... 回车

4. 确认激活成功
    随便打开一个 Office 组件, 如 Word, 点左上角 [文件] - [帮助], 看窗口右侧提示
    如果显示 [激活的产品], 则激活成功
    如果不是, 在 mini-kms 窗口, 点击 [restart service] 重新启动服务
      出现窗口: kmservice it is successfully restarted. 后按确定按钮
    重复步骤 2/3, 再重新确认是否激活

6. 激活成功后, 在 mini-kms 窗口, 点击 [install/uninstall kmservice] 按钮, 出现窗口提示
        kmservice will be removed from your computer.continue?(y/n):
    输入 y, 等出现提示 press any key to exit..., 回车

7. 关闭 mini-kms
</pre>
</div>

 </div> 
  </div>

<?php include("../footer.php") ?>

