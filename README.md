原始项目 [sing-box](https://sing-box.sagernet.org/zh/)

### 编辑配置文件 config.json

直接编辑

使用第三方软件进行转换
1. [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe)
2. 使用自定义脚本进行转换

2.1 使用 python 脚本进行转换
执行下面的命令, 获取脚本文件. 编辑配置文件 config.json
``` shell
git clone https://github.com/9lit/sing-box.conf.git
```

2.2 使用 shell 脚本进行订阅转换

``` shell
curl http://text.1210923.xyz/text/sing-box/sub_sing-box.sh | bash
```
如果需要上传到 github 项目, 则需要传入项目在本地的地址, 并且具有推送权限

``` shell
curl http://text.1210923.xyz/text/sing-box/sub_sing-box.sh | bash -s your/path
```

### 使用 [winsw](https://github.com/winsw/winsw) 管理 sing-box 程序

下载 [winsw](https://github.com/winsw/winsw/releases)

新建并编辑 xml 文件 sing-box.xml (名称随意), 配置模板 [winsw.xml](https://github.com/winsw/winsw#sample-configuration-file)

```
<service>
  <id>0</id>
  <name>sing-box</name>
  <description>sing-box 自启动后台服务</description>
  <env name="sing-box" value="Your_program_path"/>
  <download from="Your_subscribe" auth="sspi" />
  <executable>%sing-box%sing-box.exe</executable>
  <arguments>run</arguments>
  <log mode="reset" />
  <onfailure action="restart" />
</service>
```
执行命令,启动 sing-box 后台服务
> start | status | restart | stop

``` shell
winsw.exe start sing-box.xml
```
