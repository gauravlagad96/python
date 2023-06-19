# How To Encode And Decode A Message using Python?
'''
Encryption is the process of converting a normal message (plain text) into a meaningless message (Ciphertext).
Whereas,
Decryption is the process of converting a meaningless message (Cipher text) into its original form (Plain text).


'''


def encodeMsg(message, key):
    def encoder(message, key):
        encoded_message = ""
        for char in message:
            encoded_message += chr(ord(char) + key)
        return encoded_message

    return encoder(message, key)


def decodeMsg(encoded_message, key):
    def decoder(encoded_message, key):
        decoded_message = ""
        for char in encoded_message:
            decoded_message += chr(ord(char) - key)
        return decoded_message

    return decoder(encoded_message, key)


# Example usage
message = "Hello, world!"
key = 3

encoded_message = encodeMsg(message, key)
print("Encoded message:", encoded_message)

decoded_message = decodeMsg(encoded_message, key)
print("Decoded message:", decoded_message)
