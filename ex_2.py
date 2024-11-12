"""def replace_line(file, line, new_line):
    fh = open(file, 'r')
    content = fh.read()
    lines = content.split('\n')
    fh.close()

    if 0 < line <= len(lines):
        lines[line - 1] = new_line + '\n'
        content = ''.join(lines)

        with open(file, 'w') as file:
            file.write(content)
        print(f"Line {line} replaced successfully.")
    else:
        print(f"Invalid line number: {line}")


file = 'OS.txt'
line_num = 3
new_line = "This is the new line content"
replace_line(file, line_num, new_line)"""

def transform_text(file):
    fh = open(file, 'r')
    content = fh.read()
    fh.close()

    transformed_content = content.upper()

    fh = open(file, 'w')
    fh.write(transformed_content)
    fh.close()

    print("Text transformed and written back to the file.")

file = 'Multiprocessing.txt'
transform_text(file)
