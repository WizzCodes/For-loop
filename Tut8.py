#List = [["Ramesh", 25], ["Suresh", 30], ["Ganesh", 33], ["Rahul", 35]]
#dict1 = dict(List)

#for item, Marks in dict1.items():
   # print(item, "Marks in St-1", Marks)


List1 = (int, float, "suresh", 22, 14, 788, 142, 7, 22, 47, 68, 58, 22, 1458, 583)

for item in List1:
    if str(item).isnumeric() and item>10:

        print(item)