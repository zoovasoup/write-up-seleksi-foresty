# Byte Circus
**Author:** ooflamp

**Difficulty:** -

---
## Description
ezpz

## Enumeration
diberikan file .pyc... trus saya coba di decompile
```
the_flag = [1423,1432,1403,1422,1404,1405,1410,1444,1436,1437,1450,1437,1458,1452,1416,1450,1463,1450,1461,1442,1436,1458,1436,1416,1458,1437,1416,1458,1436,1416,1450,1455,1372,1369,1452,1453,1446]
def enc(string):
  return [ord(x)^16+1337 for x in string]

def main():
  inp = input('Enter password: ').strip()
  inp_enc = enc(inp)
  if inp_enc == the_flag:
    print(f'''Correct! Flag: {inp}''')
    return None
  else:
    print('Wrong password')
    return None

if __name__ == '__main__':
  main()
```
ada variable `the_flag` namun ter-enkripsi

tinggal di decrypt
```python
the_flag_values = [
    1423, 1432, 1403, 1422, 1404, 1405, 1410, 1444, 1436, 1437, 1450, 1437, 
    1458, 1452, 1416, 1450, 1463, 1450, 1461, 1442, 1436, 1458, 1436, 1416, 
    1458, 1437, 1416, 1458, 1436, 1416, 1450, 1455, 1372, 1369, 1452, 1453, 
    1446
]

decrypted_chars = []

for val in the_flag_values:
    temp_val = val - 1337
    original_ord = temp_val ^ 16
    original_char = chr(original_ord)
    decrypted_chars.append(original_char)

the_flag = "".join(decrypted_chars)

print(f"The flag is: {the_flag}")
```

## Flag 
```
FORESTY{static_analysis_it_is_af30cd}
```
