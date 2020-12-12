def parse_lines(pswd_and_rule):
    rule, letter, password = pswd_and_rule.split(" ")
    first_num, second_num = map(int, rule.split("-"))
    return first_num, second_num, letter[0], password


def problem_1(pswds_and_rules):
    valid_passwords = 0
    for x in pswds_and_rules:
        lb, ub, letter, password = x
        if lb <= password.count(letter) <= ub:
            valid_passwords += 1
    return valid_passwords


def problem_2(pswds_and_rules):
    valid_passwords = 0
    for x in pswds_and_rules:
        index_1, index_2, letter, password = x
        at_index_1 = password[index_1 - 1] == letter
        at_index_2 = password[index_2 - 1] == letter
        if at_index_1 != at_index_2:
            valid_passwords += 1
    return valid_passwords



if __name__ == "__main__":
    filepath = "./input.txt"
    pswds_and_rules = []
    f = open(filepath, "r")
    for line in f:
        pswds_and_rules.append(parse_lines(line))
    f.close()
    print(problem_1(pswds_and_rules))
    print(problem_2(pswds_and_rules))
