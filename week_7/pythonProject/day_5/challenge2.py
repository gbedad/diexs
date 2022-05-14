# Exercise 1
# Draw the following pattern using for loops:
#   *
#  ***
# *****

print("\nExample 1")
for i in range(1, 6):
    if i % 2 != 0:
        print(' '*(int((5-i)/2)) + '*'*i)

print("\nExample 2")

for i in range(1, 6):
    print('-'*(5-i)+'*'*i)

print("\nExample 3")

for i in range(1, 6):
    print('*'*i)
for i in range(5, 0, -1):
    print(' '*(5-i) + '*' * i)

# Exercise 2
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): # Loop in my_list
    minimum = i # assign index to minimum. in first loop minimum = 0
    for j in range( i + 1, len(my_list)): # loop starting from index i + 1. First loop j = 1
        if(my_list[j] < my_list[minimum]): # Compare the next item to minimum and set it to the new minimum
            minimum = j
            if(minimum != i): # if the new minimum is not previous minimum, set it
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
