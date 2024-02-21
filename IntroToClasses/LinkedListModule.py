class Node:
    def __init__(self, data:int, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None

    def append(self, data:int) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        # for a linked list that has contents, it needs to advance further until it gets to the end. 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        # keeps going until it reaches the end. 
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def helper(node:Node, target:int) -> Node:
    if node and node.data == target: 
        print(node.data)
        return node
    return helper(node.next, target)


def searchForNode(ll, target_val): 
    return helper(ll.head, target_val)

if __name__ == "__main__": 
    l0 = LinkedList()

    l0.append(1)
    l0.append(2)
    l0.append(3)

    l0.display()
    l0.append(4)
    l0.display()
    print(searchForNode(l0, 3).data)