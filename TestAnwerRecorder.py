
answers = []

print("Input answers to the questions")
while True:
    answer = input(f"{len(answers) + 1}: ")
    if answer != "exit":
        answers.append(answer)
    else:
        break

with open("answers.txt", "w") as f:
    for index, i in enumerate(answers):
        f.write(f"{index}: {i}")
        f.write("\n")