
def main():
    larger = []
    larger_len = 0
    for line in sys.stdin:
        if '[' in line and ']' in line:
            lenght = line.count(',') + 1 if len(line[1:-2]) > 0 else 0
            if larger_len < lenght:
                larger_len = lenght
                larger = line[:-1]
    print(larger)

if _name_ == '_main_':
    main()