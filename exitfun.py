age = [32,9,12,67]
for age in age: 
    if age < 18:
        print(age,"not allowed")
        exit()
    else: 
        print(age,"allowed")