Rush
========

TabMenu-like simple command launcher for Maya

![gif](https://github.com/minoue/miExecutor/blob/media/images/demo.gif)

## Requirements

[Qt.py](https://github.com/mottosso/Qt.py)

## Installation


## How to run


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
