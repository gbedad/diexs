# Text analysis
from collections import Counter
import re


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


class TextModification(Text):

    def remove_punctuation(self):
        pattern = r'[^\w\s]'
        new_text = re.sub(pattern, '', self.text)
        # print(new_text)
        return new_text

    def remove_stop_words(self):
        stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
        text_list = self.text.split()
        # print(text_list)
        filtered_text = [word for word in text_list if word.lower() not in stop_words]

        print("Text without stop words: ", " ".join(filtered_text))
        return filtered_text






# t = Text("A good book would sometimes cost as much as a good house.")
# print(t.word_frequency("good"))
#
# t.most_common_word()
# t.unique_words()
# the_stranger = Text.from_file('the_stranger.txt').text
# print(the_stranger)
#
# the_stranger.most_common_word()
# the_stranger.unique_words()

the_stranger1 = TextModification.from_file('the_stranger.txt')
# the_stranger1.remove_punctuation()
# the_stranger1.remove_punctuation()
# print(the_stranger1.text)
the_stranger1.remove_stop_words()





