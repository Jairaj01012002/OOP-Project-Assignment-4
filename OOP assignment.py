class Delivery:
    """Initialize a dictionary containing list of employees available as well as 
    initialize a stack of id that will tell us which executive was assigned latest. First 2 executive are
    assigned by default as number of executive has to be more than one"""
    def __init__(self):
        self.executiveid={}
        self.executiveid[1]=1
        self.executiveid[2]=1
        self.order=[]
        self.order.append([1,0])
        self.order.append([2,0])
    def add_task(self):
        if(len(self.order)==1):
            for i in range(1,11):
                if(i not in self.executiveid):
                    self.order.append([i,1])
                    print("executive",i,"hired")
                    print("executive",i,"was assigned a task")
                    self.executiveid[i]=1
                    break
        elif(len(self.order)==0):
            for i in range(1,11):
                if(i not in self.executiveid):
                    self.order.append([i,1])
                    print("executive",i,"hired")
                    print("executive",i,"was assigned a task")
                    self.executiveid[i]=1
                    break
            for i in range(1,11):
                if(i not in self.executiveid):
                    self.order.append([i,0])
                    print("executive",i,"hired")
                    print("executive",i,"was assigned a task")
                    self.executiveid[i]=1
                    break
        else:
            chk=0
            for i in range(len(self.order)-1,-1,-1):
                if(self.order[i][1]<10):
                    self.order[i][1]+=1
                    print("executive",self.order[i][0],"was assigned a task")
                    chk=1
                    break
            if(len(self.order)>=10 and chk==0):
                print("ALL EXECUTIVE ARE BUSY")
            elif(chk==0 and len(self.order)<10):
                for i in range(1,11):
                    if(i not in self.executiveid):
                        self.order.append([i,1])
                        print("executive",i,"hired")
                        print("executive",i,"was assigned a task")
                        self.executiveid[i]=1
                        break
        for i in range(len(self.order)):
            print("executive",self.order[i][0],"has",self.order[i][1],"tasks")
    def complete_task(self,id1):
        chk=0
        for i in range(len(self.order)):
            if(self.order[i][0]==id1):
                self.order[i][1]-=1
                chk=1
                if(self.order[i][1]<=0):
                    print("executive",self.order[i][0],"completed a task")
                    print("executive",self.order[i][0],"released")
                    del self.executiveid[self.order[i][0]]
                    self.order.pop(i)
                else:
                    print("executive",self.order[i][0],"completed a task")
                break
        if(chk==0):
            print("EXECUTIVE DOES NOT EXIST")
        for i in range(len(self.order)):
            print("executive",self.order[i][0],"has",self.order[i][1],"tasks")
exe=Delivery()
"""For taking input type add_task to add a task
   Type complete_task and then id of the executive
   to complete task for that id"""
while(True):
    q=input()
    if(q=="add_task"):
        exe.add_task()
    elif(q=="complete_task"):
        q2=int(input())
        exe.complete_task(q2)
    else:
        break

        



















                

        



