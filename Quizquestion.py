answer = input("What is the capital of France?")
answer = answer.title()

while answer != "Paris":
    answer = input("Sad, try again: ")
    answer = answer.title()
    print("Finally, took quite a while!")
