class queue:
    def __init__(self):
        self.que=[]
##        self.front=self.que[0]
##        self.rear=self.que[-1]
    def enqueue(self,data):
        self.que.append(data)
        self.front=self.que[0]
        self.rear=self.que[-1]        
    def dequeue(self):
        print('removed element : ',self.que.pop(0))
        if len(self.que)==0:
            print('Queue is now empty\n')
        else:
            self.front=self.que[0]
            self.rear=self.que[-1]
    def isFull(self):
        pass
    def isEmpty(self):
        if len(self.que)==0:
            print('Queue is empty\n')
        else:
            print('Queue is not empty\n')
    def display(self):
        print(self.que)
q=queue()
while True:
    key=int(input('You want to perform 1:enque 2:dequeue 3:isEmpty 4:display 0:quit: '))
    if key==1:
        data=eval(input('Enter the data you want to add in to queue : '))
        q.enqueue(data)
    elif key==2:
        q.dequeue()
    elif key==3:
        q.isEmpty()
    elif key==4:
        q.display()
    elif key==0:
        break
