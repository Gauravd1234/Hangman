import random

f = open("words.txt", "r")
contents = f.read()
contents = contents.split("\n")
f.close()


while True:
    word_index = random.randint(0, (len(contents) - 1))
    word = contents[word_index]
    if len(word) < 4:
        continue
    else:
        break
    
    
#print(word)   
word_spaces = ["_ "] * len(word)
guesses = len(word) + 5
word_tracker = []
def print_spaces():
    print("\n")
    for x in range(len(word)):
        print(end=word_spaces[x])


print("If you think you know what the word is, type 'guess'")        
while True:
    if guesses < 1:
        print("Word: ", word)
        print("\n")
        print("You lose!")
        break
    
    if "_ " not in word_spaces:
        print("Word: ", word)
        print("\n")
        print("You win!")
        break
    
    
    print_spaces()
    print("\n")
    print("Words guessed: ", word_tracker)
    print("Guesses left: ", guesses)
    char_guess = input("Enter a letter: ")
    

    if char_guess.lower() in word_tracker:
        print("\n")
        print("You have already guessed that letter")
        continue
    if char_guess.lower() == "guess":
        final_guess = input("Enter your guess: ")
        if final_guess == word:
            print("Word: ", word)
            print("\n")
            print("You win!")
            break
            print("Word: ", word)
            print("\n")
            print("You lose!")
            break
    
    if len(char_guess) > 1:
        print("\n")
        print("Invalid guess")
        continue
            
            
    
    word_tracker.append(char_guess)
    
    
    
    if char_guess.lower() in word:
        count = 0
        while count < len(word):
            if word[count] == char_guess.lower():            
                word_spaces[count] = char_guess.lower()
            count += 1
    else:
        print("->",'"{}"'.format(char_guess.upper()), "is not in the word")
        
    guesses -= 1
        
        
   


        

    
