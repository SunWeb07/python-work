class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 

    def language(self): 
        print("Hindi is the most widely spoken language of India.") 

    def type(self): 
        print("India is a developing country.") 

class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 

    def language(self): 
        print("English is the primary language of USA.") 

    def type(self): 
        print("USA is a developed country.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type()
    

class cricket():
    def ball(self):
        print("i'm smaller in size and bowler throws me and batsman hits me with bat")
class football(cricket):
    def ball(self):
        print("i'm bigger in size and players kicks me to the goals and goalkeeper save me everytime i come there")
        
ok=cricket()
ok.ball()
ok=football()
ok.ball()