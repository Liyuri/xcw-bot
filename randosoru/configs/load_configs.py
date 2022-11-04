import yaml
import os
from pathlib import Path
from loguru import logger


class BotConfig(object):
    
    __instance = None
    
    xcw_qq: int
    Yuuki_qq: int
    verify_key: str
    mirai_url: str
    mirai_http_port: int
    mirai_ws_port: int
    
    def __new__(cls):
        
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self):
        
        with open(
            Path(os.getcwd()) / "config.yaml",
            # "D:/codes/python/xcw-myBot/xcw-bot/config.yaml",
            "r",
            encoding="utf-8"
        ) as f:
            config = yaml.safe_load(f.read())
        
        for key in config.keys():
            setattr(self, key, config[key])


if __name__ == "__main__":
    b = BotConfig()
