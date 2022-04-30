# Caesar cypher
str_alphabet = "abcdefghijklmnopqrstuvwxyz"
text_to_cypher = input("Enter the text to cypher/de-cypher: ")
shift = int(input("Enter the offset:(+ for right shift, - for left shift "))
text_info = {
    "text": text_to_cypher,
    "shift": shift
}
print()
print("1- Encrypt a message")
print("1- Decrypt a message")
print("3- quit")
print()
user_input = input("What is your choice? (1-2-3) ")
cypher_text = ""

for letter in text_info["text"]:
    if user_input == "1":
        index = ord(letter) + text_info["shift"]  # cipher the text
    elif user_input == "2":
        index = ord(letter) - text_info["shift"]  # decipher the text
    else:
        print("Bye Caesar!")
        break
    if 44 <= ord(letter) <= 46 or ord(letter) == 32:  # maintain space and punctuation
        index = ord(letter)
    print("index", ord(letter), index)
    print("Before", chr(ord(letter)))
    if index > 122 or 90 < index < 97:
        if text_info["shift"] < 0:
            if user_input == "1":
                index += 26
            elif user_input == "2":
                index -= 26
        elif text_info["shift"] > 0:
            if user_input == "1":
                index -= 26
            elif user_input == "2":
                index += 26
    elif 47 <= index < 65:
        index += 26
    elif 65 <= index <= 90 and ord(letter) > 90:
        index += 26
    elif index > 90 and ord(letter) <= 90:
        index -= 26
    cypher_text += chr(index)
    print("After", chr(index), index)

print(f"Message : {cypher_text}")
# word_coded = ""
# for letter in word_to_code:
#     pos = str_alphabet.index(letter)
#     new_pos = pos + shift
#     if new_pos >= 26:
#         new_pos = new_pos % 26
#     off_letter = str_alphabet[new_pos]
#     word_coded += off_letter
# print(f"The coded version of {word_to_code} is {word_coded}")

