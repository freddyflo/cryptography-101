import caesarcipher




if __name__ == '__main__':
   
   message = 'Welcome Fred'
   print("Original message: {}".format(message))

   encrypted_message = caesarcipher.caesar_encrypt(message)
   print("Encrypted message: {}".format(encrypted_message))

   decrypted_message = caesarcipher.caesar_decrypt(encrypted_message)
   print("Decrypted message: {}".format(decrypted_message))
   
