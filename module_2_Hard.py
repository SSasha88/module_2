def find_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i, n):
            if (i + j) % n == 0:
                password += f"{i}{j}"
    return password
for number in range(3, 21):
    print(f"Пароль для числа {number} - {find_password(number)}")