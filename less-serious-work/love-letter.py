data_file = open("love.txt", 'r')
data = data_file.read()
data_file.close()

lines = data.splitlines()

for line in lines:
    print("*-" + "-" * len(line) + "-*")
    print("|", line, "|")
    print("*-" + "-" * len(line) + "-*")