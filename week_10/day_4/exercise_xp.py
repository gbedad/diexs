import json
import random


# Exercise 1


def get_words_from_file(file_content):
    with open(file_content, mode='r') as f:
        lines = f.readlines()
    return lines


def get_random_sentence(length):
    get_words_list = get_words_from_file("words_list.txt")
    words = []
    for i in range(0, length):
        word = random.choice(get_words_list)
        words.append(word.lower().strip("\n"))
    sentence = " ".join(words)
    return sentence


def main():
    print("""
   RANDOM SENTENCE
   ---------------
   This program will ask you to input the number of words in the sentence.
   It will select this number of words randomly into a list
   and display this magic sentence""")
    ask = True
    while ask:
        user_input = input("How long should be the sentence (2 - 20)? ")
        if not isinstance(int(user_input), int) or int(user_input) < 2 or int(user_input) > 20:
            print("Invalid input")
            break
        else:

            sentence_length = int(user_input)
            print(get_random_sentence(sentence_length))
            ask = False


main()

print(get_random_sentence(6))

get_words_from_file('words_list.txt')

# Exercise 2
sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}
print(sampleJson["company"]["employee"]["payable"]["salary"])
sampleJson["company"]["employee"]["birth_date"] = "1999-05-12"
print(sampleJson)
json_employee = "employee.json"

with open(json_employee, 'w') as file_to_json:
    json.dump(sampleJson, file_to_json)
