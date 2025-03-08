import itertools


def brute_force_monoalphabetic(ciphertext):

    standard_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for permutation in itertools.permutations(standard_alphabet):

        mapping = {standard: cipher for standard, cipher in zip(standard_alphabet, permutation)}


        plaintext = ''
        for char in ciphertext:
            if char in mapping:
                plaintext += mapping[char]
            else:
                plaintext += char

        print(f"Attempt with key {''.join(permutation)}: {plaintext}")



ciphertext = "JLAP FJHERFJL OFE"
brute_force_monoalphabetic(ciphertext)