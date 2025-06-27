data=[]
# Stack operations
#general syntax
# element = list_name[index]

print("\n Stack")
data.append("34")
data.append("67")
print("Stack after push:", data)

#access element in index
stack = ['A', 'B', 'C'] 
#access top element(peek)
top = stack[-1]
print("Top of stack:", top)  
#access any element
print("First pushed element:", stack[0])   

# Queue operations
print("\n Queue")
data = []
data.append("65")
data.append("87")
print("Queue after enqueue:", data)


#access element in queue
queue = ['X', 'Y', 'Z']  # X is front, Z is rear
#access front element
front = queue[0]
print("Front of queue:", front)  # Output: X
#acess rear element
rear = queue[-1]
print("Rear of queue:", rear)  # Output: Z
# Acess any element by position
print("Second element in queue:", queue[1])  # Output: Y
