class Spam(object):
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    
    @staticmethod
    def printNumInstances():
        print Spam.numInstances
        
    #printNumInstances = staticmethod(printNumInstances)