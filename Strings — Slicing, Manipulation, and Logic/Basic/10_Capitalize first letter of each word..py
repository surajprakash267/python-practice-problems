x = input("Enter the sentence: ")
cap_word = " ".join(ch.capitalize() for ch in x.split())
print(cap_word)