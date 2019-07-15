# put your code here.

def wordcount(filename):
    file_name = open(filename)
    word_count = {}
    for line in file_name:
       line_strip = line.rstrip()
       words = line_strip.split(' ')

       for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    for k, v in word_count.items():
        print(f'{k} {v}')
    return










wordcount("test.txt")