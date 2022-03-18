import os
#dir=''
for folder, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.txt'):
            isOfType = os.path.join(folder, file)
            with open(isOfType, 'r') as opened:
                for line in opened:
                    #stringToBeFound = ''
                    if stringToBeFound in line:
                        print(line)
