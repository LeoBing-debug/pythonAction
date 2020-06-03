#方法入口     
def stringInput():
        name=input()
        print(name)
        
def intAdd(a,b):
       c=a+b
       d=a-b
       return c,d
        
if __name__ == '__main__':
    x,y=intAdd(5,3)
    print (x,y)