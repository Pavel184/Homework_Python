# Pavel Krupenya
# Strings and words counter
out_f = open("out_file.txt", "r")
strCount = 0
wordCount = 0
for el in out_f:
    strCount += 1
    for i in el.split():
        wordCount += 1
print(f"Number of strings: {strCount - 1}\nNumber of words: {wordCount}")
out_f.seek(0)
print(out_f.readlines())
out_f.close()
input("\nPress Enter for exit")