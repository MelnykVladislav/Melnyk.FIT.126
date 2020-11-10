import os

book = "Секрети і брехня. Безпека даних в цифровому світі.txt"
text = "secrety.txt"
filename = book
os.chdir("Lab542.txt")

def with_spaces():

    file = open(filename, 'r')

    data = file.read()
    total_amount = len(data)

    file.close()

    return total_amount



def with_spaces():

    num_chars = 0

    with open(filename, 'r') as f:
        for line in f:
            for letter in line:
                for i in letter:
                    if(i != ' ' and i != '\n'):
                        num_chars += 1

    return num_chars

def with_spaces():
    num_words = 0
    words_set = set()

    one_time_words = set()
    words_array = []

    with open(filename, 'r') as f:
        for line in f:

            words = line.split()
            num_words += len(words)

            for word in words:
                words_set.add(word)
                words_array.append(word)

    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            one_time_words.add(words_array[i])

    print(f'Кількість слів {len(words_set)}')
    print(f'Кількість унікальних слів {len(one_time_words)}')

    return num_words

print(f'З пробілами {with_spaces()}')
print(f'Без пробілів {with_spaces()}')
print(f'Загальна кількість слів в тексті {with_spaces()}')