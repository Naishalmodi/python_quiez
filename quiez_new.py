Questions = [
    "(1) Who is the current president of India ?",
    "(2) TUF series laptop comes from which company ?",
    "(3) Who is the prime minister of India ?",
    "(4) What is the next number after 15 ?",
    "(5) Which is the largest country in the world ?"
]

Options = [
    ("A. Ram Nath Kovind", "B. Pranab Mukherjee", "C. Droupadi Murmu", "D. Pratibha Patil"),
    ("A. Asus", "B. Lenovo", "C. Dell", "D. HP"),
    ("A. Rishi Sunak", "B. Narendra Modi", "C. Joe Biden", "D. Justin Trudeau"),
    ("A. 14", "B. 15.5", "C. 16", "D. 14.6"),
    ("A. USA", "B. UK", "C. Russia", "D. China")
]

Answer = ("C", "A", "B", "C", "C")

guesses = []
Score = 0

for i in range(len(Questions)):
    print('----------------------------------------------------------------')
    print(Questions[i])
    for opt in Options[i]:
        print(opt)
    guss = input("Enter (A, B, C, D): ").upper()
    guesses.append(guss)
    if guss == Answer[i]:
        Score += 1
        print('Correct')
    else:
        print('Wrong')
        print(f"The correct answer is {Answer[i]}")

# Score
print("Answer: ", end="")
for ans in Answer:
    print(ans, end="")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

Score = int(Score/len(Questions) * 100)
print(f"Result: {Score}%")