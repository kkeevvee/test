#Create a function named odd_indices() that has one parameter named lst.
#The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

#Write your function here
def odd_indices(lst):
  newList=[]
  for i in range(0,len(lst)):
    print(i)
    if i%2 !=0:
      print("odd")
      newList.append(lst[i])
    else:
      print("even")
  return newList


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
