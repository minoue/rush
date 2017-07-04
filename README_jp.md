Rush
========


Maya用のタブメニュー風コマンドランチャー

* 好きなコマンドを登録可能
* Gキーでリピート可能

![gif](https://github.com/minoue/miExecutor/blob/media/images/demo.gif)

## Requirements

[Qt.py](https://github.com/mottosso/Qt.py)

## Installation and setup

### Install from zip file
1. [zip](https://github.com/minoue/rush/archive/master.zip)をダウンロードし、解凍したあとにできる 'rush-master' フォルダを "rush"にリネームする。
2. "rush" フォルダをMayaのスクリプトフォルダに移動する。 例 C:\Users\YOURNAME\Documents\maya\2017\scripts
3. "rush/plug-ins"フォルダの中にある'Rush.py'をMayaのプラグインフォルダに移動する。
4. MayaのプラグインマネージャからRush.pyを有効にする。

	  <img src="https://github.com/minoue/miExecutor/blob/media/images/plugin.png" alt="Drawing" style="width: 300px;"/>

### Install using git
In your user script directory,

```
git clone https://github.com/minoue/rush.git
```
Then, copy Rush.py to the maya plug-ins directory

## How to run


mel  

```
rush;
```

in python

```
from maya import cmds
cmds.rush()
```

You can open the hotkey editor and assign the command to any key you want.

### Making commands repeatable by G key
You have to load rush module to make commands repeatable by G key. Run the following command in the script editor, or simply **add the line to your userSetup.py**.

```python
import rush
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


## Credit
<div>Icons made by <a href="http://www.flaticon.com/authors/simpleicon" title="SimpleIcon">SimpleIcon</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
