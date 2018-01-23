# -*- coding: utf-8 -*-
    
if __name__ == '__main__':

    bRun = True
    test = unicode(u'båt')
    print 'Test is:', test
    print 'Testing again åäö'

    while bRun:
        availableCommands = unicode(u'available commands: alfa, båt, quit: ')
        print availableCommands
        temp = raw_input()
        strCommand = unicode(temp)

        if strCommand == u'alfa':
            print 'Command is:', strCommand

        if strCommand == u'båt':
            print 'Command is:', strCommand

        if strCommand == u'quit':
            bRun = False
        
    #getbus()
    
        


