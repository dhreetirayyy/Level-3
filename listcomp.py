numbers = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in numbers if x%2==0]
print('list of even numbers from orignal:', even)
odd = [x for x in numbers if x%2!=0]
print('list of odd numbers from orignal:', odd)