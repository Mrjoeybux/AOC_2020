

def problem_1(entries):
    n = len(entries)
    for i in range(n):
        for j in range(i, n):
            if entries[i] + entries[j] == value:
                return entries[i]*entries[j]

def problem_2(entries):
    n = len(entries)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if entries[i] + entries[j] + entries[k] == value:
                    return entries[i]*entries[j]*entries[k]

if __name__ == "__main__":
    input_file = "./input.txt"
    entries = []
    value = 2020
    f = open(input_file, "r")
    for entry in f:
        entries.append(int(entry))
    f.close()


    print(problem_1(entries))
    print(problem_2(entries))
            