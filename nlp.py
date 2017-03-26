#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

# Dependencies
import nltk
# Location of the corpus
nltk.data.path.append('./nltk_data')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def language_detector(text):
    """
    Input: text (string) which wants to know the language
    Output: language of the text

    It detects dannish, dutch, english, finnish, french, german,
    hungarian, italian, kazakh, norwegian, portuguese, russian,
    spanish, swedish and turkish.
    """

    # Split string in a list of tokens (words and punctuation)
    tokens = word_tokenize(text)
    # Put tokens in lowercase
    low_tokens = [token.lower() for token in tokens]
    # Set of unique tokens present in the text
    tokens_set = set(low_tokens)

    # Dictionary
    # keys: language
    # value: number of different stopwords present in the string
    score = {}

    for language in  stopwords.fileids(): # Iterate over the languages
        # Load stopwords for the language
        stops = set(stopwords.words(language))
        # Look for which stopwords appear in the text
        in_common = tokens_set.intersection(stops)
        # Store the number of stopwords present in the text into
        # the dictionary score
        score[language] = len(in_common)

    # Return language with more different stopwords present in the text
    return max(score, key=score.get)



if __name__ == '__main__':

    text = "A situação é bastante preocupante porque entre os principais clientes\
            brasileiros estão China e Hong Kong, que mantêm o veto à carne bovina\
            brasileira praticamente desde que a Operação Carne Fraca ganhou o \
            noticiário nacional e internacional. Do total da proteína bovina exportada\
            pelo Brasil, a China comprou no ano passado o equivalente a 25,7% e Hong Kong,\
            a 47,3%, conforme dados da Abiec."

    print(language_detector(text))


    text = "Even as the two spoke, some of Mr. Trumps advisers were privately \
            expressing frustration with Mr. Ryan, arguing that he had badly \
            misjudged the situation and misled the president into tackling \
            health care before a tax overhaul."

    print(language_detector(text))
