#
# IMPORTS
#
import cmd
import callCenter
#
# CONSTANTS AND DEFINITIONS
#

#
# CODE
#
class CommandInterpreter(cmd.Cmd):

    def __init__(self):
        self.cCenter = callCenter.CallCenter()
        
        # initialize the parent class
        super(CommandInterpreter, self).__init__() 
    # __init__()

    def showMessage(self, msg):
        print(str(msg))
    # showMessage()
    
    # TODO: remove this parameterUnesed, but
    # fires 'takes 1 positional arguments but 2 were given'
    def do_show(self, paramUnused):
        """
        I print the status of the Call Center in the moment
        """
        self.cCenter.showStatus()
    # do_test()
            
    def do_call(self, callID):
        """
        I deal with the call command. 

        :param callID: call identification
        :type  callID: int

        :return: nothing
        :rtype : none
        """
        self.cCenter.createCall(callID)
        # log message
    # do_call()

    
    def do_answer(self, operatorID):
        """
        I deal with the answer command.

        :param operatorID: operator identification
        :type  operatorID: string

        :return: nothing
        :rtype : none
        """
        self.cCenter.answerCall(operatorID)
    # do_answer()

    
    def do_reject(self, operatorID):
        """
        I deal with the reject command

        :param ID: operator identification
        :type  ID: string

        :return: nothing
        :rtype : none
        """
        self.cCenter.rejectCall(operatorID)
    # do_reject()
    
    def do_hangup(self, callID):
        """
        I Handle the hangup command

        :param callID: call identification
        :type  callID: int

        :return: nothing
        :rtype : none
        """
        self.cCenter.hangupCall(callID)
    # do_hangup()
    
    def do_EOF(self, line):
        """
        I handle the end of file command

        :return: always returns true
        :rtype : boolean
        """
        self.cCenter.stopProgram()
        return True
    # do_EOF()
# CommandInterpreter()

if __name__ == '__main__':
    CommandInterpreter().cmdloop()
