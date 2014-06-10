 miExecutor
========
TabMenu-like simple command launcher for Maya

![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/miExecutor_overview.gif)

## Requirements

PySide or PyQt4.

## Installation

In your maya script directory,

`git clone https://github.com/mifx/miExecutor.git`

or, download zip file from the right bottom of the repositry page and extract it.
Then, rename 'miExecutor-master' folder to 'miExecutor' and move it to the maya script directory.


## Usage


In maya hotkey editor, assign the following python command to any key you want.

* PyQt4:



        from miExecutor import miExecutor_PyQt4  
        reload(miExecutor_PyQt4)  
        miExecutor_PyQt4.MiExecutor().main()  


* PySide



        from miExecutor import miExecutor_PySide
        reload(miExecutor_PySide)
        miExecutor_PySide.MiExecutor().main() 

## How to add commands
1. Open **miExecutor/pref/miExecutorCommands.py** in your text editor.
2. * Add class methods you want like the following picture.
![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/newCommandSample.jpg)  
   * Make sure **all method names start with underscore**.
   * Add the following line at the end of methods.  
`commandDict['YOUR COMMAND NAME'] = "YOUR ICON NAME"`  
This can be used to call commands name and icon names in the main script.
   * 'YOUR COMMAND NAME' **must be same as the method name.**  
   * You can also use absolute paths for icon names if you want.
3. Go back to Maya and run 'reGenerateCommands' using miExecutor. Your new command will be added to the JSON file.  
![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/reGenerateCommands.jpg)  
4. Your new command should be ready to use.  
    ![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/yourNewCommand.jpg)  
    ![alt tag](https://dl.dropboxusercontent.com/u/408180/git/images/output.jpg)  
