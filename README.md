Rush
========


TabMenu-like simple command launcher for Maya

* You can add any commands you want
* Repeatable by G key

![gif](https://github.com/minoue/miExecutor/blob/media/images/demo.gif)

## Requirements

[Qt.py](https://github.com/mottosso/Qt.py)

## Installation


* Download zip file and extract it to your maya script directory. Move the 'rush.py' in the repository to your maya plug-ins directory.


## Setup and how to run

1. import rush module first.

	```python
	import rush
	```

2. Then, activate the plugin.

  <img src="https://github.com/minoue/miExecutor/blob/media/images/plugin.png" alt="Drawing" style="width: 300px;"/>

3. Run the comamnd in your script editor.

    mel  

	```
	rush;
	```

	or in python

	```
	from maya import cmds
	cmds.rush()
	```

	Or open the hotkey editor and assign the command to any key you want.

	### Automatic setup
	You can skip the step 1 and 2 by adding the follwing code in your userSetup.py.

	```python
	from maya import cmds
	from maya import utils

	def setupRush():
	    try:
	        import rush
	        if not cmds.pluginInfo("rush.py", q=True, loaded=True):
	            cmds.loadPlugin("rush.py")
	    except:
	        print "Failed to import rush module"

	utils.executeDeferred(setupRush)
	```


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
/Users/XXXXXXX/Library/Preferences/Autodesk/maya/2015-x64/scripts/rush
/Users/XXXXXXX/Dropbox/dev/git/maya/extraModules
```
