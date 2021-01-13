import os
dir=('') #edit this string to name the directory to be recursively searched
for folder, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.txt'): #editable for other file extension types such as html, csv, etc.
            isOfType = os.path.join(folder, file)
            with open(isOfType, 'r') as opened:
                for line in opened:
                    if '' in line: #declare the string to be found
                        print(line)
