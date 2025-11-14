# Secret File
**Author:** Cyrus

**Difficulty:** -

---
## Description
Flag nya ada di dalem zip :)

## Enumeration
diberikan `secret_file.zip` namun file tersebut tercompress berlapis-lapis...
kalau dari penamaannya mungkin 1000 kali...

kita buat bash script yang men-decompress file tersebut
```sh
mkdir zip_challenge
mv secret_file.zip zip_challenge/
cd zip_challenge

while [ $(find . -maxdepth 1 -name "*.zip" | wc -l) -gt 0 ]; do
    
    CURRENT_ZIP=$(find . -maxdepth 1 -name "*.zip" | head -n 1)
    echo "Unzipping: $CURRENT_ZIP"
    unzip -o "$CURRENT_ZIP"
    rm "$CURRENT_ZIP"
    
done

echo "All zips extracted! Looking for the flag..."
ls -l

cat flag.txt

```

## Flag 
```
FORESTY{kamu_gak_solve_challenge_ini_dengan_manual_kan_???}
```
