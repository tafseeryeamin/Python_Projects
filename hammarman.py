import random

# Game setup
word_list = ["tiger", "lion", "camel","horse"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed_letters = []
attempts_left = len(chosen_word)  # New attempts system

#print(f"Debug: The word is {chosen_word}")  # Remove this line later
print(f"You get {attempts_left} attempts (one for each letter)!")

while "_" in display and attempts_left > 0:
    print("\nCurrent progress:", " ".join(display))
    print(f"Attempts remaining: {attempts_left}")

    guess = input("Guess a letter: ").lower().strip()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in guessed_letters:
        print(f"You already tried '{guess}'!")
        continue

    guessed_letters.append(guess)

    # Check for correct guess
    letter_found = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            letter_found = True

    # Handle attempts reduction
    if not letter_found:
        attempts_left -= 1
        print(f"❌ '{guess}' not in word. Attempts left: {attempts_left}")
    else:
        print(f"✅ Correct! '{guess}' is in the word!")

# Final outcome
if "_" not in display:
    print(f"\n🎉 You won! The word was: {chosen_word}")
else:
    print(f"\n💀 Game over! The word was: {chosen_word}")