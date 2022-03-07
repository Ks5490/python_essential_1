employees_str = input("What is the number of employees?: ")
employees_int = int(employees_str)

age_counter = 0 
for employee in range(employees_int):
    
    while True:
         first_name = input("What is the employees' first name?: ")
         if first_name.isalpha():
            break
    
    while True:
        last_name = input("What is the employees' last name?: ")
        if last_name.isalpha():
            break
    
    while True: 
        age_str = input("What is the employees' age?: ")
        if age_str.isdigit():
            age = int(age_str)
            if 18 <= age <= 100:
                age_counter += age
                break

    print(f"Employee {first_name} {last_name} is {age} years old")

if age_counter > 500:
    print(f"The total age of the employees is {age_counter}")
