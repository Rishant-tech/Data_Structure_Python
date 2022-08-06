class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        l=len(self.stack)
        if l==0:
            print("Stack is empty\n")
        else:
            print("The poped element : ",self.stack.pop())
        
    def isEmpty(self):
        l=len(self.stack)
        if l==0:
            print("Stack is empty\n")
        else:
            print('Stack is not empty\n')
    def display(self):
        print(self.stack)
s=stack()
while True:
    print("\nEnter 4 to print the stack")
    key=int(input('''You want to 1:add 2:pop 3:isempty, enter the operation number\n0: to exit : '''))
    if key==1:
        data=input("Enter the data to add into stack : ")
        s.push(data)
    elif key==2:
        s.pop()
    elif key==3:
        s.isEmpty()
    elif key==0:
        break
    elif key==4:
        s.display()
    else:
        print("invalid choice")
    
