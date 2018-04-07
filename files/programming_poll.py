filename = 'programming_poll.txt'
prompt = "Why do you like programming?"
prompt2 = "Do you wanna continue the quest? (Y or N)\n >"

while True:
    reason = input(prompt)
    with open(filename, 'a') as f:
        f.write(reason + "\n")
    wanna_cont = input(prompt2)
    if wanna_cont == 'N':
        break
    elif wanna_cont == "Y":
        continue
    else:
        print("Give valid input!!! Sigh!!!")
