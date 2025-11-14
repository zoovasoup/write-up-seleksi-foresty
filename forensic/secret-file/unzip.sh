
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
