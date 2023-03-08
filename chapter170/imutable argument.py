def yoda(prologue, sentence):   
    sentence.reverse()    
    prologue += " ".join(sentence)  
    return prologue
focused = ["You must", "stay focused"]
saying = "Yoda said: "
yoda_sentence = yoda(saying, focused)
print(focused)
print(saying)
print(yoda_sentence)