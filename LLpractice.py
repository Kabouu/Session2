# linkedList practice
class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None
def insert(self, val):
    n = Node(val)
    n.next = self
    return n
def delete(self, val):
    s = Node("sentinel")
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

# merge two sorted linked lists
# what type of list, singular, doubly, circular?
# return linkedlist
# this case singular linkedlist, integer values
# validation of input type:
#   always integer
#   Will one or both of the LL be empty

# could make one array, add the two list's values, sort it
# then make linked list
# values = []
# def addShtuff(third: Node):
#     if third == None:
#         return
#     values.append(third.val)
#     addShtuff(third.next)
# def merger(self,first: Node, second: Node):
#     addShtuff(first)
#     addShtuff(second)
#     values.sort()
#     head = Node()
#     for x in values:
#         head.next = x
#     return head
