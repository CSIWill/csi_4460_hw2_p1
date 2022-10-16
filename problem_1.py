import time
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

file_in = open("my_file.txt", "rb")
plaintext = file_in.read()
# DES
start_des = time.time()
key_des = get_random_bytes(8)
iv_des = get_random_bytes(8)
cipher_des = DES.new(key_des, DES.MODE_CBC, iv_des)
ciphertext_des = cipher_des.encrypt(pad(plaintext,8))
end_des = time.time()
print("Encryption execution time is ", (end_des-start_des), "s")
start_des1 = time.time()
cipher_des1 = DES.new(key_des, DES.MODE_CBC, iv_des)
plaintext_des = unpad(cipher_des1.decrypt(ciphertext_des),8)
end_des1 = time.time()
assert(plaintext == plaintext_des)
print("Decryption execution time is ", (end_des1-start_des1), "s")
# AES
start_aes = time.time()
key_aes = get_random_bytes(16)
iv_aes = get_random_bytes(16)
cipher_aes = AES.new(key_aes, AES.MODE_CBC, iv_aes)
ciphertext_aes = cipher_aes.encrypt(pad(plaintext, 16))
end_aes = time.time()
print("Encryption execution time is ", (end_aes-start_aes), "s")
start_aes1 = time.time()
cipher_aes1 = AES.new(key_aes, AES.MODE_CBC, iv_aes)
plaintext_aes = unpad(cipher_aes1.decrypt(ciphertext_aes), 16)
end_aes1 = time.time()
assert(plaintext == plaintext_aes)
print("Decryption execution time is ", (end_aes1-start_aes1), "s")