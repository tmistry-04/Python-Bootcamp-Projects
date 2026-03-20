name1 = input("Enter name1: ")
name2 = input("Enter name2: ")

def calculate_love_score(name1, name2):
    names = [name1.casefold(), name2.casefold()]
    true = ["t", "r", "u", "e"]
    love = ["l", "o", "v", "e"]
    words = [true, love]
    sum = 0
    score = ""
    for word in words:
        for name in names:
            for i in word:
                for j in range(len(name)):
                    if name[j] == i:
                        sum += 1;
        score += str(sum)
        sum = 0;
    print(score)

calculate_love_score(name1, name2)