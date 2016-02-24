#
# IMPORTS
#

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

    def isRinging(self):
        """
        I check if the operator is ringing
        
        :param operator: the operators checked
        :type  operator: operatorCall.OperatorCall

        :return : True or False
        :rtype  : boolean
        """
        if self.status != RINGING:
            print('Operator ' + str(self.ID) + ' is not expecting a call')
            return False
        
        return True
    # isRinging
# Operator()
