## I. 리눅스 기본 커맨드라인
>
> 아래 커맨드 중 일부는 커맨드가 아닌 tool
> 매뉴얼 조회: man
> 파일 목록/내용 조회 명령어: ls, cat, head, tail
> 검색/탐색 관련 명령어: grep, find
> 압축/해제 관련 명령어: tar, gzip/gunzip, zip/unzip
> 시간 관련 명령어: date, cal
> 기타 명령어: echo, exit, history
> 관리자 권한 실행: sudo
> 패키지 매니저: apt
> 텍스트 에디터: nano

### 1. man

- 메뉴얼
- `man [command]`
- 위 아래로 가기; `j, k``
- 페이지 단위로 아래로 / 위로가기: `f, space, pgdn` / `b`
- 검색 / 검색된 다음 단어로 가기 / 뒤 단어로 가기: `/` / `n` / `N`

### 2. 디렉터리 내용 조회 / 이동 / 확인

1. ls
    - `ls alrt`: 파일들을 수정시간 오름차순으로 보여줌
2. cd
    - 단독 입력시 홈 디렉터리(~)로 이동
3. pwd
    - bash가 기억하고 있는 현재 디렉토리를 출력

### 3. 파일 내용 조회

1. cat
    - 파일을 다 보여준다.

2. head
    - 파일 앞부분을 보여준다.
    - `head -n 3 [filename]`: 3줄 출력

3. tail
    - 파일 뒷부분을 보여준다.

4. less / more
    - 파일 일부분을 조금씩 잘라서 보여준다.

5. file
    - 해당 파일이 어떤 종류의 파일인지 알아본다.

- 참고: --help 또는 -h를 명령 뒤에 붙였을 때, 가이드를 주기도 한다.

### 4. 검색

1. grep
    - 파일 내용 검색
    - `grep -옵션 '문자열' 파일들...`
    - 문자열에 띄어쓰기가 있을 때는 ''로 묶어준다.
    - pipeline을 사용한 방법
        - 앞 실행결과의 출력을, 뒤 명령의 입력으로 넣어준다.
            - `ls -al | grep kern.log`
        - 명령으로 나온 결과의 앞 10줄만 보여준다.
            - `grep "hello world" myfile.log | head`
        - 파일에서 특정 문장 찾기
            - `grep "hello world" myfile.log`
            - `cat myfile.log | grep "hello world"`

2. find
    - 파일 검색
    - `find` 단독 입력 시 `find . -print`와 같은 의미
    - 해당 디렉토리, 하위 디렉토리 및 하위 디렉토리상의 모든 파일들 출력
    - expression 부분에는 따옴표 필수!
    - 현재 디렉토리에서 파일 이름이 `.conf` 로 끝나는 파일 찾기
        - `find [.] -name "*.conf" [-print]`
    - find & grep: .o로 끝나는 파일을 찾기 -> 따옴표와 이스케이프 시퀀스를 넣어주어야 한다.
        - `find | grep "\.o"`

### 5. 압축

> 압축 파일의 종류
> `.gz., .bz, .gz`

1. 압축
    - gzip

2. 압축해제
    - gunzip

3. 파일 묶기
    - `tar -cf test.tar`
    - 옵션은 각각 `create, file`을 의미
    - 해당 이름으로 tar 생성

4. 파일들을 연결하여 묶은 후 압축
    - `tar -zcf test.tar.gz filelist snap/`
        - .tar.gzip == .tgz 만들기
        - filelist와 snap/을 묶은 뒤 압축
        - 옵션의 순서를 주의해야 한다. f: 이름을 정하는 옵션 바로 뒤에 이름이 붙어야 하기 때문이다.

5. 압축 풀기
    - `tar -zxf test.tar.gz``
    - extract

### 6. 시간 및 기타 커맨드

1. 날짜 및 시간
    - `date [옵션] [+포맷]`
    - 옵션
        - u: UTC 표준시간으로 표시
    - 포맷
        - `date +%Y-%m-%d` 등으로 포맷팅을 해서 출력

2. 달력
    - cal [옵션] [연도]
    - 옵션
        - RHEL에서는 좀 다른가보다
        -A month: 현재부터 이후 2개월을 보여줌
        -B month: 현재부터 이전 2개월을 보여줌
        -d yyyy-mm: 특정 연-월의 달력을 보여줌

3. history
    - `[!number]로 실행`
    - `!!` 직전 커맨드 다시 실행

4. exit
    - 셸을 끝냄
    - 따라서 셸이 하나만 열려 있는 경우에는 터미널도 끝냄

5. echo
    - 출력
    - $변수명으로 변수 출력 가능
        - 자주 사용하는 변수
            - $PWD
            - $PATH: 특정 명령어의 command를 실행했을 때,

6. env
    - 환경변수 살펴보기

7. which
    - 특정 커맨드의 실행 파일 위치 검색

### 7. 관리자 권한 실행

> 프로그램은 기본적으로 관리자 권한으로 신청해야 함

1. sudo
    - substitute user do라는 의미
    - 원래는 다른 계정의 권한으로 명령을 실행하라는 의미
    - 계정을 지정하지 않으면 root 계정의 권한으로 실행하게 됨
    - 명령어 앞에 sudo를 붙여 사용

### 8. 패키지 매니저 사용

> fedora에서는 yum, devian에서는 apt를 사용
> 레포지토리로부터 설치 조회 사용

1. 설치
    - `sudo apt install packagename`
2. 제거
    - `sudo apt remove packagename`
    - `sudo apt autoremove packagename`
        - 해당 패키지를 삭제했을 때, 다른 패키지에서 사용하지 않는 의존성 패키지들도 같이 제거
3. 조회
    - `apt list`
        - 현재 리눅스 버전에 설치 가능한 패키지들을 조회
    - `apt list --installed`
        - 현재 설치되어 있는 패키지들 조회
    - grep을 통해 특정 패키지 검색 가능
