

class sample:

        def display(self,x,y):
            self.x=x
            self.y=y
            print("X:",self.x)
            print("Y:",self.y)
            



class sample1(sample):
    
        def show(self,x,y,z):
            super().display(x,y)
            self.z=z
            print(self.x+self.y+self.z)
    
            
        

s=sample1()
s.show(10,12,10)




            

            
            
            

            
            
            
