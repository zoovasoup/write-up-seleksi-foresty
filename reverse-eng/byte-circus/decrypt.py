
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
