class human:
    def __init__(self,name,roll_no,age,branch):
        self.human=name
        self.roll_no=roll_no
        self.age=age
        self.branch=branch
    def Display(self):
        print("i am ",self.name,self.roll_no,self.age,self.branch)
   
h1=human("kavya","22d41a0510",21,"cse")
h2=human("priya",510,22,"cse")
h1.Display()
h2.Display()


