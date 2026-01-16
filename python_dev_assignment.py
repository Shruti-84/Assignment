morse_dict = {
    "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E",
    ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J",
    "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O",
    ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T",
    ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
    "__..": "Z"
}
encrypted = input("Enter encrypted Morse string: ")
results = []
def get_length(text):
    count = 0
    for _ in text:
        count = count + 1
    return count
def match_morse(text, morse, index):
    i = 0
    while i < get_length(morse):
        if index + i >= get_length(text):
            return False
        if text[index + i] != morse[i]:
            return False
        i = i + 1
    return True
def decode(index, current_word):
    if index == get_length(encrypted):
        results.append(current_word)
        return
    for morse in morse_dict:
        if match_morse(encrypted, morse, index):
            decode(index + get_length(morse), current_word + morse_dict[morse])
decode(0, "")
n = get_length(results)
i = 0
while i < n:
    j = 0
    while j < n - 1:
        if results[j] > results[j + 1]:
            temp = results[j]
            results[j] = results[j + 1]
            results[j + 1] = temp
        j = j + 1
    i = i + 1
print("All Possible Decodings:\n")
i = 0
while i < n:
    print(results[i])
    i = i + 1
