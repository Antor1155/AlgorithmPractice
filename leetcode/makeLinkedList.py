class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeListNode(array, l = 0):
    if l == len(array):
        return 
    head = ListNode(array[l])
    head.next = makeListNode(array, l+1)
    return head
l1 = [2,4,9]
l2 = [5,6,4,9]
l1 = makeListNode(l1)
l2 = makeListNode(l2)

def addTwoNumbers(l1, l2):
    res_head = l1
    pre_of_l1 = None
    carry = 0
    while l1 and l2:
        val = l1.val + l2.val + carry
        carry = 0
        if val > 9:
            val = val - 10
            carry = 1
        l1.val = val

        pre_of_l1 = l1
        l1 = l1.next
        l2 = l2.next
    
    if not l2:
        while l1 and carry :
            val = l1.val + carry
            carry = 0
            if val > 9:
                val = val - 10
                carry = 1
            l1.val = val
            pre_of_l1 = l1
            l1 = l1.next

    elif not l1:
        pre_of_l1.next = l2

        while l2 and carry:
            val = l2.val + carry
            carry = 0
            if val > 10:
                carry = 1
                val = val -10
            l2.val = val
            pre_of_l1 = l2
            l2 = l2.next
    
    if carry:
        pre_of_l1.next = ListNode(1, None)
    
    return res_head

    

k = addTwoNumbers(l1, l2)
ans = []
while k:
    ans.append(k.val)
    k = k.next

print(ans)

           