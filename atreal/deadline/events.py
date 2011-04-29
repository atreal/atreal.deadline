from atreal.deadline.interfaces import IDeadlineable


def storeDeadlineInWorkflowHistory(obj, event):
    """ """
    print "STORE DEADLINE IN WORKFLOW HISTORY"
    IDeadlineable(obj).storeDeadlineInWorkflowHistory()