import math
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

try:
    with open('pubkey1.pem', 'r') as f:
        key1_pem = f.read() 
    with open('pubkey2.pem', 'r') as f:
        key2_pem = f.read()
    
    key1 = RSA.import_key(key1_pem)
    key2 = RSA.import_key(key2_pem)

except ImportError:
    print("Error: Library pycryptodome belum terinstal.")
    print("Silakan instal dengan: pip install pycryptodome")
    exit()
except FileNotFoundError as e:
    print(f"Error: File tidak ditemukan: {e.filename}")
    exit()

n1 = key1.n
e1 = key1.e
n2 = key2.n
e2 = key2.e

print(f"🔑 Kunci 1 (n1): {str(n1)[:80]}...")
print(f"🔑 Kunci 2 (n2): {str(n2)[:80]}...")

print("\nMencari GCD(n1, n2)...")
p = math.gcd(n1, n2)

if p == 1:
    print("Serangan gagal: Tidak ada faktor persekutuan antara n1 dan n2.")
    exit()

print(f"✅ Faktor persekutuan ditemukan (p): {str(p)[:80]}...")

q1 = n1 // p
phi1 = (p - 1) * (q1 - 1)
d1 = pow(e1, -1, phi1) 
print("\nRekonstruksi Kunci Privat 1 (d1) berhasil.")

q2 = n2 // p
phi2 = (p - 1) * (q2 - 1)
d2 = pow(e2, -1, phi2)
print("Rekonstruksi Kunci Privat 2 (d2) berhasil.")

try:
    with open('ciphertext.hex', 'r') as f:
        ciphertext_hex = f.read().strip() 
    
    c = int(ciphertext_hex, 16)
    print("\nCiphertext berhasil dibaca.")

except FileNotFoundError:
    print(f"Error: File 'ciphertext.hex' tidak ditemukan.")
    exit()
except ValueError:
    print(f"Error: 'ciphertext.hex' tidak berisi data hex yang valid.")
    exit()

print("\nMencoba dekripsi...")

try:
    m1_int = pow(c, d1, n1)
    m1_bytes = long_to_bytes(m1_int)
    print(f"\n--- Hasil Dekripsi dengan Kunci 1 ---")
    print(m1_bytes.decode('utf-8'))
except (UnicodeDecodeError, Exception) as e:
    print(f"\n--- Hasil Dekripsi dengan Kunci 1 (gagal decode / raw bytes) ---")
    print(m1_bytes)

try:
    m2_int = pow(c, d2, n2)
    m2_bytes = long_to_bytes(m2_int)
    print(f"\n--- Hasil Dekripsi dengan Kunci 2 ---")
    print(m2_bytes.decode('utf-8'))
except (UnicodeDecodeError, Exception) as e:
    print(f"\n--- Hasil Dekripsi dengan Kunci 2 (gagal decode / raw bytes) ---")
    print(m2_bytes)
