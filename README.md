Rush
========

TabMenu-like simple command launcher for Maya

* You can add any commands you want
* Repeatable by G key

![gif](https://github.com/minoue/rush/blob/dev/docs/media/demo.gif)

## Installation

### Install from zip file
1. Download [zip](https://github.com/minoue/rush/releases/download/2.1.0/rush.zip) file and extract it.
2. Move the extracted "rush" folder to your user script directory. e.g. C:\Users\YOURNAME\Documents\maya\2017\scripts
3. Move the 'Rush.py' in rush\plug-ins directory to your maya plug-ins directory.  e.g C:\Users\YOURNAME\Documents\maya\plug-ins
4. Open maya and activate Rush.py in the plugin manager.

	  <img src="https://github.com/minoue/miExecutor/blob/media/images/plugin.png" width="600">

### Install using git
If git command is available to you, alternatively you can install using git command.  
In your user script directory,

```
git clone https://github.com/minoue/rush.git
```
Then, copy Rush.py to the maya plug-ins directory

## How to run


mel  

```
rush2;
```

in python

```
from maya import cmds
cmds.rush2()
```

You can open the hotkey editor and assign the command to any key you want.

## How to add commands
Commands can be added by editting/creating module files.
For example, here is the templete script in the module directory.


```python
class Commands(object):

    commandDict = {}

    def _sampleCommand(self):
        print "Hello World"
    commandDict['sampleCommand'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
```

To add new command, just add new method to the Command class.
Make sure to add underscore at the begging of the method name. Then, add new key/item to the commandDict. Key is the command name without underscore, and the item is an icon path(relative or absolute)


1. Create a new file.
	
	<img src="https://github.com/minoue/miExecutor/blob/media/images/createFile.png" alt="Drawing" style="width: 400px;"/>

2. Copy and paste the code from template file and edit your command as you want.
	
	<img src="https://github.com/minoue/miExecutor/blob/media/images/editFile.png" alt="Drawing" style="width: 400px;"/>

3. Save the file, go back to maya, and run reload command.

	<img src="https://github.com/minoue/miExecutor/blob/media/images/reload.png" alt="Drawing" style="width: 400px;"/>

4. You new command should be available in the completion.

	<img src="https://github.com/minoue/miExecutor/blob/media/images/runNewCommand.png" alt="Drawing" style="width: 400px;"/>

5. Done.

	<img src="https://github.com/minoue/miExecutor/blob/media/images/done.png" alt="Drawing" style="width: 400px;"/>


## Using custom module directory
You can choose any directories for you modules.  
Create '.rushConfig' file in your home directory and paths line by line.

eg.

```
/Users/XXXXXXX/Dropbox/dev/git/maya/extraModules
/Users/some/other/module/dir
```


## Credit
[Qt.py](https://github.com/mottosso/Qt.py) by Marcus Ottosson
<div>Icons made by <a href="http://www.flaticon.com/authors/simpleicon" title="SimpleIcon">SimpleIcon</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
