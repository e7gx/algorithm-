class Stack:
    def __init__(self):
        self.AbdullahAndHassan = []

    def push(self, item):
        """Pushes an element onto the stack."""
        self.AbdullahAndHassan.append(item)

    def pop(self):
        """Pops an element from the top of the stack."""
        if not self.is_empty():
            return self.AbdullahAndHassan.pop()
        else:
            print("AbdullahAndHassan Stack is empty")
            return None

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.AbdullahAndHassan) == 0

    def peek(self):
        """Returns the top element of the stack without removing it."""
        if not self.is_empty():
            return self.AbdullahAndHassan[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.AbdullahAndHassan)


def create_stack():
    stack = Stack()
    num_elements = int(input("Enter the number of elements to push onto the stack: "))
    for i in range(num_elements):
        AbdullahAndHassan = input(f"Enter element {i+1}: ")
        stack.push(AbdullahAndHassan)
    return stack


stack = create_stack()

print('Stack after pushing elements:')
print(stack.AbdullahAndHassan)

while True:
    choice = input("\nDo you want to pop an element from the stack? (yes/no): ").lower()
    if choice == 'yes':
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped item:", popped_item)
            print("Stack after popping element:", stack.AbdullahAndHassan)
    elif choice == 'no':
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        print(stack.AbdullahAndHassan)
