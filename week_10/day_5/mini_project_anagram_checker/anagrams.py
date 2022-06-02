import anagram_checker


def check_if_only_one_word(word):
    check_word = word.split(" ")
    if len(check_word) > 1:
        return False
    else:
        return True


def show_menu():
    ask_user = True
    while ask_user:
        print("""
        ANAGRAM CHECKER
    (a) Input a word
    (x) Exit
    """)
        user_choice = input("Enter an option: ")
        if user_choice == 'a':
            word_instance = anagram_checker.AnagramChecker()
            user_input = input("Enter a word: ")
            check = check_if_only_one_word(user_input)
            if check:
                user_input = user_input.strip()
                check_validity = word_instance.is_valid_word(user_input)
                if check_validity:
                    words = word_instance.get_anagrams(user_input)
                    anagram_string = " ".join(words)
                    print(f'YOUR WORD: "{user_input}"\nthis is a valid English word\nAnagrams for your word : {anagram_string}')
                else:
                    print(f'YOUR WORD: "{user_input}"\nthis is not a valid English word')
            else:
                print("Enter only one word.")

        elif user_choice == 'x':
            ask_user = False
        else:
            print("Wrong input")


show_menu()