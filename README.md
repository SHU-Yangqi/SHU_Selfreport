# SHU_Selfreport

使用selenium配合win10的任务计划程序实现每日一报自动填报

首先下载谷歌浏览器对应版本的chromedriver.exe，记住其路径，在selfreport.py 文件的对应路径更改为你的电脑上chromedriver.exe的位置

在搜索框中搜索任务计划程序

![image](https://user-images.githubusercontent.com/72846399/130378839-5659f8c9-b3d2-4c7c-8c8e-6f4baba6e973.png)

点击操作 创建基本任务

任意输入任务名称

![image](https://user-images.githubusercontent.com/72846399/130378971-33fd9343-ae67-44bb-b2b0-d78a98e7c0fe.png)

“每日”一报，所以触发器选择每天

![image](https://user-images.githubusercontent.com/72846399/130379047-b7504247-20e4-4ffd-a73f-fb7699c3cc95.png)

设置你想要任务开始的时间，比如零点。

![image](https://user-images.githubusercontent.com/72846399/130379118-aa8ceba8-5bfc-429c-a1e8-7fe9f97cbb7d.png)

选择启动程序

![image](https://user-images.githubusercontent.com/72846399/130379139-a48e21b6-2f46-40a2-b1d2-883414781bfc.png)

选择批处理脚本

![image](https://user-images.githubusercontent.com/72846399/130379202-729ccd19-9e4d-4890-b577-2bbd18bc7da4.png)

任务计划就完成了

在编写批处理脚本的时候要注意，一定要使用selfreport.py的绝对路径，因为任务计划程序执行的时候使用的是初始的路径，也就是你打开cmd时候的路径，如果你将run.bat 与selfreport.py放在同一目录下，run.bat文件中使用相对路径时，双击run.bat文件可以正常运行，但是任务计划程序运行时无法找到selfreport.py这个文件。如果是十二点前睡觉的好孩子，可以在run.bat最后加上一行 shutdown /p 
这样程序填报完每日一报后就会自动关机了，不用担心电脑开一晚上浪费电了。
