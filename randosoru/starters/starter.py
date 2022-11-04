import time
import pkgutil

from loguru import logger

from creart import create
from graia.ariadne.app import Ariadne
from randosoru.configs.load_configs import BotConfig
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)

from graia.saya import Saya


class Starter(object):
    
    start_time = time.time()
    
    @staticmethod
    def gain_app(bot_config: BotConfig) -> Ariadne:
        
        http_client_host = str(bot_config.mirai_url) + ":" + str(bot_config.mirai_http_port)
        ws_client_host = str(bot_config.mirai_url) + ":" + str(bot_config.mirai_ws_port)
        
        app = Ariadne(
            connection=config(
                bot_config.xcw_qq,
                str(bot_config.verify_key),
                HttpClientConfig(host=http_client_host),
                WebsocketClientConfig(host=ws_client_host)
            ),
        )
        
        return app
    
    @staticmethod
    def gain_saya_modules():
        saya = create(Saya)
        
        with saya.module_context():
            for module_info in pkgutil.iter_modules(["modules"]):
                # pkgutil.iter_modules() 要传入一个列表作为参数，返回一个 generator
                if module_info.name.startswith("_"):  # name 是 generator 中元素的一个属性
                    # 假设模组是以 `_` 开头的，就不去导入
                    # 根据 Python 标准，这类模组算是私有函数
                    continue
                saya.require(f"modules.{module_info.name}")
