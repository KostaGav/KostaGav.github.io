import codecs, nltk, string
from nltk.corpus import stopwords
import csv

from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("german")

dataset = codecs.open("presse/fdp/fdp.tsv", "r", "utf-8").read().strip().split("\n")

from nltk.stem.wordnet import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

exclude = set(string.punctuation)
stop_word_list = stopwords.words('german')

# input should be a string
def nlp_pipeline(text):
    # if you want you can split in sentences - i'm usually skipping this step
    # text = nltk.sent_tokenize(text)

    # tokenize words for each sentence
    text = nltk.word_tokenize(text)

    # pos tagger
    text = nltk.pos_tag(text)

    # lemmatizer
    text = [
        wordnet_lemmatizer.lemmatize(token.lower(), "v") if "V" in pos else wordnet_lemmatizer.lemmatize(token.lower())
        for token, pos in text]

    # remove punctuation and numbers
    text = [token for token in text if token not in exclude and token.isalpha()]

    # remove stopwords - be careful with this step
    text = " ".join([token for token in text if token not in stop_word_list])

    return text


corpus = []

output = codecs.open("presse/fdp/fdp_final.tsv","w","utf-8")

# be careful with this, the dataset is huge!
for line in dataset:
    #print line
    article = line.split("\t")[3]

    text = nlp_pipeline(article)

    text = text.replace("\t", " ")
    #print text

    output.write(line + "\t" + text + "\n")

output.close()