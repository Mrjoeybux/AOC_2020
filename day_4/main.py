def valid_passport_problem_1(passport, valid_fields):
    return all([field in passport.keys() for field in valid_fields])


def year_check(value, lb, ub):
    return (len(value) == 4) and (lb <= int(value) <= ub)


def hgt(value):
    if "cm" in value:
        return 150 <= float(value[:-2]) <= 193
    if "in" in value:
        return 59 <= float(value[:-2]) <= 76
    return False


def hcl(value):
    if (value[0] == "#") and len(value) == 7:
        valid_fields = [str(i) for i in range(10)] + ["a", "b", "c", "d", "e", "f"]
        return all([char in valid_fields for char in value[1:]])


def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(value):
    try:
        int(value)
    except:
        return False
    return len(value) == 9
    

def cid(value):
    return True


def parse_input(path):
    passports = []
    current_passport = []
    with open(path, "r") as f:
        for line in f:
            if line == "\n":
                passports.append({field.split(":")[0]: field.split(":")[1] for field in current_passport})
                current_passport = []
                continue
            current_passport += line.split("\n")[0].split(" ")
    passports.append({field.split(":")[0]: field.split(":")[1] for field in current_passport})
    return passports


def valid_passport_problem_2(passport, checking_funcs):
    return all([checking_funcs[field](passport[field]) for field in passport])


def problem_1(passports, valid_fields):
    valid_passports = 0
    for passport in passports:
        if valid_passport_problem_1(passport, valid_fields):
            valid_passports += 1
    return valid_passports


def problem_2(passports, valid_fields, checking_funcs):
    valid_passports = 0
    for passport in passports:
        if valid_passport_problem_1(passport, valid_fields):
            if valid_passport_problem_2(passport, checking_funcs):
                valid_passports += 1
    return valid_passports


if __name__ == "__main__":
    path = "input.txt"
    passports = parse_input(path)
    valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    print(problem_1(passports, valid_fields))
    checking_funcs = {
        "byr" : lambda value: year_check(value, 1920, 2002),
        "iyr" : lambda value: year_check(value, 2010, 2020),
        "eyr" : lambda value: year_check(value, 2020, 2030),
        "hgt" : hgt,
        "hcl" : hcl,
        "ecl" : ecl,
        "pid" : pid,
        "cid" : cid
            }
    print(problem_2(passports, valid_fields, checking_funcs))