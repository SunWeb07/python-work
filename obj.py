class employe:
    def __init__(self,name,id,salary,exp):
        self.name=name
        self.id=id
        self.salary=salary
        self.exp=exp
        
    def display(self):
        print(self.name,self.id,self.salary,self.exp)
    
    
        



e=employe("sandeep",21,20000,2)
e.display()
