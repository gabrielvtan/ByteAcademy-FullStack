def remove_duplicate(string):
    non_repeat = []
    repeat = []
    for letter in string:
        if len(non_repeat) == 0:
            non_repeat.append(letter)
        
        elif len(non_repeat) > 0:
            if non_repeat[-1] != letter:
                non_repeat.append(letter)
            else:
                repeat.append(letter)

    return ("".join(non_repeat), "".join(repeat))

if __name__ == "__main__":
    print(remove_duplicate("balloons"))
    print(remove_duplicate("aabbccddeded"))
    print(remove_duplicate("flabby aapples"))
