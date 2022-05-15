
class wish :
    def __init__(self,say) :
        self.say=say
    def greet(self):
        print("Hello",self.say)



class fruits( ) :
    def __init__(self, shape="sphere", color="red", taste="sour") :
        self.shape=shape
        self.color=color
        self.taste=taste
    
    def display(self):
        print(self.shape,self.color,self.taste)
        
        
        
        
berry=fruits()
berry.display()
berry=fruits("sphere","blue","sour")
berry.display()
wel=wish("Good Morning")
wel.greet()