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

	![image here](asdfsdf)
	
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
Commands can be added by editting/creating module files in the module directory.
For example, here is the templete script.


```python
class Commands(object):

    commandDict = {}

    def _sampleCommand(self):
        print "Hello World"
    commandDict['sampleCommand'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
```

To add new command, just add new method to the Command class.
Make sure to add underscore at the begging of the method name. Then, add new key/item to the commandDict. Key is the command name which is the method name without underscore, and item is an icon path(relative or absolute)

1. Create a new file.  
	![image here](asd)
	
2. Copy and paste template.  
	![image here](asdf)
	
3. Add a command.  
	![image here](asdf)

4. Done.  
	![image here](asdf)