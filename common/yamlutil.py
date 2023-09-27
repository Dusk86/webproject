import pytest
import yaml

class YamlUtil:
    # 登录/注册
    def userlogin(self, yaml_path, part):
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            new_value = value[part]
            return new_value
