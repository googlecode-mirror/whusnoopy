<?php include("../header.php") ?>
<title>Win7/Office2010 安装使用教程</title>
<meta name="Description" content="如何安装激活 Windows 7 和 Office 2010" />
<?php include("../bar.php") ?>
<?php include("../right.php") ?>

  <div id="left">
 <div style="width:100%">

<div class="pt">本页面说明</div>
<div class="pb">

<div class="ntc">请注意, 本页面尚未完全完工</div>

<pre>
本盘为 Win7 Pro x86 chs 安装盘
Office_2010_Pro_x86_chs 目录下提供了 Office 2010 Pro 和其激活工具
Baidu_Internal 目录下提供了百度内部的杀毒软件和准入系统 (非百度内无需使用)
X201i_Drivers 目录下提供了百度版 X201i 笔记本电脑的基本驱动和驱动下载工具
Software 下提供了其他一些常用软件
</pre>
</div>

<div class="pt"> I. Windows 7 安装, 激活及使用技巧</div>
<div class="pb">
<pre>
1. 安装

a. U 盘安装
本 U 盘已经设定好, 开机前插入 U 盘, 开机按 F12 选 U 盘启动即可
如果需要自己制作其他版本的引导, 在磁盘管理器里将 U 盘格式化 (不能是卷), 设置为主分区和活动分区
将 Win7 iso 的所有文件解压到 U 盘, 在命令提示符运行
    u:\boot\bootsect /nt60 u:
使 U 盘可引导 (其中 u: 是 U 盘的盘符, 根据自己情况改变)

b. 硬盘安装
见 Software/硬盘格式化安装Win7图片教程.jpg

2. 激活
// TODO

3. 驱动

让 Win7 自动更新就可以找到绝大部分驱动
ThinkPad 可以安装 System Update 4.0 来自动下载所需驱动和软件 (见本文 III 章)
    本 U 盘中 X201i_Drivers/systemupdate40-2009-10-19.exe
如果是 X201i, 需要先安装有线网卡驱动  X201i_Drivers/Ethernet[6irf24ww_732].exe, 连上有线后更新即可
如在公司内网使用, 还需要在 ~/Baidu_Internal 里安装杀毒软件和准入, 并加域后完成驱动更新

4. 加域
在桌面或开始菜单的 [计算机] 上点右键, 选 [属性], 在 [TODO] 选设置, 点 [Network ID] 进入加域向导
中间一直按要求输入公司的用户名/密码和域名 (internal.baidu.com, 可能会强制大写) 即可
切记最后一步要把用户选为 [管理员]

4. 系统优化
a. 关闭系统还原节省硬盘空间. 直接 Computer 上右键, System Protection 里关闭
b. 关闭休眠(Hibernate). 管理员模式运行 cmd, C:>powercfg -h off
c. 取消字体语言限制. 在控制面板的 Font settings, 去掉 Hide fonts based on language settings 的勾
    # 这个很脑残感觉, 害的在 记事本/Chrome 等地方要选 Fixedsys 和 Courier New 都选不到
d. 在鼠标的电源管理页将 允许此设备将计算机从待机状态恢复 的勾去掉
    # 这个也很脑残, 一开始不知道, 发现待机后随便动下机器就又醒了
e. 开始菜单输 UAC 直接回车, 推荐调低一档, 或者自己使用电脑习惯比较好的可以拉到最低将其关闭

5. 软件
x. 如无特意说明, 安装时点右键选 run as administrator 模式运行, 这样不容易出问题, 特别是文件关联什么的.
a. 7zip. 装好后选文件关联时, 也用管理员模式运行, 这样右键菜单啥的都对了.
b. Daemon Tools. 需要装 SPTD 1.72, 保证和 X201i 的硬件兼容
c. Office 2010. 见 Adds/Office_2010_安装指南.txt

6. 小提示
a. 鼠标拖拽窗口标题栏到桌面上沿快速最大化, 拖到桌面左右两侧快速半屏最大化, 拖回中间还原
b. Win+P 进行多显示器切换 (接外接显示器或投影仪时很方便, 会自动调整分辨率)
c. Win+X 进入移动设置, 可以调整一堆和笔记本有关的设置
d. 在任务栏上按住图标向上推可以和右键一样调出 JumpList, 向上推这个动作可以更好衔接调出 JumpList 后的操作

</pre>
</div>

<div class="pt">II. Office 2010 安装教程</div>
<div class="pb">
<pre>
Win7 下, 在 Office_2010_Pro_x86_chs 目录里面的 setup.exe 上点右键, 选 "使用管理员模式运行"

在出来的第一个界面里选 [自定义], 勾选自己需要的组件并设定好个人信息后, 点 [现在安装]
  (推荐 Word/Excel/PowerPoint/OneNote/Visio Viewer 和通用组件, 如在公司内用, 再加 Outlook)

关闭杀毒软件, 使用 mini-KMS_Activator_v1.2_Office2010_VL_ENG.rar 里的 [mini-KMS] 完成激活
  (即 mini-KMS_Activator_v1.2_Office2010_VL_ENG.exe)

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

