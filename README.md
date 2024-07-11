原始项目 [sing-box](https://sing-box.sagernet.org/zh/)

##### 编辑配置文件 config.json

1.直接编辑, 查看配置[文档](https://sing-box.sagernet.org).  
2.使用第三方软件进行转换, 使用自定义脚本, 或者 github 中的项目 [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe).  

**使用自定义脚本进行转换**  
1.使用 python 脚本进行转换  
> 执行下面的命令, 获取脚本文件. 编辑配置文件 config.json  
``` shell
git clone https://github.com/9lit/sing-box.conf.git
```

2.使用 shell 脚本进行订阅转换  
``` shell
curl http://text.1210923.xyz/text/sing-box/sub_sing-box.sh | bash
# 如果需要上传到 github 项目, 则需要传入项目在本地的地址, 并且具有推送权限
curl http://text.1210923.xyz/text/sing-box/sub_sing-box.sh | bash -s your/path
```

##### 在 windows 中,使用 [winsw](https://github.com/winsw/winsw) 管理 sing-box 程序

1.下载 [winsw](https://github.com/winsw/winsw/releases)  
2.新建并编辑 xml 配置文件 sing-box.xml (名称随意), 官方配置模板 [winsw.xml](https://github.com/winsw/winsw#sample-configuration-file)  
3.安装并启动 winsw 服务  
``` shell
# 安装
winsw.exe install sing-box.xml
# 启动
winsw.exe start sing-box.xml
# 重启/停止/卸载
restart/stop/uninstall
```
```
# 配置模板文件
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
