Hello guys!!!...I am S.R Praneash shiva from KGiSL insitution of Engineering and technology(KiTE).This is a python code for calculating and displaying final grade of students.

print("------------GRADE CALCULATOR-------------")
print("90<=score<=100:Grade A\n80<=score<=90:Grade B\n70<=score<=80:Grade C\n60<=score<=70:Grade D\nscore<60:Grade F")
a=int(input("Enter your marks:"))
if(a>100):
    print("Please enter your proper mark!!!")
elif(a<=100 and a>=90):
    print("Congraulation!!! you got Grade A")
elif(a<90 and a>=80):
    print("Congralation!!! you got Grade B")
elif(a<80 and a>=70):
    print("Nice try!!! you got Grade C")
elif(a<70 and a>=60):
    print("Improve Hardwork!!! you got Grade D")
else:
    print("Study Hard!!! you got Grade F")
print("------------------------------------")
