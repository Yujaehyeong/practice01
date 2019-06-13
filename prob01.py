# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

# try:
#     number = int(input('수를 입력하세요: '))
#     if number > 0 and (number % 3) == 0:
#         print('3의 배수 입니다.')
#     else:
#         print('3의 배수가 아닙니다.')
# except ValueError:
#     print('정수가아닙니다')


# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

# try:
#     number = int(input('수를 입력하세요: '))
#     if number % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# except ValueError:
#     print('정수가아닙니다')


# 문제3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

# number = 1
# for i in range(0, 10):
#     for j in range(0, number):
#         print ('*', end='')
#
#     number+=1
#     print(end='\n')

# 문제4. 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

# 10보다 작을때 까지 true
# for i in range(1, 10):
#     for j in range(1, 10):
#         print (i,'x',j,'=', i*j, end='\t\t')
#     print(end='\n')


# 문제5. 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
#
# def checkMultipleOfThree(list):
#     count = 0
#     sum = 0;
#     for number in list :
#         if number > 0 and (number % 3) == 0:
#             count = count+1
#             sum = sum + number
#     return [count , sum]
#
# list = [3, 1, 7, 12, 8, 97, 23, 55, 6, 9]
# count, sum = checkMultipleOfThree(list);
#
# print('주어진 리스트에서 3의 배수의 개수 =>', count)
# print('주어진 리스트에서 3의 배수의 합 =>', sum)


# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전,
# 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.

# cash = int(input('금액: '))
#
# count = int(cash / 50000)
# cash = cash % 50000
# print('50000원:', count, '개')
# count = int(cash / 10000)
# cash = cash % 10000
# print('10000원:', count, '개')
# count = int(cash / 5000)
# cash = cash % 5000
# print('5000원:', count, '개')
# count = int(cash / 1000)
# cash = cash % 1000
# print('1000원:', count, '개')
# count = int(cash / 500)
# cash = cash % 500
# print('500원:', count, '개')
# count = int(cash / 100)
# cash = cash % 100
# print('100원:', count, '개')
# count = int(cash / 50)
# cash = cash % 50
# print('50원:', count, '개')
# count = int(cash / 10)
# cash = cash % 10
# print('10원:', count, '개')
# count = int(cash / 5)
# cash = cash % 5
# print('5원:', count, '개')
# count = int(cash / 1)
# cash = cash % 1
# print('1원:', count, '개')



# 문제 7. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오.

# list = []
# for i in range(0, 5):
#     list.append(int(input('>')))
# sum=0
# for i in list:
#     sum+=i
#
# print(sum/len(list))


# 문제8. 문자열을 입력 받아, 해당 문자열을 문자
# 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

# def reverse(s):
#     result = ''
#     size = len(s)-1
#     for i in range(0, size+1):
#         result+=s[size-i]
#     return result
#
# str = input('입력> ')
# result = reverse(str)
#
# print('결과>', result)


# 문제9. 주어진 if 문을 dict를 사용해서 수정하세요.

# menu = input('메뉴: ')
# dic = {'오뎅' : 300, '순대' : 400, '만두' : 500}
# if dic.__contains__(menu) == False:
#     price =0
# else :
#     price = dic.get(menu)
# print('가격: {0}'.format(price))


# 문제10 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

number = int(input('숫자를 입력하세요: '))
divideResult = 0
if(number % 2==0):
    divideResult = 0
else:
    divideResult = 1
sum = 0
for i in range(1, number+1):
    if (i % 2) == divideResult:
        sum += i
print('결과 값 :', sum)
