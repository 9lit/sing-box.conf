from base64 import b64decode
import urllib
import urllib.request
import json
from config import *

def read(path):
    ext = path.split(".")[-1]
    with open(path, "r", encoding='utf-8') as f: return json.load(f) if ext == "json" else f.read()


def write(context, path):
    with open(path, "w", encoding='utf-8') as f: json.dump(context, f, indent=4, ensure_ascii=False)

def get_context(path:str) -> str:
    """获取订阅"""

    def requests_context():

        headers = {
            "User-Agent":"Gecko/20100101 Firefox/127.0 Chrome/126.0.0.0",
            "Content-Type": "text/plain; charset=utf-8"
        }
        req = urllib.request.Request(path, headers=headers)
        return urllib.request.urlopen(req).read()
    
    def read_context(): return read(path)
    
    return requests_context() if "https://" in path else read_context()

def decode_context(context:str) -> list:
    """对订阅地址进行解码"""
    share_links = b64decode(context).decode('utf-8').splitlines()
    return share_links


def get_configs(share_links):
    def set_vless_config(url):

        def get_tag():
            tag = urllib.parse.unquote(url.fragment)
            return tag if tag else 'none'
        
        def get_tls_config():
            tls_config = {}
            for tls_config_string in url.query.split("&"):
                key, value = tls_config_string.split("=")
                tls_config[key] = value

            return tls_config


        uuid, server = url.netloc.split("@")    
        server, server_port = server.split(":")
        if not server: return False
        
        tls = get_tls_config()


        return  {
                "tag": get_tag(),
                "server": server,
                "server_port": int(server_port),
                "uuid": uuid,
                "type": url.scheme,
                "packet_encoding": "xudp",
                "tls":{
                    "enabled": True,
                    "insecure": False,
                    "server_name": tls['sni'],
                    "utls": {
                        "enabled": True,
                        "fingerprint": tls['fp'], 
                    }
                },
                "transport": {
                    "type": tls['type'],
                    "path": urllib.parse.unquote(tls['path']),
                    "headers": {
                        "Host": tls['host']
                    }
                }
                
            }
    
    def get_config(share_link):
        url = urllib.parse.urlsplit(share_link)
        
        config = set_vless_config(url)

        return config if url.scheme == "vless" and config else False

    return [get_config(share_link) for share_link in share_links if get_config(share_link)]

def set_tag(configs):
    """设置标签"""

    def delete_tag_string(tag:str):
        """删除多余的标签"""
        redundant_string = ["TG@ZDYZ2 -"]
        if not DEL_TAG_FLAG: return tag
        for del_string in redundant_string: return "".join(tag.split(del_string))
        
    def rename_repeatability_tag(first_tag:str):
        """重复的标签进行重命名"""
        i = 0
        for index, config in enumerate(configs):
            if first_tag != config['tag'] : continue
            i += 1
            if i == 1: continue
            configs[index]['tag'] = '%s-%i' % (config['tag'], i-1)
        return configs

    for index, config in enumerate(configs):
        configs[index]['tag'] = delete_tag_string(configs[index]['tag'])
        configs = rename_repeatability_tag(config['tag'])
        
    return configs


def update_sing_box_config(configs, template_config):
    """读取模板配置文件, 将节点写入到配置模板中去"""

    # 获取 tag 列表
    def set_outbounds_tag():
        tag = [config['tag'] for config in configs]
        template_config['outbounds'][0]['outbounds'] = tag

    def set_outbounds():
        template_config['outbounds'] = template_config['outbounds'] + configs

    
    set_outbounds_tag(); set_outbounds()
    return template_config

def upload():
    if not UPLOAD_FLAG: return
    import os
    os.system(f"cd {UPLOAD_PATH} && git pull && cp {OUT_CONFIG_PATH} {UPLOAD_PATH} && git add config.json && git commit -am '更新配置文件' && git push")

def main():

    context = get_context(path=CONTEXT_PATH)
    share_links = decode_context(context)
    config = get_configs(share_links); config = set_tag(config)
    template_config = read(path=TEMPLATE_CONFIG_PATH)
    template_config = update_sing_box_config(configs=config, template_config=template_config)

    write(template_config, path=OUT_CONFIG_PATH)
    upload()


if __name__ == "__main__":
    main()