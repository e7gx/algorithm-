class Queue:
    def __init__(self):
        self.AbdullahAndHaassan = []#! create an empty list to store queue elements

#???! append  it's like push put in python it's append
    def enqueue(self, item):
        """Adds an element to the rear of the queue."""
        self.AbdullahAndHaassan.append(item)#! Adds an element to the queue

    def dequeue(self):
        """Removes and returns the element from the front of the queue."""
        if not self.is_empty():#! Check if the queue is empty
#!بمعنى انه اتحقق من ان الكيو فارغ ام يوجد داخله عناصر اذا كان يوجد داخله شيء هنا انا اقدر اسوي "pop"و احذف
#! اذا ماتحقق الشرط تقدر تحذف
            return self.AbdullahAndHaassan.pop(0)
        else:
            #!رسساله اذا كان الكيو فارغ 
            print("Queue is empty")
            return None

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.AbdullahAndHaassan) == 0
    #!len هنا يتحقق من 
    #! الخاص ب المصفوفه اذا كان يساوي صفر ف ارجع له الرسالة التي في الاعلى

    def peek(self):#!peek هذي خاصية في بايثون تساعدك تشوف اخر عنصر في المصفوفة ومن اسمها تاخذ نظره خاطفة 
        """Returns the element at the front of the queue without removing it."""
        #!السطر يسمح للمستخدم برؤية العنصر الأول في طابور الانتظار دون إزالته
        if not self.is_empty():#! يتاكد من المصفوفة ب اخذ نظره عليها    
            return self.AbdullahAndHaassan[0]
        else:
            print("Queue is empty")
            return None

    def size(self):#! يطبع حجم الطابور او المصفوفه التي ب اسم عبدالله و حسان
        """Returns the number of elements in the queue."""
        return len(self.AbdullahAndHaassan)


queue = Queue()

while True:
    print("\nQueue operations:")
    print("1. Enqueue❤️")
    print("2. Dequeue💔")
    print("3. Peek👀")
    print("4. Size🫙")
    print("5. Quit👋")

    choice = input("Enter your choice (1-5)1️⃣2️⃣3️⃣4️⃣5️⃣: ")

    if choice == '1':
        AbdullahAndHaassan = input("Enter the element to queue: ")
        queue.enqueue(AbdullahAndHaassan)
        print("Element queued successfully👍❤️")
    elif choice == '2':
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print("Dequeued item 😥😥:", dequeued_item)
    elif choice == '3':
        peeked_item = queue.peek()
        if peeked_item is not None:
            # Peek at the front element of the queue
            print("Peeked item🦴🦴:", peeked_item)

    elif choice == '4':
        #! Get the size of the queue
        print("Size of the queue 👍:", queue.size())

    elif choice == '5':
        print("Exiting the program❤️❤️❤️.")            # Exit the program

        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
