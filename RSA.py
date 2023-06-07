from Crypto.Util.number import *
import math
# Hàm mã hóa
def encrypt(plaintext, e, n): 
    ciphertext = pow(plaintext, e, n)
    return ciphertext

# Hàm giải mã
def decrypt(ciphertext, d, n):
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Hàm tạo khóa
def create_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    # Chọn một số nguyên tố e . Do e-phi là coprime nên gcd của chúng sẽ là 1
    e = getPrime(32)
    # Nếu gcd khác 1 , tạo lại e
    while math.gcd(e, phi) != 1:
        e = getPrime(32)
    # Tạo d
    d = inverse(e, phi)
    return (e, d, n)

# Random p, q
p = getPrime(1024)
q = getPrime(1024)
(e, d, n) = create_key(p, q)
plaintext = "Chua te tach gacha"  # Chuỗi ký tự
# Chuyển đổi plaintext thành số nguyên
plaintext_int = int.from_bytes(plaintext.encode(), 'big')
# Mã hóa và giải mã plaintext
ciphertext = encrypt(plaintext_int, e, n)
decrypted_plaintext_int = decrypt(ciphertext, d, n)
# Chuyển đổi plaintext từ số nguyên thành chuỗi ký tự
decrypted_plaintext = decrypted_plaintext_int.to_bytes((decrypted_plaintext_int.bit_length() + 7) // 8, 'big').decode()
print("Plaintext:", plaintext)
# Không in Key trên 1 dòng vì nó quá dài nên khó nhìn
print("Public Key : ", e )
print (n)
print("Private Key : " , d)
print(n)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
