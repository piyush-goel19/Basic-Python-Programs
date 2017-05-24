#Inheritence
class Parent():
    def __init__(self,first_nm,last_nm,blood_grp):
        print("Parent Constructor called")
        self.first_name = first_nm
        self.last_name = last_nm
        self.blood_grp = blood_grp

    def show_info(self):
       # print("Parents Information!!")
        print("First name: ",self.first_name)
        print("Last name: ",self.last_name)
        print("Blood group :",self.blood_grp)

class Child(Parent):
    def __init__(self,first_nm,last_nm,blood_grp,age):
        print("Child constructor called")
        self.age = age
        Parent.__init__(self,first_nm,last_nm,blood_grp)

 	def show_info(self):	
 		print("Childs Information !!")
        print("First name: ",self.first_name)
        print("Last name :",self.last_name)
        print("Blood group :",self.blood_grp)
        print("Age :",self.age)


#piyush_goel = Parent("Piyush","Goel","O+")
#piyush_goel.show_info()
ayush_goel = Child("Ayush","Goel","O-",17)
ayush_goel.show_info()
#print(piyush_goel.first_name + piyush_goel.last_name)
#print(piyush_goel.blood_grp)
