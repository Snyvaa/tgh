class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def traversal(self):
        tem = self.head
        for i in range(self.length):
            tem = tem.next
    
    def search(self,value):
        tem = self.head
        for i in range(self.length):
            if tem.value == value:
                return print('Yes')
            tem = tem.next
        return print('No')
    
    def get(self,index):
        tem = self.head
        if self.length > index:
            for i in range(index):
                tem = tem.next
            print(tem.value)
            return tem
        else:
            return False
    
    def set_value(self,index, value):
        tem = self.get(index)
        tem.value = value
    
    def pop_first(self):
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
    
    def pop(self):
        pop = self.head
        while pop.next is not self.tail:
            pop = pop.next
        pop.next = None
        self.tail = pop

    def remove(self,index):
        pre = self.get(index-1)
        remove = pre.next
        pre.next = remove.next
        remove.next = None





linked_list = LinkedList()
linked_list.append(10)
linked_list.prepend(20)
linked_list.append(30)
linked_list.insert(2,40)
linked_list.traversal()
linked_list.get(2)
linked_list.search(30)
linked_list.insert(1,50)
print(linked_list)
linked_list.set_value(1,60)
print(linked_list)
linked_list.pop_first()
print(linked_list)
linked_list.pop()
print(linked_list)
linked_list.remove(2)
print(linked_list)

