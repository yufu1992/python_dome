#Demo

一、首先下载安装git：
	Windows: https://gitforwindows.org/index.html
	Mac: https://sourceforge.net/projects/git-osx-installer/
	Linux: 在终端输入命令行安装
	Debian系列: apt-get install git
	Fedora: yum install git-core

二、在git上创建仓库：
	点击加号，选择New repository选项。
	填好仓库名，选择是否公开还是私有，然后点击创建。
	创建好后跳转到仓库的主页，记好仓库地址。

三、在本地电脑系统创建本地仓库（项目文件）：
	命令：
		mkdir Demo
		cd Demo
		gedit README.md
		上面命令是创建项目文件，并在文件里创建README.md文件，gedit是一个创建.md工具。
	在README.md文件里填写项目描述内容，然后在项目文件的目录下输入命令：
		git init
		这是git的初始化操作，将一个已存在的文件夹，置于git的控制管理之下。

四、提交代码：
	命令：
		git add + 文件名/目录名
		git status
		git commit -m "提交代码的注释描述等文字"
	遇到：
		git config --global user.name "YourName"
		git config --global user.email "YourEmail@xxx.com"
		设置你的名字和email设置完后可以继续 git commit -m "***" 的操作。

五、与github远程仓库同步：
	命令：
		git remote add origin 仓库链接
			     （仓库小名）（仓库链接）
		git push littleName master
			   (仓库小名)（分支名）

六、克隆github上的仓库到本地：
	命令：
		git clone [url]
