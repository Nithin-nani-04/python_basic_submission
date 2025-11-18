try:
    with open('sample.txt','r') as file:
        i=1
        print(f"Reading file content")
        for line in file:
            print(f"Line {i}: {line.strip()}")
        file.close()
except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")

