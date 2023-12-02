# SenKongDao
明日方舟森空岛签到Python程序

---

## 加密参引用说明

加密参数计算方法使用[xxyz30的仓库](https://gitee.com/FancyCabbage/skyland-auto-sign/tree/master)的计算方法，

---

为了防止仓库消失，已删除GitHub Actions使用方法。

---

## 新版本脚本的使用说明（重要变动，cred变为token）

1.使用pip install -r requirments.txt来安装依赖（实际上只需要requests，已安装可以跳过这步）

2.在SenKongDao_config.txt中填入uid以及token字段，其中xxx为uid（游戏内名称下方ID，一串数字），yyy为token字段,uid与token字段用&符号隔开  

> **Token字段获取方式**
> 1. 打开[森空岛](https://www.skland.com)，按F12开启抓包模式，选择网络（或network）选项卡，选中保留日志（或preserve log），点击选中右边的XHR（或Fetch/XHR），然后接收验证码登录账号（已登录的话需要退出重新登陆）
>    
> 2. 找到token_by_phone_code点击选中，然后点击右边的响应（或Response）,可以看到右侧这种样式的一串，其中token右侧引号里的就是要获取的token字段，{"status":0,"type":"A","msg":"OK","data":{"token":"aaaaaaaaaaaaa"}}
>    
> 3. 将该字段填入SenKongDao_config.txt即可使用脚本，示例：123345&aaaaaaaaaaaaa。（其中12345是示例的uid（游戏内uid），aaaaaaaaaaaaa为第二步中获取的token）
>
> 4. 如果有多个账号需要获取，建议使用浏览器的隐身模式
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
