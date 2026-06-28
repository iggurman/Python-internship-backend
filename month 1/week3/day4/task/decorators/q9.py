class Mydec():
    def __init__(self,func):
        self.func=func
        
    def __call__(self,*args,**kwargs):
        print("func started ")
        result=self.func(*args,*kwargs)
        print("func ended")
        return result
    
    
@Mydec
def greet(name):
    print("hello",name)
    
greet("gurman")