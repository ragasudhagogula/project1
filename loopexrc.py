#1 Print First 10 natural numbers using while loop  
# using for loop
# for i in range(1,11):
#     print(i)

#2 Print the following pattern
# a=5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

#3 Calculate the sum of all numbers from 1 to a given number
# n=0
# s=int(input("enter the value "))
# for i in range(0,s+1,1):
#     n=n+i
# print("sum ",n)

#4 Write a program to print multiplication table of a given number
# n=0
# s=int(input("enter the value "))
# for i in range(1,11):
#     n=s*i
#     print("mul ",n)

#9 Display numbers from -10 to -1 using for loop
# for i in range(-10,0):
#     print(i)

#10 Use else block to display a message “Done” after successful execution of for loop
# for i in range(5):
#     print(i)
# else:
#     print("done")

#8 Print list in reverse order using a loop
# list1[10, 20, 30, 40, 50]
# for i in range(0,)

#7 Print the following pattern

# n=int(input("enter the number "))
# for i in range(0,n-1):
#     for j in range(i-1,0,-1):
#         print(j,end = "")
# print(" ")

#11 Write a program to display all prime numbers within a range

# start=int(input("enter the start number "))
# end=int(input("enter the end number "))
# for i in range(start,end+1):
#     mid=i//2
#     if i>1:
#         for j in range(2,mid+1):
#             if i%j==0:
#                 break
#             else:
#                 pass
#         else:
#             print(i)

#13 Find the factorial of a given number

# n=int(input("enter the number "))
# result=1
# for i in range(n,0,-1):
#     result=result*i
# print("factorial number ",result)

# n=int(input("enter the numer "))
# factorial=1
# for i in range(n,0,-1):
#     factorial=factorial*i
# print("factorial number ", factorial)

#14 Reverse a given integer number

# list3 = int(input("enter the number "))
# print(list3)
# num_string = str(list3)
# size = len(num_string)
# reversed_num = num_string[size::-1]
# string_num = int(reversed_num)
# print(string_num)

#15 Use a loop to display elements from a given list present at odd index positions

# a=int(input("enter the number "))
# for i in range()


n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,i-1):
        print(j,end = " ")
print( " " )
