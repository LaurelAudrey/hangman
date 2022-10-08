import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []
guessed_letters = []

print(f'Pssst, the solution is {chosen_word}.')
print(logo)

for _ in range(word_length):
  display += "_"

while not end_of_game:
  print(f"\n{' '.join(display)}")
  print(stages[lives])

  print(guessed_letters)
  
  guess = input("\nGuess a letter: ").lower()

  if guess in guessed_letters:
      print(f"\nYou already guessed '{guess}'. Try again.")
      continue
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        guessed_letters += guess

  if "_" not in display:
    end_of_game = True
    print(f"\n{' '.join(display)}")
    print("\nYou win!")
    break

  if guess not in chosen_word:
    if guess in guessed_letters:
      print(f"\nYou already guessed '{guess}'. Try again")
    else:
      print(f"\n'{guess}' not in secret word.")
    guessed_letters += guess
    lives -= 1
    if lives == 0:
      print("\nHangman! You lose..")
      print(f"\nThe secret word was: {chosen_word}")
      break