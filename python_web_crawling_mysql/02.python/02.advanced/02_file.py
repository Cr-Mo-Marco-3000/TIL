# 파일 읽기, 쓰기

# r: 읽기
# w: 파일 쓰기
# a: (파일이 존재x) 쓰기 또는 (파일이 존재시) 덧붙이기

# 1. 파일 읽기
'''
f = open('./resource/python.txt', 'r') # 파일을 특정 모드로 사용

print(f) # 나오는 io io모듈을 의미 =>  input, output => 객체형태 

contents = f.read() # 전체 파일 읽기 => string으로 읽어온다.

print(contents)

f.close() # 닫아주지 않으면 자원 낭비가 된다.
'''


# 2. 파일 읽기 2
# 파일을 열고 알아서 닫아주는 기능이 있어서, 따로 close()를 사용할 필요가 없다.
# auto close 기능

with open('./resource/python.txt', 'r') as f_2:

    # 1) read()
    # contents = f_2.read()
    # iter() => iterator 반환
    # print(iter(contents))
    # print('>>>', type(contents))

    # read()는 파일을 한 번에 다 읽는다
    # 위에서 다 읽었기 때문에, 더 읽을 부분이 없다.

    # contents = f_2.read()
    # print('>>>', contents)

    # 2) readline() =>  한 줄씩 읽기
    contents = f_2.readline()
    print('>>>', contents)

    # 3) readlines() => 전체 내용을 읽은 뒤에, 라인 단위의 리스트로 저장
    # contents = f_2.readlines()
    # print('>>>', contents)

    # for content in contents:
    #     print(content, end='')

# 3. 파일 쓰기 => write() 파일 생성
with open('./resource/info.txt', 'w') as f_3:
    f_3.write('nice day!\nnice day!\nnice day!\nnice day!\nnice day!\n')


# 3-1. mode='a' => add => 맨 뒤에 하나 더 붙음
# with open('./resource/info.txt', 'a') as f_3:
    # f_3.write('nice day!\n')

# 4. 파일 쓰기 => 라인을 기준으로 저장
# with open('./resource/info2.txt', 'w') as f_3:
#     # f_3.writelines('alpha\nbeta')
#     f_3.writelines(['alpha\n', 'beta'])

# 5. 파일 쓰기 => 파일로 바로 저장
# with open('./resource/info3.txt', 'w') as f_4:
#     # 출력이 아닌 저장이 된다.
#     print('freedom', file=f_4)

# with open('./resource/score.txt', 'r') as f_5:
#     my_list = list(map(int, f_5.read().split('\n')))
#     print(sum(my_list) / len(my_list))
