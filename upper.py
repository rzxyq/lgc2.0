
append_format = "@cornell.edu"
with open("upper.txt", 'r') as f:
    file_lines = [''.join([x.strip(), append_format, '\n']) for x in f.readlines()]

with open("upper1.txt", 'w') as f:
    f.writelines(file_lines) 
