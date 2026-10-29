#create student class that take name & marks of 3 subject 
#as arugemnet in constructor then create a method to print the avg
class student:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
    def avrage(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hii",self.name,"your avg score is",sum/3)

info=student("Nikhil",[98,99,97])
info.avrage()

    