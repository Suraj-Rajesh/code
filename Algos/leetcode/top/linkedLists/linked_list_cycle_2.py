#
# https://leetcode.com/problems/linked-list-cycle-ii/
#

def detect_cycle(head):
    slow = fast = head

    #
    # we need to check for both because,
    # 
    # fast itself can be None (head is None (or) fast was previously one node
    # earlier to tail and on doing, fast.next.next(fast.next will be tail in this
    # case) it became None
    #         (or)
    # fast.next is None
    # 
    # in both cases, fast.next.next will fail
    #
    # also, no need to check if head is None initially, since head is assigned
    # to fast and in while-condition below, if fast is None, condition fails
    # and we return None
    # 
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # found an entry point 
        if slow == fast:
            slow = head
            # loop over next nodes until we intersect
            while slow != head:
                slow = slow.next
                fast = fast.next
            return slow
    return None
