def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)

        else:
            bit = "0" + bin(num)[2:]
            idx=bit.rfind("0")

            bit = list(bit)

            bit[idx] = "1"
            bit[idx + 1] = "0"

            answer.append(int("".join(bit), 2))

    return answer