 miExecutor
========
TabMenu-like simple command launcher for Maya

![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/miExecutor_overview.gif)


Differences between this script and the one in Node Editor in behavior.  
ノードエディタのタブメニューとの違い  

* You can add any commands you want.
* Repeatable by G key  
* You don't need to complete commands. Just you can hit Enter once you got it on the top of the completion list.  
    
    
* 好きなコマンドを登録できる
* Gキーでピート可能
* 候補リストの一番上にコマンドが来た時点でエンターを押せば実行可能 


## Requirements

PyQt4 or PySide

## Installation


[http://github.com/minoue/miExecutor/archive/1.1.0.zip](https://github.com/minoue/miExecutor/archive/1.1.0.zip)  


* Download zip file and extract it, then rename the folder to 'miExecutor'  
* Move the folder to your maya script directory.  The directory structure should be something like this.

        maya
        |--version  
        |    |--script
        |    |    |--miExecutor
        |    |    |    |--__init__.py
        |    |    |    |--miExecutor.py
        |    |    |    |--  ....
        |    |    |    |--module
        |    |    |    |    |--mayaNode.py



* Restart maya or do 'rehash;' command.  
* Assign the following python command to any key you want.  

    PyQt4  

            from miExecutor import miExecutor
            reload(miExecutor)  

    PySide  

            from miExecutor import miExecutor_pyside
            reload(miExecutor_pyside)


## How to add commands

1. Copy and rename **miExecutor/module/templete.py** to whatever you like.  

	 ![](https://dl.dropboxusercontent.com/u/408180/git/images/rename.jpg)

2. Open the file and add any class methods like the following picture.  

	![](https://dl.dropboxusercontent.com/u/408180/git/images/yourModule2.jpg)

   * Make sure **all method names start with underscore**.
   * Add the following line at the under the method.  
`yourCommandDict['YOUR COMMAND NAME'] = "YOUR ICON NAME"`  
This dictionary is used to call commands names and icon paths in the main script.
   * 'YOUR COMMAND NAME' **must be same as the method name.(no underscore)**  
   * You can also use absolute paths for icon names if you need.  
  

3. Once you save the file, your new command should be ready to use.  
	![](https://dl.dropboxusercontent.com/u/408180/git/images/yourNewCommand2.jpg)  

	![](https://dl.dropboxusercontent.com/u/408180/git/images/helloSphere.jpg)  
