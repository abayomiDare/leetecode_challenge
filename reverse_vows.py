def reverse_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = list(s)

    reversed_vows = [vows for vows in string if vows in vowels][::-1]
    # print(extract_reverse_vows_from_string)
    vow_position: int = 0
    for count in range(len(string)):
        if string[count] in vowels:
            string[count] = reversed_vows[vow_position]
            vow_position += 1  # increment count; to track position to switch the vowel
        else:
            continue

    return "".join(string)
