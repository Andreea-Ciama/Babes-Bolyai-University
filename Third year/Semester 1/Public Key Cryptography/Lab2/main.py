import numpy as np

# Substitution dictionary for mapping letters to numbers
substitution = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Inverse substitution dictionary for mapping numbers to letters
inverse_substitution = {value: key for key, value in substitution.items()}

def is_invertible(matrix):

    # Calculate the determinant for a 2x2 matrix
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Check if the determinant is non-zero
    return determinant
def gcd(a, b):
    #calculate gcd between 2 numbers
    while b:
        a, b = b, a % b
    return a

def encrypt(plain_text, key_matrix):

    # Convert the plain text to uppercase
    plain_text = plain_text.upper()

    # Remove any spaces from the plain text
    plain_text = plain_text.replace(" ", "")

    # Pad the plain text if its length is not a multiple of the key matrix size
    if len(plain_text) % len(key_matrix) != 0:
        padding_length = len(key_matrix) - (len(plain_text) % len(key_matrix))
        plain_text += 'X' * padding_length

    # Initialize the cipher text
    cipher_text = ''

    # Encrypt the plain text
    for i in range(0, len(plain_text), len(key_matrix)):
        # Get the current block of the plain text
        block = plain_text[i:i + len(key_matrix)]

        # Convert the block to a column vector of numbers
        block_vector = np.array([substitution[ch] for ch in block])

        # Multiply the key matrix with the block vector
        encrypted_vector = np.dot(key_matrix, block_vector) % 26

        # Convert the encrypted vector back to a string
        encrypted_block = ''.join([inverse_substitution[num] for num in encrypted_vector])

        # Append the encrypted block to the cipher text
        cipher_text += encrypted_block

    return cipher_text

# Example usage
plain_text = 'HELLO'
key_matrix = [
    [2, 2],
    [2, 13]
]
result=0
determinant = is_invertible(key_matrix)
if determinant !=0:
    result=gcd(determinant,26)
if result==1:
    key_matrix = np.array(key_matrix)
    cipher_text = encrypt(plain_text, key_matrix)
    print("Cipher Text:", cipher_text)
else:
    print("The matrix does not satisfy the conditions")

#problema 3 la lab 3
#probelam 2 lab 4