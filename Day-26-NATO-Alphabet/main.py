import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dic)

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_version = [phonetic_dic[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_version)


generate_phonetic()
