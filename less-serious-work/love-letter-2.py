letter = open("letter.txt", "r")
data = letter.read()

lines = data.splitlines()

for line in lines:
    line = line.replace('[blank]', 'Brittany')
    print(line)
    
letter.close()