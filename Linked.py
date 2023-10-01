class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
node1 = Node(10)

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def Print_LL(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"-->",end=" " )
                n=n.ref
    def add_begin(self,data):
        new_n = Node(data)
        new_n.ref = self.head
        self.head = new_n

    def add_end(self,data):
        new_n = Node(data)
        n=self.head
        if n is None:
            n = new_n
        else:
            while n.ref is not None:
                n=n.ref
            n.ref = new_n

    def delete_begin(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while (n.ref).ref is not None:
                n=n.ref
            n.ref = None

    def delete_any(self,data):
        if self.head is None:
            print("Empty")
        n=self.head
        if n.data == data:
                n = n.ref
        else:
            while n.ref.data != data:
                n=n.ref
            n.ref = n.ref.ref

l = LinkedList()
l.add_begin(100)
l.add_end(50)
l.add_begin(20)
l.add_end(30)
l.add_end(1)
# l.delete_begin()
# l.delete_end()
l.delete_any(20)
l.Print_LL()