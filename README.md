# SenKongDao
明日方舟森空岛签到Python程序

---

## 目前脚本已失效
早些时间脚本模拟旧版本签到，就在最近这种方式被阻止了。  
在签到的时候多了几个加密参数，导致脚本无限期停更。

注：新版app使用了梆梆企业加密。

---

## 旧版本脚本的使用说明（已失效）

1.使用pip install -r requirments.txt来安装依赖（实际上只需要requests，已安装可以跳过这步）

2.在SenKongDao_config.txt中填入uid以及cred字段，其中xxx为uid（游戏内名称下方ID，一串数字），yyy为cred字段,uid与cred字段用&符号隔开  

> **Cred字段获取方式**
> 1. 打开[森空岛](https://www.skland.com)并登录，如果有多个账号需要获取，建议使用浏览器的隐身模式
>    
> 3. 按下F12打开网页开发工具，切换至控制台选项卡，输入`localStorage.getItem("SK_OAUTH_CRED_KEY");`并回车
>    
> 5. 控制台返回的一串长度为32的数字字母组合字符串即为所需Cred字段
>
支持多账号，每行一个账号即可

以下为某个账户的实例：  

xxxxxx&yyyyyyyyyy

### 或使用 docker 运行
 1. 参考上面教程新建 `SenKongDao_config.txt` 文件，填入 `uid` 以及 `cred` 字段
 2. 运行 `docker run -v ./SenKongDao_config.txt:/app/SenKongDao_config.txt maojuan180/senkongdao` 其中 `./SenKongDao_config.txt` 为配置文件路径，可自行修改

### 定时任务相关使用说明  
 1. 在任意目录使用`crontab -e`命令来编辑 cron 文件，第一次运行会让你选择一个编辑器，选择推荐的第一个编辑器即可。
 2. 在最后一行添加`10 0 * * * /usr/bin/docker start xxxx(容器名称或容器id)`，按`Ctrl+X`退出编辑，按`Y`确定，最后按`Enter（回车）`来保存。
 3. 使用`docker ps -a`命令来查询docker容器的名称或者id。
 4. 第二步中cron表达式意思为每天的凌晨0:10运行，可以自行修改。
 5. 如果docker目录不对，可以用命令`which docker`查看一下自己docker的位置，修改第二步的命令。

## 贡献者

<a href="https://github.com/Maojuan-lang/SenKongDao/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Maojuan-lang/SenKongDao" />
</a>
