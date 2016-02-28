#
# IMPORTS
#
import operatorCall

#
# CONSTANTS AND DEFINITIONS
#

#
# CODE
#
class CallCenter():
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
        self.operatorsThread = {}
        self.waitingQueue = []
        
        # Create some operators
        
        self.createCallOperator('A')
        self.createCallOperator('B')
    # __init__()

    def createCallOperator(self, opID):
        """
        Create the operator and start a Thread for it.

        The thread will be responsible for the timeout
        """
        operator = operatorCall.OperatorCall(opID)
        self.operators[opID] = operator
        opThread = operatorCall.OperatorThread(operator)
        opThread.start()
        self.operatorsThread[opID] = opThread
    
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

    def deliverCall(self, callID=-1):
        """
        I delivery the next call in the waiting queue to an operator
      
        :param callID: call identification
        :type  callID: int

        :return : True if delivered, False otherwise
        :rtype  : boolean
        """

        # get the next call from the waiting queue
        if callID == -1:
            waitingID = self.nextCallID()
            # There is no waiting call
            if waitingID == -1:
                return True
            else:
                callID = waitingID

        # search for an available operator sorted by IDs
        for op in sorted(self.operators.values(),
                         key=lambda operator: operator.ID):
            if not op.hasCall():
                 op.setStatus(operatorCall.RINGING, callID)
                 print('Call ' + str(callID) +
                       ' ringing for operator '+ op.ID)
                 self.operatorsThread[op.ID].startTimeout()
                 return True

        return False
    # deliveryCall()

    def showStatus(self):
        print('=======================')
        print('Number of Operators: ' + str(self.operators.__len__()))
        for op in self.operators.values():
            print('Operator: ' + op.ID + 
                  '; Status: ' + op.getStatus() +
                  '; Call : ' + str(op.callID))
        print('=============')
        print('Number of Waiting Calls: ' + str(self.waitingQueue.__len__()))
        for callID in self.waitingQueue:
            print('Call: ' + str(callID))
        print('=============')
    # showStatus()

    def createCall(self, callID):
        """
        If there is an operator available the call is passed to him, 
        otherwise the call is placed in the waiting queue

        :param callID: call identification
        :type  callID: int

        :return: nothing
        :rtype : none
        """
        print('Call ' + str(callID) + ' received')
        delivered = self.deliverCall(callID)
        
        # put the call in the waiting queue
        if not delivered:
            self.waitingQueue.append(callID)
            print('Call ' + str(callID) + ' waiting in queue')
    # createCall()

    def answerCall(self, operatorID):
        """
        Find the operator and make him answer a call
        
        :param operatorID: operator identification
        :type  operatorID: string

        :return: nothing
        :rtype : none
        """
        op = self.findOperator(operatorID)
        if op is None:
            return 

        if op.hasCall():
            op.answer()
    # answerCall()

    def rejectCall(self, operatorID):
        """
        Find the operator and make him answer a call
        
        :param operatorID: operator identification
        :type  operatorID: string

        :return: nothing
        :rtype : none
        """
        op = self.findOperator(operatorID)
        if op is None:
            return
        
        if op.hasCall():
            callID = op.callID
            # append the call id in the first position
            self.waitingQueue = [callID] + self.waitingQueue
            op.reject()
            self.deliverCall()
    # rejectCall()

    def hangupCall(self, callID):
        """
        Get the call and ends it
 
        :param callID: call identification
        :type  callID: int
        """

        # Call is with an operator
        for op in self.operators.values():
            if op.callID == callID:
                if op.status == operatorCall.RINGING:
                    print('Call ' + callID + ' missed')
                    op.setStatus(operatorCall.AVAILABLE)
                else:
                    op.hangup()
                
                self.deliverCall()
                return
            
        # Call is the waiting queue
        if self.waitingQueue.__len__() > 0:
            self.waitingQueue.remove(callID)
            print('Call ' + callID + ' missed')
    # hangoutCall()


    def stopProgram(self):
        """
        Stop all the threads in self.operatorsThread
        """
        for opThread in self.operatorsThread.values():
            opThread.stopThread()
    # stopProgram()
# CallCenter()
