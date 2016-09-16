miExecutor
========


## What's this?
TabMenu-like simple command launcher for Maya


![](https://dl.dropboxusercontent.com/u/408180/miexec/miExec.gif)

https://player.vimeo.com/video/144866783

## Requirements
PySide

## Installation
https://github.com/minoue/miExecutor/archive/1.3.0.zip

Download zip file from the above link and extract it. Rename miExecutor-1.3.0 directory to miExecutor and move it to the maya user script direcotry.

Directory structure should be something like this

```python
maya
|--version
|    |--script
|    |    |--miExecutor
|    |    |    |--__init__.py
|    |    |    |--miExecutor.py
|    |    |    |--README.md
|    |    |    |--app
|    |    |    |    |--mayaNode.py
|    |    |    |    |--module
|    |    |    |    |    |general
|    |    |    |    |    |...
```

or you can download through git.  
In maya scriiiipt directory,

```
git clone https://github.com/minoue/miExecutor.git
```


Then, try restarting Maya or run rehash command to activate the command.


## How to run

Just assgin the following command to any keys you want in hotkey editor.


```python
import miExecutor
reload(miExecutor)
miExecutor.main()
```


## How to add commands
Commands can be added by editting/creating module files in the module directory.
For example, this is templete script.


```python
""" class name must be 'Commands' """
class Commands(object):

    commandDict = {}

    def _sampleCommand(self):
        print "Hello World"
    commandDict['sampleCommand'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
```

To add new command, just add new method.
Make sure to add underscore at the begging of method name. Method name withougt underscore is its command name.
Once you finish adding method, just add new key/item to the commandDict. Key is the command name and item is the icon path.
You can not change dictionary name. It alwasy must be 'commandDict'. Icon path can be absolute.

Once you saved the file, go back to maya and reload it.

```python
reload(miExecutor)
```

Now your new command should be available.

Commands can be organized by module and directory. If you use directory, don't forget to add **\_\_init\_\_.py** so it can be loaded as package.




## Changing style
You can change style if you want. Just change 'style' option in pref.json.

### Standard
Same as the one in the node editor.  
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/standard.png" alt="nuke" style="width: 320px;"/>

### Nuke
Nuke-like style.  
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/nuke.png" alt="nuke" style="width: 320px;"/>

### NukeSquared
Nuke-like but rounded corner.  
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/nukeSquared.png" alt="nuke" style="width: 320px;"/>

### MediumRounded
a bit nicer looking.  
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/mediumRounded.png" alt="nuke" style="width: 320px;"/>

### AlfredLight
like Alfred in Mac  
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/alfredLight.png" alt="nuke" style="width: 320px;"/>

## AlfredDark
<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/alfredDark.png" alt="nuke" style="width: 320px;"/>


## Known issues

### Transparency
Backgraound transparency will not work in some environments as it's shown in the following image.
For example, windows and linux with compositeWindow off.

<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/alphaIssue.jpg" alt="nuke" style="width: 320px;"/>

Looks fine in my Mac.

### Drop Shadow
You might need to disable drop shadow effect. It's not from PySide but OS.

<img src="https://dl.dropboxusercontent.com/u/408180/blog/15_11_07_miExecutorUpdate/windowBorder.jpg" alt="nuke" style="width: 320px;"/>
Windows10

[How to Disable the Drop Shadows in Windows 10](http://www.howtogeek.com/197866/how-to-disable-the-drop-shadows-in-windows-10/)

## Libraries used
[Qt.py](https://github.com/mottosso/Qt.py)
