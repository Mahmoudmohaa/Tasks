from collections import Counter


english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def frequency_analysis(ciphertext):

    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))


    freq = Counter(ciphertext)


    sorted_freq = sorted(freq, key=freq.get, reverse=True)


    mapping = {}
    for i in range(len(sorted_freq)):
        if i < len(english_freq):
            mapping[sorted_freq[i]] = english_freq[i]
        else:
            mapping[sorted_freq[i]] = '?'  # Unknown for less frequent letters


    plaintext = ''
    for char in ciphertext:
        if char in mapping:
            plaintext += mapping[char]
        else:
            plaintext += char

    return plaintext, mapping



ciphertext = "YVCCF NFICU"
plaintext, mapping = frequency_analysis(ciphertext)

print("Ciphertext:", ciphertext)
print("Suggested Plaintext:", plaintext)
print("Mapping:", mapping)