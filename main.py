from loguru import logger

from randosoru.configs.load_configs import BotConfig
from randosoru.starters.starter import Starter


Kyoka = BotConfig()  # 众所周知，小仓唯的声优是冰川镜华
Yuuki = Starter()  # 佑树君是镜华的启动器（等着吃牢饭吧
xcw = Yuuki.gain_app(Kyoka)  # 获取 app
Yuuki.gain_saya_modules()  # 获取 modules 文件夹下的插件

xcw.launch_blocking()  # 这里没有抄红猪佬的代码，因为要致敬 graiax
