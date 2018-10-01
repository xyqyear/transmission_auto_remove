# transmission_auto_remove
这个程序可以帮助你移除已经停止的transmission任务

应用场景是你设置了一个发送ratio,然后你想要一键移除已经做种完成的种子

如果你创建一个crontab的任务,就可以自动定时移除种子啦

配置在py文件里面的最前面几行改

比如我现在使用的情况就是设置的发送ratio是5.0,然后创建了一个每一个小时执行的任务,这个任务就能帮我每个小时检查是否有种子做完种了需要删除.

this program can help you delete the torrent in transmission which is already stopped

the config is in the front lines of the .py file

if you want to remove the torrent automatically, you can just create a crontab task(on Linux).