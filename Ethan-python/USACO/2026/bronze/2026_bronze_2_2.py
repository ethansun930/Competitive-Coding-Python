T = int(input())
answers = []
for i in range(T):
    x = input()
    ans = 0
    while int(x) > 0:
        zeros_and_ones = True
        for i in range(len(x)):
            if int(x[i]) != 0 and int(x[i]) != 1:
                zeros_and_ones = False
        if zeros_and_ones == True:
            x = str(int(x) - 1)
        else:
            new_x = ""
            for i in range(len(x)):
                if (int(x[i]) % 2) == 0:
                    new_x = new_x + "0"
                else:
                    new_x = new_x + "1"
            x = str(int(new_x))
        ans += 1;
        ans %= 10**9 + 7
        # print(ans)
        # print(x)
    answers.append(ans)
for answer in answers:
    print(answer)