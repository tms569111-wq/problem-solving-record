# 일단 현재 있는 단일 수 중에서 가장 큰 수
# ex 18 이런 식이면 최소한 8까지는 되니까 무조건 9진수
# 즉 단일 수 중에서 가장 큰 수 + 1까지는 후보
# expressions가 최대 10문자 * 100개니까 1000번 연산으로 무조건 제일 큰 수 체크 가능
# 그렇게 후보 만 든 뒤에는
# 이미 있는 연산, X가 아닌 연산으로 또 진수 구하기
# 이때 한 자리수끼리 뺄셈은 음수 없으니까 무조건 결과 얻을 수 있음
# 두자릿수 또는 한자릿수 덧셈은 진수 필요
# 두자릿수 뺄셈은 경우에 따라 진수 필요
# 이미 있는 연산 법에서 진수의 존재를 알아야 함
# 생각보다 간단한 게 만약 이게 n진수라면...하는 연산의 시간 복잡도가 n ^ 2여도
# 100번 * 10번 * 1000번으로 백만 번 내외로 해결 됨.
# 즉 어떤 덧셈 또는 뺄 셈 연산이 나왔을 때에 n진수로 가정하고 했을 때와 같다면 후보가 생김
# 그 후보들의 교집합을 계속 구하다가 끝까지 했을 때 남는 후보들.
# 그 후보들로 봤을 때에 경우의 수가 많다면 ?를 출력하고 경우의 수가 1이라면 끝내버림
# 근데 무조건 제일 큰 수보다는 경우의 수가 커야 함
# 이거 보면 쉽게 할 듯
def solution(expressions):
    def to_base(num, base):
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            result = str(num % base) + result
            num //= base
        return result
    max_digit = 0
    for expression in expressions:
        a, op, b, _, c = expression.split()
        for num in [a, b]:
            for ch in num:
                max_digit = max(max_digit, int(ch))
        if c != 'X':
            for ch in c:
                max_digit = max(max_digit, int(ch))
    candidates = list(range(max(2, max_digit + 1), 10))
    for expression in expressions:
        a, op, b, _, c = expression.split()
        if c == 'X':
            continue
        new_candidates = []
        for base in candidates:
            a10 = int(a, base)
            b10 = int(b, base)
            c10 = int(c, base)
            if op == '+':
                if a10 + b10 == c10:
                    new_candidates.append(base)
            else:
                if a10 - b10 == c10:
                    new_candidates.append(base)
        candidates = new_candidates
    answer = []
    
    for expression in expressions:
        a, op, b, _, c = expression.split()
        if c != 'X':
            continue
        results = set()
        for base in candidates:
            a10 = int(a, base)
            b10 = int(b, base)
            
            if op == '+':
                value = a10 + b10
            else:
                value = a10 - b10
            results.add(to_base(value, base))
        if len(results) == 1:
            result = results.pop()
        else:
            result = '?'
        answer.append(f"{a} {op} {b} = {result}")
    return answer