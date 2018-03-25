class aTree():
    def __init__(self,rootObj):
        self.key= rootObj
        self.leftchild = None
        self.rightchild = None
        return 

    def insert_left(self, newNode):
        if self.leftchild == None:
            self.leftchild = aTree(newNode)
        else:
            temp = aTree(newNode)
            temp.leftchild = self.leftchild
            self.leftchild = temp

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_rightchild(self):
        return self.rightchild
    
    def get_leftchild(self):
        return self.leftchild
    
    def get_root(self):
        return self.key

    def set_root(self, valueObj):
        self.key = valueObj

    def isEmpty(self):
        return self.get_root() == []

    def preOrderTraversal(self):
        if not self.isEmpty():
            print(self.get_root())
            if not self.get_leftchild() == None:
                self.get_leftchild().preOrderTraversal()
            if not self.get_rightchild() == None:
                self.get_rightchild().preOrderTraversal()
        return 

    def postOrderTraversal(self):
        if not self.isEmpty():
            if not self.get_leftchild()== None:
                self.get_leftchild(postOrderTraversal)
            if not self.get_rightchild() == None:
                self.get_rightchild().postOrderTraversal()
            print(self.get_root())
        return

a = aTree(1)
a.insert_left(2)
a.insert_left(3)
a.set_root(5)
a.preOrderTraversal()

