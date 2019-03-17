sentence=raw_input()
words=sentence.split(" ")
newword=[word[::-1] for word in words]
newSentence = " ".join(newword) 
print newSentence;
