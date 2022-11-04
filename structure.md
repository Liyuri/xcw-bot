* main.py
* config.yaml
* log
  * INFO
  * ERROR
* modules
  * mod 1
  * mod 2
  * ...
* logs_and_events
  * 1
* randosoru(兰德索尔)
  * starter
  * managers
    * 加载重载卸载插件
    * 权限系统(咕咕咕)
    * 频率限制系统(咕咕咕)
  * orm
  * configs
  * resource

```mermaid
graph LR


main.py --launch_bot--> app
main.py --> initer

initer --> check_config
initer --> create_database
initer --> refresh_group_info
initer --> load_managers

main.py --> get_and_save_logs
main.py --> load_modules

config.yaml --config_类--> config_实例
config_实例 --> app
```