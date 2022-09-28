
#1. Using a while loop, implement bubble sort algorithm


# Employees = {'SpongeBob Squarepants': 1200, 'Eugene Krabs': 50000, 
#              'Patrick':800, 'Sandy': 600, 'Squidward Tentacles':300}
             
Employee_list = ['SpongeBob Squarepants','Eugene Krabs', 
             'Patrick','Sandy Cheeks','Pearl Krabs',
              'Squidward Tentacles','Plankon']
#Employee_list = list((Employees.items()))

def bubble():
   length = len(Employee_list) -1
   sorted = False
   while not sorted:
        sorted = True
        for i in range(0,length):
            if Employee_list[i] > Employee_list[i + 1]:
                sorted = False
                Employee_list[i], Employee_list[i + 1] = Employee_list[i + 1], Employee_list[i]  
   return Employee_list

print(bubble())