# SenKongDao
明日方舟森空岛签到Python程序

1.使用pip install -r requirments.txt来安装依赖（实际上只需要requests，已安装可以跳过这步）

2.在SenKongDao_config.txt中填入uid以及cred字段，其中xxx为uid（游戏内名称下方ID，一串数字），yyy为cred字段,uid与cred字段用&符号隔开  

> **Cred字段获取方式**
> 1. 打开[森空岛](https://www.skyland.com)并登录，如果有多个账号需要获取，建议使用浏览器的隐身模式
>    
> 3. 按下F12打开网页开发工具，切换至控制台选项卡，输入`localStorage.getItem("SK_OAUTH_CRED_KEY");`并回车
>    
> 5. 控制台返回的一串长度为32的数字字母组合字符串即为所需Cred字段
>
支持多账号，每行一个账号即可  

以下为某个账户的实例：  

xxxxxx&yyyyyyyyyy
