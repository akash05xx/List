#Creating a list
my_list =[]
print(my_list)
my_list2 =[]
print(my_list2)

#Adding elements into lists
my_list =['akash','python','AI','ML']
print(my_list)
my_list2 =list([8451092817,'1','2'])
print(my_list2)

#List indexing
my_list =['p','y','t','h','o','n']
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])

#List Slicing
my_list =['p','y','t','h','o','n']
print(my_list[0:])    #['p', 'y', 't', 'h', 'o', 'n']
print(my_list[0:1])   #['p']
print(my_list[0:2])   #['p', 'y']
print(my_list[:-1])   #['p', 'y', 't', 'h', 'o']
print(my_list[::5])   #['p', 'n']
print(my_list[0:])    #['p', 'y', 't', 'h', 'o', 'n']
print(my_list[:-4])   #['p', 'y']

#Mistaken values
odd =[2,4,6,8,10]
odd[0]= 1
print(odd)   #[1, 4, 6, 8, 10]

odd[1:4] = [3,5,7]
print(odd)         #[1, 3, 5, 7, 10]

#Appending and extending list in python
odd =[1,3,5,7]
odd.append(9)
print(odd)     #[1, 3, 5, 7, 9]

odd.extend([9,11,13,])
print(odd)            #[1, 3, 5, 7, 9, 9, 11, 13]

#Concatenating & repeating lists
odd =[1,3,5,7]
print(odd+[9,11,13]) #[1, 3, 5, 7, 9, 11, 13]
print(["re"]*6)      #['re', 're', 're', 're', 're', 're']



