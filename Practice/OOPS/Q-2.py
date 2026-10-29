#create student class that take name & marks of 3 subject 
#as arugemnet in constructor then create a method to print the avg

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avrg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("namaste",self.name,"your avg score is:",sum/3)

info=student("nikhil",[100,100,100])
info.avrg()
    