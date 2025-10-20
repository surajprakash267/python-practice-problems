# B. Reverse each word of a sentence
# --------------------------------------------------


sentence = "India is my country"
rev_sentence = " ".join(x[::-1] for x in sentence.split())
print(" Reverse each word:", rev_sentence)