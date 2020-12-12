"""
交易对象对外开放的API
输入股票的order_id  以及 细粒度划分 
0, 给出起点 终点 
1， 按日 
2， 按分钟
3， 按财务周期
"""
import yaml
import os

FILE_PATH = os.path.dirname(__file__)
CONFIG_PATH = "/".join(FILE_PATH.split("/")[:-1])   # only get up root

class DataProxy(object):
    CONFIG_YAML_PATH = CONFIG_PATH + "/config.yaml"
    def __init__(self, order_id: str, start_date: str, end_date: str, frequency_type: str):
        pass

        
    
    def _get_config_parse(self, file_path: str):
        f = open(file_path, "r", encoding="utf-8")
        content_text = f.read()
        yaml_reader = yaml.load(content_text)
        return yaml_reader

        
        

if __name__ == '__main__':
    a = CONFIG_PATH
    print(a)
    file_path = "/Users/yaotianshu/Downloads/HangzhouNo2/bigwin/config.yaml"
    f = open(file_path, "r", encoding="utf-8")
    content_text = f.read()
    yaml_reader = yaml.load(stream=content_text, Loader=yaml.FullLoader)
    print(yaml_reader)
    print(yaml_reader["TRANSCATION"])