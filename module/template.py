

# class name must be 'Commands'
class Commands(object):

    #Name of dictionary must be this module name + 'Dict'
    templeteDict = {}

    def __init__(self):
        pass

    def _sampleCommand(self):
        print "Hello World"
    templeteDict['sampleCommand'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
