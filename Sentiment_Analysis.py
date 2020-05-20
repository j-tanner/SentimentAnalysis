punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for letter in word:
        if letter in punctuation_chars:
            word = word.replace(letter, "")
    return word

def get_neg(sentence):
    negative_count = 0
    sentence = sentence.split()
    for word in sentence:
        word = strip_punctuation(word.lower())
        if word in negative_words:
            negative_count += 1
    return negative_count

def get_pos(sentence):
    positive_count = 0
    sentence = sentence.split()
    for word in sentence:
        word = strip_punctuation(word.lower())
        if word in positive_words:
            positive_count += 1
    return positive_count

fileconnection = open('project_twitter_data.csv', 'r')

outfile = open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

lines = fileconnection.readlines()

for line in lines[1:]:
    line = line.strip().split(',')
    positive_score = get_pos(line[0])
    negative_score = get_neg(line[0])
    net_score = int(positive_score) - int(negative_score)
    info = '{}, {}, {}, {}, {}'.format(line[1], line[2], positive_score, negative_score, net_score)
    outfile.write(info)
    outfile.write('\n')
