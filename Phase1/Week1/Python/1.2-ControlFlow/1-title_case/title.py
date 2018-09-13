
# convert title into words
# subsequently, all words NOT in exceptions need to be in Correct Title Form

def titlecase(title, exceptions):
    title = title.split()
    word_list = []
    for word in range(len(title)):
        if title[word] not in exceptions:
           word_list.append(title[word].capitalize())
        else:
            word_list.append(title[word])
    return " ".join(word_list)

# def titlecase(title,exceptions):
    # for word in title:
        # if word in exceptions:
            #continue
        # else
            # word = word.title()
    # return title.join('')

    
if __name__ == "__main__":
    print (titlecase ("the quick brown fox jumps over the lazy dog", ["quick", "brown"]))


