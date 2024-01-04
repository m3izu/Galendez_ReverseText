def reverskies():
    while True:
        user_input = input("Enter a string: ")

        if user_input.isalpha():
            reversed_text = user_input[::-1]
            print('Output: ', reversed_text)
            break
        else:
            print("Error Reported! Enter text only.")

reverskies()
