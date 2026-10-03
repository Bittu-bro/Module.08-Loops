# range() - built-in function used to generate sequence of integers in a given interval 
# range (start, stop, step) stop is not included

#for i in range(start, stop, step):
    # statements


# for i in range(1,11,1):
#     print(i)
# for i in range(1,11,2): # odd number
#     print(i)

# #generate even number between 1 to 10  (10 excluded)
# for i in range(2,10,2):  # even number
#     print(i)

# # reverse order => 20 to 10(excluding 10)
# for i in range(20,10,-1):
#     print(i)

# #countdown from 10 to 1
# for i in range(10,0,-1):
#     print(i)
# print("Happy New Year")


# # range(start, stop) => step = 1 (by default)
# for i in range(1,5):   #step = 1
#     print(i) 

# # range(stop) => step = 1, start = 0 (by default)    
# for i in range(5):
#     print(i)


# groceries = ['salt', 'milk', 'sugar']
# # for item in groceries:
# #     print(item)

# for index in range(0, len(groceries),1):
#     print(index)


profits = [8,6,9,10]

# for index in profits:
#     print(index)



for index in range(len(profits)):
    q = index + 1
    #print(q,profits[index])
    print(f"Profit for Quarter {q} is {profits[index]}.")
