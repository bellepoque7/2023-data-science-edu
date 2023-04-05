import sys
read = sys.stdin.readline


def main():
    # s = read().rstrip()
    s = '12ab112ab2ab'
    # expose = read().rstrip()    # 폭발 문자열
    expose = '12ab'
    stack = []

    for c in s:
        print(stack)
        stack.append(c)     # 일단 무조건 push

        # 스택에 문자가 아직 expose의 길이 만큼 들어있지 않으면 확인할 필요 없음
        if len(stack) < len(expose):
            continue
        # 끝 글자 다르면 다른 문자열이기 때문에 확인할 필요 없음
        if expose[-1] != stack[-1]:
            continue

        temp = ""
        # 폭발 문자열 길이만큼 스택에서 뽑아내기
        for _ in range(len(expose)):
            temp += stack.pop()

        temp = temp[::-1]   # 스택 top에서 하나씩 뽑았으므로 뒤집어야 원래 문자열 확인 가능

        # 폭발 문자열이면 다음 문자로 넘어가기
        if expose == temp:
            continue

        # 다른 문자면 다시 넣기
        for i in temp:
            stack.append(i)

    if len(stack) == 0:
        print("FRULA")
    else:
        for c in stack:
            print(c, end='')


if __name__ == '__main__':
    main()