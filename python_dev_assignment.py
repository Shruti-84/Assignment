# Morse code mapping
morse_keys = [
    "._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..",
    ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.",
    "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."
]

letters = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

# Take input from user
encrypted = input("Enter encrypted Morse string: ")

results = []

# Function to calculate length 
def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Function to check match 
def match_string(text, pattern, index):
    i = 0
    while i < get_length(pattern):
        if index + i >= get_length(text):
            return False
        if text[index + i] != pattern[i]:
            return False
        i += 1
    return True

# Recursive decoding
def decode(index, current):
    if index == get_length(encrypted):
        results.append(current)
        return

    i = 0
    while i < 26:
        morse = morse_keys[i]
        letter = letters[i]

        if match_string(encrypted, morse, index):
            decode(index + get_length(morse), current + letter)
        i += 1

# Start decoding
decode(0, "")

#  sort in alphabetical order 
n = get_length(results)
i = 0
while i < n:
    j = 0
    while j < n - 1:
        if results[j] > results[j + 1]:
            temp = results[j]
            results[j] = results[j + 1]
            results[j + 1] = temp
        j += 1
    i += 1

# Print output
print("\nPossible Decodings:\n")
i = 0
while i < n:
    print(results[i])
    i += 1
