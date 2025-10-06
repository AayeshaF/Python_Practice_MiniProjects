# secretWord = "Medicine"
# attempts = 4
#
# while attempts!=0:
#     guess = input("Enter the guess: ").capitalize()
#     if guess==secretWord:
#         print("You Won")
#         break
#     else:
#         attempts -= 1
#         if attempts>1:
#             print(f"Wrong Guess, {attempts} attempts left")
#         if attempts==1:
#             print("Wrong Guess, one attempt left")
#
# if attempts == 0:
#     print("No more chances left")

#the first try is above, below is a revised version

secretWord = "Medicine"
tries = 4
guess = input("Guess the secret word: ").capitalize()

while secretWord != guess:
    tries -= 1
    if tries>1:
        print(f"Wrong Guess, {tries} chances left")
    elif tries == 1:
        print(f"Wrong Guess, {tries} chance left")
    elif tries == 0:
        print(f"Wrong Guess, No More chances left")
        break
    guess = input("Guess the secret word: ").capitalize()
else:
    print("You Won")








