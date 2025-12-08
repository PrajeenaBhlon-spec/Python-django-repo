import array as arr

no_of_num = int(input("how many numbers? "))
number = arr.array('i' , [])
while no_of_num > 0:
  num = int(input("enter number "))
  number.append(num)
  no_of_num -= 1

print("order of numbers: ")
for i in range( 0 , len(number)):
  print(number[i] , end=" ")
  i += 1

print()

for i in range( 0 , len(number)):
  bubble = number[0]
  for j in range (0 , len(number)-1):
    if bubble < number[j+1]:
      bubble = number[j+1]
    elif bubble > number[j+1]:
      temp = number[j]
      number[j] = number[j+1]
      number[j+1] = temp
    j += 1
  i += 1

print("order of numbers after bubble sort :")
for i in range( 0 , len(number)):
  print(number[i] , end=" ")
  i += 1