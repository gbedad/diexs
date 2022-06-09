import itertools


class AnagramChecker:
    def __init__(self):
        with open('words.txt', 'r') as f:
            self.lines = f.readlines() # define it twice, remove it and replace
            self.lines = [line.strip("\n") for line in self.lines]

    def is_valid_word(self, word):
        if word.upper() in self.lines:
            return True # replace with return word.upper() in self.lines
        else:
            return False

    # def get_anagrams(self, word):
    #     anagrams = []
    #     letters = list(word)
    #     a = list(itertools.permutations(letters))
    #     for item in a:
    #         ana = "".join(item)
    #         if ana.upper() in self.lines:
    #             anagrams.append(ana)
    #     unique_anagrams = list(set(anagrams))
    #     unique_anagrams.remove(word)
    #
    #     return unique_anagrams

    @staticmethod
    def is_anagram(word1, word2):
        if sorted(list(word1)) == sorted(list(word2)):
            print(sorted(list(word1)) == sorted(list(word2)))
            return True # the same here make it one line
        else:
            return False

    def get_anagrams(self, word):
        word = word.upper()
        anagrams = []
        first_filtered_list = list(filter(lambda x: len(x) == len(word), self.lines))
        for item in first_filtered_list:
            if self.is_anagram(word, item):
                anagrams.append(item.lower())
        anagrams.remove(word.lower())
        return anagrams


# word1 = AnagramChecker()

# print(word1.is_valid_word('Genome'))

# print(word1.get_anagrams("meat"))

