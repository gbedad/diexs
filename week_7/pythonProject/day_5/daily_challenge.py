# Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.


# def sort_sentence(*args):
#     args_list = [args for ]
#     args_list.sort()
#     return args_list

args = "without", "hello", "bag", "world"
list_args = list(args)
list_args.sort()
output = ",".join(list_args)
print(output)



for i in range(len(list_args)):
    for j in range(i + 1, len(list_args)):

        if list_args[i] > list_args[j]:
            list_args[i], list_args[j] = list_args[j], list_args[i]

print(list_args)
result = ",".join(sorted(item for item in list_args))
print(result)


# print(sort_sentence("without","hello","bag","world"))

