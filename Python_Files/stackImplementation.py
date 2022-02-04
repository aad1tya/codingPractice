class StackNode():

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack():
    def __init__(self):
        self.end = None
        self.begin = None

    def push(self, data):
        node = StackNode(data)
        if self.end == None:
            self.begin = node
            self.end = node
            return
        temp = self.end
        self.end = node
        temp.next = node
        return
    
    def remove(self):
        if self.end == None:
            print("Nothing to remove")
            return
        temp = self.begin
        if temp.next == None:
            self.begin = None
            self.end == None
            return temp.data
        while True:
            prev = temp
            temp = temp.next
            if temp.next == None:
                break
        prev.next = None
        self.end = prev
        return temp.data
    
    def printData(self):
        if self.begin == None:
            print("The stack is empty!")
            return
        temp = self.begin
        if temp.next == None:
            print(temp.data)
            return
        while True:
            print(temp.data)
            temp = temp.next
            if temp.next == None:
                print(temp.data)
                break
##Example
new_stack = Stack()
new_stack.push("Hello")
new_stack.push(10)
new_stack.push(True)
new_stack.printData()
new_stack.remove()
new_stack.remove()
new_stack.remove()
new_stack.printData()
