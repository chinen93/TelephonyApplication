#
# IMPORTS
#
import cmd
import operatorCall
import sys
#
# CONSTANTS AND DEFINITIONS
#

#
# CODE
#
class CallCenter(cmd.Cmd):
    """
    I am responsible for handling the Call Center's commands
    """
    def __init__(self):
        """
        I initialize the Call Center

        :return: nothing
        :rtype : none
        """

        # Create lists to store Operators and Calls
        self.operators = {}
        self.waitingQueue = []
        
        # Create some operators
        self.operators['A'] = operatorCall.OperatorCall('A')
        self.operators['B'] = operatorCall.OperatorCall('B')

        # initialize the parent class
        super(CallCenter, self).__init__() 
    # __init__()

    def findOperator(self, operatorID):
        """
        I find  in the dictionary of operators.
        To find an operator with the ID equals :param operatorID:
        
        :param operatorID: operator identification
        :type  operatorID: string

        :return : Operator wanted
        :rtype  : operadorCall.OperatorCall
        """
        try:
            operator = self.operators[operatorID]
        except KeyError:
            # if the operator don't exist, exit function and log message
            print('Operator with ID "' + str(operatorID) + '" do not exist')
            return None 
        else:
            return operator
    # findOperator()

    def nextCallID(self):
        """
        I get the next call in the waiting queue and return its ID

        :return : Call Identification 
        :rtype  : int
        """
        # The waiting queue is empty
        if self.waitingQueue.__len__() == 0:
            return -1

        # get first call in the waiting queue
        callID = self.waitingQueue[0]
        self.waitingQueue.remove(self.waitingQueue[0])
        
        return callID
    # nextCall

    def deliverNextCall(self, operator):
        """
        I delivery the next call in the waiting queue to an operator
      
        :param operator: operator who will receive the call
        :type  operator: operatorCall.OperatorCall

        :return : nothing
        :rtype  : none
        """
        callID = self.nextCallID()

        # There is no waiting call
        if callID == -1:
            operator.setStatus(operatorCall.AVAILABLE)
            return

        operator.setStatus(operatorCall.RINGING, callID)
        print('Call ' + str(callID) +
              ' ringing for operator '+ operator.ID)
    # deliveryNextCall()
    
    # TODO: remove this parameterUnesed, but
    # fires 'takes 1 positional arguments but 2 were given'
    def do_test(self, paramUnused):
        """
        I print the status of the Call Center in the moment
        """
        print('Number of Operators: ' + str(self.operators.__len__()))
        for op in self.operators.values():
            print('Operator: ' + op.ID + 
                  '; Status: ' + op.getStatus() +
                  '; Call : ' + str(op.callID))
        print('Number of Waiting Calls: ' + str(self.waitingQueue.__len__()))
        for callID in self.waitingQueue:
            print('Call: ' + callID)
    # do_test()
            
    def do_call(self, callID):
        """
        I deal with the call command. 
        If there is an operator available the call is passed to him, 
        otherwise the call is placed in the waiting queue

        :param callID: call identification
        :type  callID: int

        :return: nothing
        :rtype : none
        """

        # log message
        print('Call ' + str(callID) + ' received')

        waiting = True
        # find an operator to deliver the call
        for op in self.operators.values():
            if op.status == operatorCall.AVAILABLE and waiting == True:
                op.setStatus(operatorCall.RINGING, callID)
                print('Call ' + str(op.callID) +
                      ' ringing for operator '+ op.ID)
                waiting = False

        # put the call in the waiting queue
        if waiting:
            self.waitingQueue.append(callID)
            print('Call ' + str(callID) + ' waiting in queue')
    # do_call()

    
    def do_answer(self, operatorID):
        """
        I deal with the answer command.
        Find the operator and make him answer a call

        :param operatorID: operator identification
        :type  operatorID: string

        :return: nothing
        :rtype : none
        """

        op = self.findOperator(operatorID)
        if op is None:
            return 

        if op.isRinging():
            op.setStatus(operatorCall.BUSY, op.callID)
            print('Call ' + str(op.callID) +
                  ' answered by operator ' + str(op.ID))
    # do_answer()

    
    def do_reject(self, operatorID):
        """
        I deal with the reject command

        :param ID: reject identification
        :type  ID: int

        :return: nothing
        :rtype : none
        """
        
        op = self.findOperator(operatorID)
        if op is None:
            return 

        if op.isRinging():
            print('Call ' + str(op.callID) +
                  ' rejected by operator ' + str(op.ID))
            op.setStatus(operatorCall.AVAILABLE)
            self.deliverNextCall(op)
    # do_reject()
    
    def do_hangup(self, callID):
        """
        I Handle the hangup command

        :param callID: call identification
        :type  callID: int

        :return: nothing
        :rtype : none
        """
        print('Hangup : ' + str(callID))
    # do_hangup()
    
    def do_EOF(self, line):
        """
        I handle the end of file command

        :return: always returns true
        :rtype : boolean
        """
        return True
    # do_EOF()
# CallCenter()

if __name__ == '__main__':
    CallCenter().cmdloop()
