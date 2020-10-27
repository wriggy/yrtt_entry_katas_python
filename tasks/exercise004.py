# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
# move first letter of each word to end of word and add "ay" leaving punctuation unchanged
    words = text.split()
    new_words = []
    for word in words :
        if word.isalpha() : 
            new_word = word[1:] + word[0] + "ay"
        else : 
            # separate out all non alphabet chars at start and end of word
            # eg ()!? etc. Punctuation within word left unchanged
            # if no alpha chars found 'word' is left unchanged
            start_punct = ""
            end_punct = ""
            while (word != '') and (not word[0].isalpha()):
                start_punct = "".join([start_punct, word[0]])
                word = word[1:]
            while (word != '') and (not word[-1].isalpha()):
                end_punct = "".join([word[-1], end_punct])
                word = word[:-1]
            # add back in removed punctuation
            if word == '' : new_word = start_punct + end_punct
            else: new_word = start_punct + word[1:] + word[0] + "ay" + end_punct
        new_words.append(new_word)
    return " ".join(new_words)
    