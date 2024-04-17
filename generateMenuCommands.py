from collections import OrderedDict

from maya import cmds
from maya import mel
import json
import uuid


def getCommand(menuItemObject, data, menuTitle, parentLabel=None):

    itemLabel = cmds.menuItem(menuItemObject, q=True, label=True)
    itemCommand = cmds.menuItem(menuItemObject, q=True, command=True)
    isOptBox = cmds.menuItem(menuItemObject, q=True, isOptionBox=True)
    isSubMenu = cmds.menuItem(menuItemObject, q=True, subMenu=True)
    sourceType = cmds.menuItem(menuItemObject, q=True, sourceType=True)
    itemIcon = cmds.menuItem(menuItemObject, q=True, image=True)

    if itemLabel.startswith("/"):
        return

    if isSubMenu:
        subMenuItemObjs = cmds.menu(menuItemObject, q=True, itemArray=True)

        if subMenuItemObjs is None:
            # Do nothing eg. Recent files..
            return

        for subMenuItemObj in subMenuItemObjs:
            getCommand(subMenuItemObj, data, menuTitle, itemLabel)

    else:
        if itemCommand is None:
            return

        if isOptBox:
            dataDict = list(data.items())[-1][1]
            prevLabel = dataDict["label"]

            if ":" in prevLabel:
                prevLabel = prevLabel.split(" : ")[0]

            itemLabel = prevLabel + " Options"

        if isinstance(itemCommand, str):

            if parentLabel is not None:
                itemLabel = "{} : {}".format(itemLabel, parentLabel)

            id = str(uuid.uuid4())
            data[id] = {
                "label": itemLabel,
                "sourceType": sourceType,
                "command": itemCommand,
                "category": "",
                "module": menuTitle,
                "icon": itemIcon,
            }


def buildData():

    # get the main window
    gMainWindow = mel.eval('$temp=$gMainWindow')

    # get all the menus that are children of the main menu
    mainWindowMenus = cmds.window(gMainWindow, query=True, menuArray=True)

    for menuObj in mainWindowMenus:
        cmd_data = OrderedDict()

        if "hotbox" in menuObj.lower():
            continue

        if "help" in menuObj.lower():
            continue

        menuName = cmds.menu(menuObj, q=True, label=True)
        menuItems = cmds.menu(menuObj, q=True, itemArray=True)

        menuName = menuName.replace("/", "_")

        path = "PATH/TO/CMD_DIR/{}.json".format(menuName)

        if menuItems is None:
            continue

        for item in menuItems:
            getCommand(item, data=cmd_data, menuTitle=menuName)

        with open(path, "w") as file:
            json.dump(
                cmd_data,
                file,
                sort_keys=False,
                indent=4,
                separators=(',', ': '))


if __name__ == "__main__":
    buildData()
