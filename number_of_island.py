class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self,head):
        self.head = head
    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not self.head:
            return False
        
        walk = self.head
        run = self.head.next
        while walk != run :
            if run is None or run.next is None:
                return False

            walk = walk.next
            run = run.next.next
        return True
new_obj = Solution([1,2])
if(new_obj.hasCycle):
    print(True)
else:
    print(False)