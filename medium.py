# Write a program that takes a string, 
# string should be of even length. Divide the string into two 
# equals parts, check the number of vowels in both the parts of the 
# string. If both parts of string have same number of vowels then return
# true otherwise return false.
# s='mars'
# l=len(s)
# s1=s[0:l//2]
# s2=s[l//2:len(s)]

# v='aeiouAEIOU'
# c1=c2=0
# for i in s1:
#     if i in v:
#         c1+=1
# for i in s2:
#     if i in v:
#         c2+=1
# if c1==c2:
#     print(True)
# print(False)

# Write a program that takes array of numbers as input, 
# among the numbers in array, check how many numbers starts 
# with the same digit and ends with the same digits. 
# Print the count of such kind of numbers in the given array.

# l= [ 102, 56, 42, 11, 64, 10]
# c=0
# for i in l:
#     t=str(i)
#     if t[0]==t[-1]:
#         c+=1
# print(c)
    
# Write a program that takes array of numbers as input, 
# among the numbers in array, print the numbers which forms a 
# prime number by adding one to it. Print such numbers in the 
# given array separated b spaces.

# l= [ 7, 4, 7, 23, 10 ]
# l1=[]
# for i in l:
#     if i>1:
#         for j in range(2,i+1):
#             if (i+1)%j==0:
#                 break
#         else:
#             l1.append(i)
# print(l1)

# Write a program that takes array of numbers 
# as input and a number as second input. 
# Check the position of the factorial of the second 
# input number in the given array. Print the position of it. 
# If the factorial of given second input number is not presented
# in the array then print factorial of  
# the number is not presented.

# l= [61, 4, 6, 7, 120,10]
# t=5
# def fact(n):
#     if n==1  or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# if fact(t) in l:
#     print(l.index(fact(t)))
# else:
#     print('not possible')

# 
# Write a program that takes a number as input, 
# print the sum of duplicate numbers in the given number.

# n=234234
# s=str(n)
# l={}
# for i in s:
#     if i not in l:
#         l[i]=1
#     else:
#         l[i]+=1

# print(l)
# s=0
# for k,v in l.items():
#     if l[k]==2:
#         s+=int(k)
# print(s)

# Write a program that takes array of numbers are input,
# print the second duplicate number and it’s occurrence.
# a= [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# l={}
# for i in a:
#     if i not in l:
#         l[i]=1
#     else:
#         l[i]+=1


# r={}
# for k,v in l.items():
#     if v>=2:
#         r[k]=v

# k_list=list(r.keys())

# print(k_list)
# # if len(k_list)>=2:
# print(f'Second duplicate number is {k_list[1]} and it is occurred {r[k_list[1]]} times')

hello