import re

# Option: Ignore case (grep -i)
def grep_option_i(pattern, filename):
    with open(filename, 'r') as file:
        for line in file:
            if re.search(pattern, line, re.IGNORECASE):
                print(line.strip())

# Option: Count of matching lines (grep -c)
def grep_option_c(pattern, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                count += 1
    print(f"Count of lines matching the pattern: {count}")

print("Simulating 'grep' command with option 'i':")
grep_option_i('OS', 'file.txt')

print()
print("Simulating 'grep' command with option 'c':")
grep_option_c('OS', 'file.txt')
