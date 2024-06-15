check if linked list is palindrome or not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow_ptr = self.head
        fast_ptr = self.head
        prev_of_slow_ptr = None
        
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            prev_of_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next
        
        # If the number of nodes is odd, skip the middle node
        if fast_ptr:
            slow_ptr = slow_ptr.next
        
        # Step 2: Reverse the second half of the linked list
        second_half = self.reverse_linked_list(slow_ptr)
        
        # Step 3: Compare first half with the reversed second half
        first_half = self.head
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def reverse_linked_list(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Example usage:
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(2)
    llist.append(1)

    print("Linked List:")
    llist.print_list()

    if llist.is_palindrome():
        print("Linked List is a palindrome")
    else:
        print("Linked List is not a palindrome")
