# a라는 기계에 “abcabc”라는 문자열을 넣으면 abcabcabcabc…처럼 “abc”를 넣었을 때와 같은 문자열이 출력됩니다.
# 두 문자열 s와 t가 주어졌을 때, 두 문자열을 a에 넣으면 같은 문자열을 만드는지 판별하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 s, 둘째 줄에 t가 입력됩니다. 두 문자열 s와 t의 길이는 50보다 작거나 같은 자연수이고, 알파벳 소문자로만 이루어져 있습니다.

# [출력]
# 두 문자열을 맷돌에 넣고 돌린 결과가 같으면 1, 다르면 0을 출력합니다.


# ------------------------------------------------------


s = input()
t = input()
a = 0
for i in range(len(t) // len(s)):
    if t[i*len(s): (i+1) * len(s)] == s:
        a += 1
if a == (len(t) // len(s)):
    print(1)
else:
    print(0)
