 miExecutor
========
TabMenu-like simple command launcher for Maya

![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/miExecutor_overview.gif)

## Requirements

PyQt4.

## Installation


[http://github.com/minoue/miExecutor/archive/1.0.0.zip](https://github.com/minoue/miExecutor/archive/1.0.0.zip)



1. Download zip file and extract it, then rename the folder to 'miExecutor'  
2. Move the folder to your maya script directory.
3. Restart maya or do 'rehash;' command.
4. Assign the following python command to any key you want.

        from miExecutor import miExecutor
        reload(miExecutor)  


## How to add commands

1. Copy and rename **miExecutor/module/templete.py** to whatever you like
	 ![](https://dl.dropboxusercontent.com/u/408180/git/images/rename.jpg)

2. Open the file and add any class methods like the following picture.  

![](https://dl.dropboxusercontent.com/u/408180/git/images/yourModule2.jpg)

   * Make sure **all method names start with underscore**.
   * Add the following line at the under the method.  
`yourCommandDict['YOUR COMMAND NAME'] = "YOUR ICON NAME"`  
This dictionary is used to call commands names and icon paths in the main script.
   * 'YOUR COMMAND NAME' **must be same as the method name.(no underscore)**  
   * You can also use absolute paths for icon names if you need.
4. Once you save the file, your new command should be ready to use.  
	![](https://dl.dropboxusercontent.com/u/408180/git/images/yourNewCommand2.jpg)  
	![](https://dl.dropboxusercontent.com/u/408180/git/images/helloSphere.jpg)  

