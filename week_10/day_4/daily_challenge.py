# Text analysis
from collections import Counter


class Text:
    def __init__(self, text):
        self.text = text
        list_text = self.text.split()
        self.freq = Counter(list_text)

    def word_frequency(self, word):
        if word in self.freq.keys():
            return self.freq[word]
        else:
            return None

    def most_common_word(self):
        fin_max = max(self.freq, key=self.freq.get)
        print("Most common word:", fin_max)
        return fin_max

    def unique_words(self):
        uniques = []
        for k, v in self.freq.items():
            if v == 1:
                uniques.append(k)
        print(uniques)
        return uniques

    @classmethod
    def from_file(cls, text):
        with open(text, mode='r') as f:
            lines = f.readlines()
            lines_without_new_line = [line.strip("\n") for line in lines]
            return cls(' '.join(lines_without_new_line))


t = Text("A good book would sometimes cost as much as a good house.")
print(t.word_frequency("good"))

t.most_common_word()
t.unique_words()
the_stranger = Text.from_file('the_stranger.txt')
print(the_stranger.word_frequency('blazing'))

the_stranger.most_common_word()
the_stranger.unique_words()





