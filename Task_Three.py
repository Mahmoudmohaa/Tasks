def prepare_text(text):

    text = ''.join(filter(str.isalpha, text.upper()))

    text = text.replace("J", "I")

    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
        i += 2

    if len(text) % 2 != 0:
        text += 'X'
    return text


def create_playfair_matrix(key):

    key = ''.join(filter(str.isalpha, key.upper()))
    key = key.replace("J", "I")
    key = ''.join(dict.fromkeys(key))


    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)


    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)


    playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return playfair_matrix


def find_position(matrix, char):

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    matrix = create_playfair_matrix(key)
    ciphertext = ''

    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:

            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:

            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:

            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ''

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:

            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:

            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:

            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext



key = "ORCHID"
plaintext = "HIKE THE FOOTHILLS"
ciphertext = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)