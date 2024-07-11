# sing-box 配置

1. 原始项目 [sing-box](https://sing-box.sagernet.org/zh/)

2. 使用 [windows](https://github.com/winsw/winsw) 中开机自启 sing-box

+ 下载 [winsw](https://github.com/winsw/winsw/releases)
+ 新建并编辑 xml 文件 sing-box.xml (名称随意), 配置模板 [winsw.xml](https://github.com/winsw/winsw#sample-configuration-file)
~~~
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
+ 执行命令,启动 sing-box 后台服务
~~~ shell
winsw.exe start sing-box.xml
~~~

3. 将机场订阅转换为 sing-box 订阅
+ 没有服务器, 可以使用 开源项目 [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe), 搭建到 vercel, 进行在线转换,或者搭建到服务器或者本地
+ 使用脚本进行转换, 定时执行上传到服务器或者本地文件夹
  + 使用 python 脚本进行订阅的转换, 本项目中的脚本暂时只支持转换 vless 协议
  + 使用 shell 脚本执行
    
