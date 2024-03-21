from Bird import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
class BSTree:

    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        


            
    def f0(self):
        return "HE182137"
    
    
    def f1(self, xType, xRate, xWing):
        if xType[0] != 'B' and xRate <= 10:
            new_bird = Bird(xType, xRate, xWing)
            if self.root is None:
                self.root = new_bird
            else:
                current = self.root
                while True:
                    if xRate < current.rate:
                        if current.left is None:
                            current.left = new_bird
                            break
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = new_bird
                            break
                        current = current.right
    
    def f2(self):
        self.preOrder2(self.root)
    
    def preOrder2(self,p):
        if p==None:
            return
        if p.data.wing <= 10 and p.data.wing >= 4:
            self.visit(p)
        self.preOrder2(p.left)
        self.preOrder2(p.right)
    
    def f3
    
    
    
    
    
    
    
    
    
    
    