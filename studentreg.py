name=input("Enter your Name:")
roll=input("Enter your roll no:")
math=int(input("Enter maths marks:"))
phy=int(input("Enter physics marks:"))
chem=int(input("Enter chemistry marks:"))
py=int(input("Enter python marks:"))

print("****************STUDENT MARKSHEET******************")
print("Name",name,sep=":")
print("Roll_No",roll,sep=":")
total=float(math+phy+chem+py)
print(total)
avg=float(total/4)
print(avg)
