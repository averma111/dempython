from cryptography.fernet import Fernet

key=Fernet.generate_key();

##print(key);

cipher_suite=Fernet(key)

encrypted_text=cipher_suite.encrypt(b'This is key ');

decrypted_text=cipher_suite.decrypt(encrypted_text);

print(encrypted_text);

print(decrypted_text);
