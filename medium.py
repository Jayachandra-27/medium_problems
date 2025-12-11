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


r={}
# for k,v in l.items():
#     if v>=2:
#         r[k]=v

# k_list=list(r.keys())

# print(k_list)
# # if len(k_list)>=2:
# print(f'Second duplicate number is {k_list[1]} and it is occurred {r[k_list[1]]} times')


# ARRAY BASED QUESTIONS
# Write a function that rotates an array to the right by a
# given number of steps.


# def rotate(nums, k):
#         l2=nums[:]
#         s=k%len(nums)
#         newl=len(nums)-s
#         for i in range(newl-1,-1,-1):
#             nums[i+s]=l2[i]
#         for i in range(s):
#             nums[i]=l2[newl+i]
#         return nums
    
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(rotate(nums,k))

# Intersection of Two Arrays
# l1=[1, 2, 3]
# l2=[2, 3, 4]
# l=[]
# for i in l1:
#     if i in l2:
#         l.append(i)

# print(l)

# Find Missing Number
# l=[1, 2, 4, 5]
# m=max(l)
# for i in range(min(l),max(l)):
#     if i not in l:
#         print(i)
# else:
#     print(max(l)+1)

#Find the Maximum Product of Two Elements





# Write a function to find all pairs in an array whose 
# sum is equal to a given target.
# l=[2, 4, 3, 5, 7, 8, 9]
# t=7
# p=[]
# seen=set()
# for i in l:
#     s=t-i
#     if s in seen:
#         p.append([s,i])
#     seen.add(i)

# print(sorted(p))



# Find Peak Element

# Problem: Write a function to find a peak element in an array. 
# An element is a peak if it is not smaller than its neighbours.


# def p1(l):
#     for i in range(len(l)):
#         if i==0:
#             if l[i]>l[i+1]:
#                 return l[i]
#         if i>=1 and i<len(l)-1:
#             if l[i]>l[i+1] and l[i]>l[i-1]:
#                 return l[i]
#         if i==len(l)-1:
#             if l[i]>l[i-1]:
#                 return l[i]

# print(p1([1, 1, 2, 1, 1, 2]))


# Check for Anagrams
# s = "anagram"
# t = "nagaram"
# seen={}
# if len(s)!=len(t):
#     print(False)
# for i in s:
#     if i in seen:
#         seen[i]+=1
#     else:
#         seen[i]=1
# # print(seen)

# for i in t:
    
#     if i not in seen:
        
#         seen[i]-=1
# # print(seen)

# for val in seen.values():
#     if val!=0:
#         print(False)

# print(True)


# for i in range(1,3):
#     for j in range(1,3):
#         print(j,end=' ')
#     print( )


# arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# seen=set()
# r=set()

# for i in arr:
#     req=-i
#     if req in seen:
#         a=min(req,i)
#         b=max(req,i)
#         if (b,a) not in seen:
#             r.add((a,b))
#         # r.add((a,b))
#     seen.add(i)
# l=[]
# for i in r:
#     l.append(list(i))
# print(l)




# r={(-1, 1)}
# print(sorted(r))

# l=[(2,3),(4,6)]
# if (2,3) not in l:
#     l.append((2,3))
# print

# flatten array


r=[]
def flat(l):
    
    for i in l:
        if type(i)==int:
            r.append(i)
        else:
            flat(i)
k=flat([[1,1],2,[1,1]])
print(r)




