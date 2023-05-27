#q1
'''from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Copying the contents of from_file to to_file
in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print("File copied successfully.")'''

#q2 q3
from sys import argv
script, from_file, to_file = argv

with open(from_file) as in_file, open(to_file, 'w') as out_file:
    out_file.write(in_file.read())

print("File copied successfully.")
print("Copied data is ")
print(out_file.read())

#q4
'''Closing files explicitly using the close() method is considered good practice.
It ensures resource management, data integrity, and portability of the code.
Explicitly closing files releases system resources, flushes buffered data, and ensures consistent behavior across platforms'''


