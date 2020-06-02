# Pavel Krupenya
# List
s = set("abcd")
fs = frozenset("efgh")
for ind, el in enumerate([None, 1, "two", 3.0, [4, 5], {6 : 7}, (8, 9), s, fs, True, ZeroDivisionError, b'bytes', bytearray(b'bytes')], 1):
    print(ind, type(el))
input("\nPress Enter to exit")