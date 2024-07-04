# sing-box.conf
sing-box 的配置文件

## 源项目
[github](https://sing-box.sagernet.org/zh/)
[说明文档](https://sing-box.sagernet.org/zh)

## 启动命令

在配置文件见所在目录执行命令
~~~shell
sing-box run
~~~

### 使用 [windows](https://github.com/winsw/winsw) 中开机自启 sing-box

1. 下载 [winsw](https://github.com/winsw/winsw/releases)
2. 新建并编辑 xml 文件 sing-box.xml (名称随意), 配置模板 [winsw.xml](https://github.com/winsw/winsw#sample-configuration-file)
~~~xml
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
~~~
3. 执行命令,启动 sing-box 后台服务
~~~ shell
winsw.exe start sing-box.xml
~~~

## 将机场订阅转换为 sing-box 订阅
1. 没有服务器, 可以使用 开源项目 [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe), 搭建到 vercel, 进行在线转换,或者搭建到服务器或者本地
2. 使用 python 脚本进行订阅的转换, 本项目中的脚本暂时只支持转换 vless 协议
   + 可以进行本地手动进行转换, 生成 sing-box 配置文件, 或者克隆到服务器, 使用定时器定时执行脚本文件, 并发布到线上
