

# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    commandDict = {}

    def __init__(self):
        pass

    def _sampleCommand(self):
        print "Hello World"
    commandDict['sampleCommand'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
