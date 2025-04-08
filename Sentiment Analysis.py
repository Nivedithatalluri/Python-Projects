def check_elements_in_sentence(sentence,array):
    sentence_words = sentence.lower().split()
    

    for word in array:
        if word.lower() in sentence_words:
            return True
    return False
    
sentence = input("Enter a sentence: ")
positive = ["happy", "excited", "good", "fine", "successful", "completed", "finished", "accepted"]
negative = ["sad", "cry", "bad", "went wrong", "disappointed", "rejected"]
neutral = ["nothing much", "same", "as usual", "common"]
combined_array = positive + negative + neutral

if check_elements_in_sentence(sentence, positive):
    print("You are happy.")
elif check_elements_in_sentence(sentence, negative):
    print("You are Sad. Identify the reasons for your sad mood and work on them to become happy")
else:
    print("Your mood is neutral")

