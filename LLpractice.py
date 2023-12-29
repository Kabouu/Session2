# linkedList practice
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
def insert(self, val):
    n = ListNode(val)
    n.next = self
    return n
def delete(self, val):
    s = ListNode("sentinel")
    s.next = self
    p = s
    c = self
    while c:
        if c.val == val:
            p.next = c.next
            return s.next
        p = c
        c = c.next
    return s.next     
def __len__(self):
    c = self
    l = 0
    while c:
        l += 1
        c = c.next
    return l

B = "Wazzah"
newNode = ListNode(B)
print(newNode.val)