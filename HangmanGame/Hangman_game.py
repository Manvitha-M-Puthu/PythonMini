import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("Welcome to the hangman Game")
choosen_word= random.choice(hangman_words.word_list)
display=[]
end_of_game=False
lives=6

for i in range(len(choosen_word)):
        display.append("_")

while not end_of_game:
    guess=input("guess: ").lower()
    if guess in display:
          print("Already Tried")
          
    for i in range(len(choosen_word)):
        if guess==choosen_word[i]:
            display[i]=guess
    print(hangman_art.stages[lives])
    if guess not in choosen_word:
            lives-=1
            print("The guess is wrong, you loose a life.")
            if lives==0:
                print("You lost")
                print(f"The Word is {choosen_word}")
                end_of_game=True
                
    print(f"{' '.join(display)}")
    if "_" not in display:
            print("You Win")
            end_of_game=True
            
    
    