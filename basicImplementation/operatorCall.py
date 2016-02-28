#
# IMPORTS
#
import threading
import time
#
# CONSTANTS AND DEFINITIONS
#
AVAILABLE = 0
RINGING   = 1
BUSY      = 2
#
# CODE
#
class OperatorCall():
    """
    
    """
    def __init__(self, ID):
        """
        I initialize an Operator
        
        :param ID: Operator's id
        :type  ID: char

        :return: nothing
        :rtype : none
        """
        self.ID = ID
        self.status = AVAILABLE
        self.callID = -1
    # __init__()
    
    def setStatus(self, newStatus, callID=-1):
        """
        I change the status of an Operator
        
        :param newStatus: the new status for the Operator
        :type  newStatus: int

        :return: nothing
        :rtype : none
        """
        self.status = newStatus
        self.callID = callID
    # setStatus()

    def getStatus(self):
        """
        I return the status from a Operator in a more readble way

        :return : status
        :rtype  : string
        """
        
        if self.status == AVAILABLE:
            return 'Available'
        elif self.status == BUSY:
            return 'Busy'
        elif self.status == RINGING:
            return 'Ringing'
    # getStatus()

    def hasCall(self):
        """
        I check if the operator is ringing
        
        :param operator: the operators checked
        :type  operator: operatorCall.OperatorCall

        :return : True or False
        :rtype  : boolean
        """
        if self.callID == -1:
            #print('Operator ' + str(self.ID) + ' is not expecting a call')
            return False
        
        return True
    # isRinging
    
    def answer(self):
        """
        I answer a Call

        :return: nothing
        :rtype : none
        """
        if self.hasCall() and self.status == RINGING:
            self.setStatus(BUSY, self.callID)
            print('Call ' + str(self.callID) +
                  ' answered by operator ' + str(self.ID))
    # answer()

    def reject(self):
        """
        I reject a Call

        :return: nothing
        :rtype : none
        """
        if self.hasCall() and self.status == RINGING:
            print('Call ' + str(self.callID) +
                  ' rejected by operator ' + str(self.ID))
            self.setStatus(AVAILABLE)
    # reject()

    def hangup(self):
        """
        I hangout a Call

        :return: nothing
        :rtype : none
        """
        if self.hasCall() and self.status == BUSY:
            print('Call ' + str(self.callID) +
                  ' finished and operator ' + str(self.ID) + ' available')
            self.setStatus(AVAILABLE)
    # hangout()

    def ignore(self):
        """
        I ignore a call
        
        :return: nothing
        :rtype : none    
        """
        if self.hasCall() and self.status == RINGING:
            print('Call ' + str(self.callID) +
                  ' finished and operator ' + str(self.ID) + ' available')
            self.setStatus(AVAILABLE)
    # ignore()
# OperatorCall()


class OperatorThread(threading.Thread):
    def __init__(self, operator):
        """
        I Initialize the class Operator Thread
        
        :param operator: Operator that the thread will control
        :type  operator: operatorCall.OperatorCall
        """
        threading.Thread.__init__(self)
        self.operator = operator
        self.timeout  = -1
        self.runThread = True
    # __init__()
        
    def run(self):
        """
        I will constantly check if the operator changed his status to
        ringing. Once he do i will start a timeout for this status
        """
        while self.runThread:
            if self.operator.status == RINGING and self.timeout != -1:
                time.sleep(self.timeout)    
                if self.operator.status == RINGING:
                    print('Call ' + str(self.operator.callID) +
                          ' ignored by operator ' + str(self.operator.ID))
                    self.operator.setStatus(AVAILABLE)
                    self.timeout = -1
    # run()

    def startTimeout(self):
        """
        Start the timeout count down
        """
        self.timeout = 10
    # startTimeout()

    def stopThread(self):
        """
        Change the flag 'runThread' to false, making the thread stop
        """
        self.runThread = False
        self.timeout = -1
    # stopThread()    
# OperatorThread
