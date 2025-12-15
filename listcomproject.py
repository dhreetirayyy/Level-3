num = int(input("Enter a number:"))
odd = [x for x in range(num) if x%2!=0]
oddlist = [1,3,5,7,9]
print(odd, oddlist)
flists = ['grape', 'jackfruit', 'lychee', 'apple','blueberry']
fcapatilazed =[flists.capitalize() for flists in flists]
print("Orignal Fruit Names", flists)
print("Capitalized Fruit Names",fcapatilazed)