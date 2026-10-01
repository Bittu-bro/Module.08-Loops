# s1 = "Hello world"
# for char in s1:
#     print(char)
# print("End of the loop")    

employee = {'empid':1001, 'name':"John",'department':"HR"}
# for i in employee:
#     print(i)
#     print(i,employee[i])

print(employee.items())
for i in employee.items():
    #print(i)
    #print(i[0])
    print(i[1])