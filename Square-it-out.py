M = []
lower = int(input("Enter the lowest limit number:"))
upper = int(input("Enter the highest limit number:"))
for j in range(lower,upper):
  M.append(j**2)
print(M)
for i in M:
  if i%2 == 0:
    print("Even",i)
  else:
    print("Odd",i)