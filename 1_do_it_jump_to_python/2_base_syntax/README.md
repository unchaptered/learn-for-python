[< Backward](../README.md)

# Base Syntax

## Syntax

### Escape Code

문자열 예제에서 여러 줄의 문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드를 사용했다. 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다. 몇 가지 이스케이프 코드를 정리하면 다음과 같다.

| 코드 |	설명                                               |
| ---- | ---------------------------------------------------- |
| \n |	문자열 안에서 줄을 바꿀 때 사용                         |
| \t |	문자열 사이에 탭 간격을 줄 때 사용                      |
| \\ |	문자 \를 그대로 표현할 때 사용                          |
| \' |	작은따옴표(')를 그대로 표현할 때 사용                   |
| \" |	큰따옴표(")를 그대로 표현할 때 사용                     |
| \r |	캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)  |
| \f |	폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)       |
| \a |	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)       |
| \b |	백 스페이스                                           |
| \000 | 널 문자                                             |

- [점프 투 파이썬 - 02-2 문자열 자료형#이스케이프 코드란?](https://wikidocs.net/13)

### Explicit and Implicit Boolean

```py
is_valid_user = True
is_unvalid_user = False

print(is_valid_user, is_unvalid_user) # True, False
```

| 자료형 | 참 | 거짓 |
| ----- | --- | --- |
| string | "hello" | "" |
| arrays | [1, 2, 3] | [] |
| set | (1, 2, 3) | () |
| dictionary | { 'a': 1 } | {} |
| number | 1 | 0 | 
| etc.. | - | None (None이라는 값이 존재함...) |

- [점프 투 파이썬 - 02-7 불 자료형#자료형의 참과 거짓](https://wikidocs.net/17)

### Comparison Operators

| 비교연산자 | 설명                 |
| --------- | -------------------- |
| x < y	    | x가 y보다 작다        |
| x > y	    | x가 y보다 크다        |
| x == y    | x와 y가 같다          |
| x != y    | x와 y가 같지 않다     |
| x >= y    | x가 y보다 크거나 같다 |
| x <= y    | x가 y보다 작거나 같다 |

- [점프 투 파이썬 - 03-1 If 문#and, or, not](https://wikidocs.net/20)

| 연산자 | 설명 |
| ------ | -------------------------------- |
| x or y | x와 y 둘중에 하나만 참이어도 참이다 |
| x and y | x와 y 모두 참이어야 참이다 |
| not x	| x가 거짓이면 참이다 |

- [점프 투 파이썬 - 03-1 If 문#in, not in](https://wikidocs.net/20)

| in          | not in |
| ----------- | -------------- |
| x in 리스트 | x not in 리스트 |
| x in 튜플   | x not in 튜플 |
| x in 문자열 | x not in 문자열 |