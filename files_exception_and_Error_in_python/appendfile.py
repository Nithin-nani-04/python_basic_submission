try:
    with open(r'output.txt',"w") as file:
        message=str(input("Enter text to write to the file: "))
        file.write(message)
        print("Data successfully written to output.txt")
        file.close()
    with open(r"output.txt",'a') as file:
        message=str(input("Enter additional text to append"))
        file.write('\n'+message)
        print("Data successfully appended")
        file.close()

    with open('output.txt','r') as file:
        print(f"Final content of Output.txt")
        for line in file:
            print(f"{line.strip()}")
        file.close()
    
except Exception as e:
    print("an error occured:",e)