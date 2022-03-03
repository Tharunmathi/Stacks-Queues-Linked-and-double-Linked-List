stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
stack.pop(-2)
print(stack)
stack = [20,40,60,80]
print(stack)
print(len(stack)==0)
print(not stack)
print(stack[-1])
stack = []
def push():
    ele= input("enter the element:")
    stack.append(ele)
    print(stack)
"""def pop():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed element",e)
        print(stack)
while True:
    print("select one option 1.push 2.pop 3.quit:")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("enter the valid option")"""

print("******")
"""stack = []
def push():
    if(len(stack) == a):
        print("stack is full!")
    else:
        elemen = input("enter the element:")
        stack.append(elemen)
        print(stack)
def pop():
    if(len(stack) == 0):
        print("we cannot pop because stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
a = int(input("limit of the stack:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("invalid operation selected")"""
import collections
stacka = collections.deque()
stacka.append(10)
stacka.append(30)
stacka.append(50)
print(stacka)
stacka.pop()
print(stacka)
print(not stacka)
print(stacka[-1])
import queue
stackb = queue.LifoQueue()
stackb.put(10)
stackb.put(30)
stackb.put(50)
stackb.put(70)
print(stackb)
stackb.get()
stackb.get()
print(stackb)
stackb = queue.LifoQueue(3)
stackb.put(10)
stackb.put(30)
stackb.put(50)
# QUEUE DATA STRUCTURE ////////////////////////////////////////////////////////////////////////////////////////////////
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print(queue.pop(0))
a = queue.pop(0)
b = queue.pop(0)
print(a)
print(b)
print(queue)
queue = []
queue.insert(0,20)
queue.insert(0,30)
queue.insert(0,40)
print(queue)
print(queue.pop())
print(queue.pop())
print( not queue)
print(queue[-1])
queue = []
def enqueue():
    e = input("enter the element :")
    print("element added is ",e)
    queue.append(e)
    print(queue)
def dequeue():
    if not queue :
        print("queue is empty")
    else:
        queue.pop()
        print(queue)
def display():
    print(queue)

"""while True:
    print("select the operations 1.add 2.pop 3.show 4.quit:")
    choice  = int(input())
    if choice ==1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("enter the valid operation")"""
# implementation of queue using classes
import collections as cs
q = cs.deque()
print(q)
q.append(40)
q.append(55)
q.append(98)
print(q)
q.popleft()
q.popleft()
q.popleft()
print(q)
q.appendleft(20)
q.appendleft(66)
q.appendleft(51)
print(q)
print(q.pop())
q.pop()
q.pop()
print(q)
print(not q)
q.append(44)
q.append(55)
q.append(66)
q.append(77)
print(q)
print(q[0])
print(q[-1])
import queue
q = queue.Queue()
q.put(99)
q.put(88)
q.put(77)
print(q)
q.get()
q.get()
q.get()
print(q)
# PRIORITY QUEUE /////////////////////////////////////////////////////
q = []
q.append(10)
q.append(30)
q.sort()
q.append(5)
q.sort()
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
q = []
q.append(44)
q.append(33)
q.sort(reverse = True)
q.append(88)
q.sort(reverse= True)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
import queue
q =queue.PriorityQueue()
q.put(20)
q.put(30)
q.put(55)
print(q)
q.get()
q.get()
q.get()
print(q)
q = []
q.append((1,"Tharun"))
q.append((2,"Tharun"))
q.append((3,"Tharun"))
q.sort(reverse = True)
print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print("************************************************Linked list starts here***************************************")
# LINKED LIST /////////////////////////////////////////////////////////////////////////////////////////////////////////
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def printllt(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                 print(n.data)
                 n = n.ref
    def add_begin(self,data):
        newnode = Node(data)
        newnode.ref = self.head
        self.head = newnode

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def after_node(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                 break
            else:
                n = n.ref
        if n is None:
            print("linked listis empty")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

            n = self.head
            while n is not None:
                print(n.data,"---->",end = " ")
                n = n.ref

    def before_node(self,data,x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head is not None:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n =self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node


    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")



ll1 = Linkedlist()
"""ll1.add_begin(20)
ll1.add_end(50)
ll1.add_begin(10)
ll1.after_node(30,20)
ll1.before_node(15,30)
#ll1.before_node(15,200)"""
ll1.insert_empty(10)
ll1.insert_empty(20)
ll1.printllt()
print("********************    Doubly linked list starts here  *********************")
# "DOUBLY LINKED LIST"//////////////////////////////////////////////////////////////////////////////////
class node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class doublyLL:
    def __init__(self):
        self.head = None
    def printLL(self):
        print("In forward direction:")
        if self.head is None:
            print("Doubly Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.nref
    def printLL_reverse(self):
        print()
        print("In reverse direction:")
        if self.head is None:
            print("Doubly reverse  Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                 n = n.nref
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")

    def add_begin(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                 n = n.nref
            n.nref = new_node
            new_node.pref = n
    def add_after(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.nref
            if n is None:
                print("Given node is not present in DlL")
            else:
                new_node = node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.nref
            if n is None:
                print("Given node is not present in DlL")
            else:
                new_node = node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node


dlls = doublyLL()
#dlls.insert_empty(10)
dlls.add_begin(4)
dlls.add_end(100)
dlls.add_after(10,4)
#dlls.add_after(100,10)
#dlls.add_after(100,10000)

dlls.printLL()
dlls.printLL_reverse()





