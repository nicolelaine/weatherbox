
words = ["angry", "furious", "annoyed", "agitated"];

def wordInput(feeling):
  if feeling in words:
    print("Wow, you are indeed", feeling)
  else:
    print(feeling, "is not a recognized feeling. Try again!")
wordInput("bonkers")
