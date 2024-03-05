def find_missing_digits(n_str, prev_digit=None):
    if not n_str:
        return []

    current_digit = int(n_str[0])
    remaining_digits = n_str[1:]
    missing_digits = []

    if prev_digit is not None and current_digit > prev_digit + 1:
        for missing_digit in range(prev_digit + 1, current_digit):
            missing_digits.append(missing_digit)

    missing_digits += find_missing_digits(remaining_digits, current_digit)
    return missing_digits

number = 379
number_str = str(number)
missing_digits = find_missing_digits(number_str[1:], int(number_str[0]))

if missing_digits:
    print(f"Для числа {number} пропущены цифры: {', '.join(map(str, missing_digits))}.")
else:
    print(f"Для числа {number} нет пропущенных цифр.")
