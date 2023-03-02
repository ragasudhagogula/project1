# a = "sudha"
# if a[0]=="z":
#     print("sudha")
# else:
#     print("welcome")

# n=2
# if n%2!=0:
#     print("wierd")
# else:
#     print("not wierd")

# If n is even and in the inclusive range of 2 to 5 , print Not Weird

# n=5
# if ((n % 2)== 0) & ((n >= 2) & (n<= 5)): 
#     print("not wierd")
# else:
#     print("wierd")

# n=0
# if n%2==0 and n>=2 and n<=5:
#     print("not weird")
# else:
#     print("weird")

# If n is even and in the inclusive range of 6 to 20, print Weird

# n=21
# if ((n % 2)== 0) and ((n >= 6) and (n<= 20)): 
#     print("wierd")
# else:
#     print("not wierd")

# n=26
# if n%2==0:
#     print("not weird")
# elif n%2==0 and n>20:
#     print("not weird")
# else:
#     print("wierd")

# a=4
# b=3
# print (a//b, a/b)

# n=3
# if n%2==0:
#     print("wierd")
# else:
#     print("not wierd")

# n=4
# if n%2==0:
#     print("not wierd")
# elif n%2==0 and n<=2 and n>=5:
#     print("not wierd")
# else:
#     print("wierd")

# n=16
# if n%2==0:
#     print("wierd")
# elif n%2==0 and n<=6 and n>=20:
#     print("wierd")
# else:
#     print("not wierd")

# n=22
# if n%2==0:
#     print("not wierd")
# elif n%2==0 and n<20:
#     print("not wierd")
# else:
#     print("wierd")

# a=25
# if a%7==0:
#     print("a is divisible")
# else:
#     print("not divisible")

# a=int(16)
# if a%5==0:
#     print("Hello")
# else:
#     print("Bye")


# n=19
# if n%2 !=0:
#     print("wierd")
# elif n%2==0 and n<=2 and n>=5:
#     print("not wierd")
# elif n%2==0 and n<=6 and n>=20:
#     print("wierd")
# elif n%2==0 and n<20:
#     print("not wierd")
# else:
#     print("wierd")

# # 100 units no charge
# next 100 units 5 per unit
# after 200 units 10 per unit

# n=350
# result=0
# if n<=100:
#     result=0
#     print("110")
# if n>100 and n<200:
#     result=(n-100)*5
#     print("112")
# if n>200:
#     result=500+(n-200)*10
# print("amount to pay", result)

# height=float(input("please let me know your height "))
# print(height)



3# Take two int values from user and print greatest among them.

# a=int(input(""))
# b=int(input(""))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("both are equal")
 
2# Take values of length and breadth of a rectangle from user and check if it is square or not.

# a=int(input("length "))
# b=int(input("breadth "))
# if a==b:
#     print("yes, it is a square")
# else:
#     print("no, it is not a square")

6#Take input of age of 3 people by user and determine oldest and youngest among them.

# a=int(input("age "))
# b=int(input("age "))
# c=int(input("age "))
# if a>b:
#     print("youngest")
# elif b>c:
#     print("oldest")
# elif c>a:
#     print("oldest")
# else:
#     print("equal age")

4#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity

# Suppose, one unit will cost 100.
# Judge and print total cost for user.

# n=int(input("quantity "))
# if n*100:

5# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# marks=int(input("marks "))
# if marks<=25:
#     print("F grade")
# elif marks>=25 and marks<=45:
#     print("E grade")
# elif marks>=45 and marks<=50:
#     print("D grade")
# elif marks>=50 and marks<=60:
#     print("C grade")
# elif marks>=60 and marks<=80:
#     print("B grade")
# else:
#     print("A grade")

# 8#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam

# a=int(input("number of classes held "))
# b=int(input("number of classes attended "))
# # percentage=(y/x)*100
# if percentage>=75:
#     print("student is allowed to sit in exam")
# else:
#     print("student is not allowed to sit in exam")


1# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

# salary=int(input("what is your salary "))
# service=int(input("what is your service "))
# bonus=salary*5/100
# if service>=5:
#     print("your bonus is ", bonus)
# else:
#     print("no bonus")
 
#  4#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# # Judge and print total cost for user.   

# quantity=int(input("what is quantity "))
# discount_10 = (10*quantity)/ 100
# if quantity>1000:
#     print("Total amount after discount", (quantity*100) - discount_10)
# else:
#     print("Total amount", (quantity*100))


# # one unit=100 
# discount=quantity>=1000*10/100
# if quantity>=1000*10/100:
#     print("discount for total quantity ", quantity)
# else:
#     print("no discount")


# # a=6**2
# # print(a)


# # for i in range (-10):
# #     print(i)


# # list="sudha"
# # for s in range (0,len(list)):
# #     print(list[s])

# # list3="skumdahma"
# # # [0,1,2,3,4,5,6,7,8]
# # for s in range(0,len(list3),2):
# #     print(s,list3[s])

# # list4="sarmajvnanns"
# # [0,1,2,3,4,5,6,7,8,9,10,11]
# # for a in range(0,len(list4),2):
# #     print(a,list4[a])

# # list2="pqalvmajn"
# # for p in range(0,len(list2),2):
# #     print(p,list2[p])

# list6="hwrertmwea"
# list5=[]
# for i in range(len(list6)-1,0,-1):
#     list5.append(list6[i])
# print(list5)

# # print first 10 naturals number using for loop:

# for i range(0,10):
#     print(i)

# for loop exercises:
#2
# list1=[1,2,3,4,5,6,7]
# for i in range(0,len(list1),2):
#     print(list1[i])

#9 for i in range(-10,0):
    # print(i)

# # #10
# for i in range(0,5):
#     print(i)
else:
    print("done!")

#14
# list3=str(76542)
# list1=[]
# for a in range(-1,len(list3),1):
#     list1.append(list3[a])
# print(str(list1))

# #14
# ist3 = 76542
# print(list3)
# num_string = str(list3)
# size = len(num_string)
# reversed_num = num_string[size::-1]
# string_num = int(reversed_num)
# print(string_num)

#3
# n=0
# s=int(input("enter the number "))
# for i in range(0,s+1,1):
#     n=n+i
# print("sum ",n)

#4
# n=0
# s=int(input("enter the number "))
# for i in range(1,11):
#     n=s*i
#     print("mul ",n)

#2 (mul meth)
# n=5
# for i in range(0,n+1):
#     if i==0:
#         print(i)
#     else:
#         print(i*2)

#2
n=10
for d in range(1,n+1):
    for e in range(1,d+1):
        print(e,end="")
    print("")

# reverse pattern
# n=10
# for a in range(0,n+1):
#     for b in range(a-1,0,-1):
#         print(b,end = "")
#     print(" ")

# num=[12, 75, 150, 180, 145, 525, 50]
# for i in num:
#     if i%5==0:
#         print("divisible",i)
#     if i>150:
#         print("next",i)
#     if i>500:
#         print("stop",i)

# var="James Bond"
# print(var[2:: -1])

# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)

# for i in range(10,15,1):
#     print(i, end="")

# x=36/4*(3+2)*4+2
# print(x)

# for num in range (-2,-5,-1):
    # print(num, end=", ")

# a=5
# for i in range(0,a+1):
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()

#8 Print list in reverse order using a loop

#9 Display numbers from -10 to -1 using for loop
# for a in range(-10,0):
#     print(a)

