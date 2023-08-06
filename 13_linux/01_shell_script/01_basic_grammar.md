# 1. 셸 스크립트 기초 문법

## I. 셸 스크립트 생성

셸 스크립트 파일을 만들 때는 `.sh` 확장자를 주로 이용하지만, 사실 권장되는 사항은 확장자를 붙이지 않는 것이다.

파일 생성 후 파일 맨 앞에 쉬뱅 `#!/bin/bash` 를 붙여서 해당 파일이 셸 스크립트인것을 알린다.

쉬뱅은 해당 파일을 실행할 때 어떤 명령어 해석기의 명령어 집합인지를 나타낸다. 헤당 부분에 오류가 있으면 실제로 파일이 정상 실행되지 않는다.

- 셸 스크립트 실행방법 3가지
  - sh filename.sh
  - `chmod +x filename.sh`로 파일 실행권한 부여 후 `./filename.sh` 로실행
  - 커맨드라인 직접 실행



## II. 변수

### 1. 변수 선언

- 일반적으로 셸 스크립트에서의 변수는 모두 문자열로 취급된다. 하지만 문맥에 따라서 이 문자열이 수식에서 계산되기도 한다.
- 즉, 타입으로 셸 스크립트의 변수를 구분하는것은 무의미하다
- [참고](https://tldp.org/LDP/abs/html/untyped.html)

- 변수를 선언할 때는 `변수=값` 형태로 선언한다. **주의할 점은 변수 선언시 띄어쓰기가 있으면 안 된다는 것이다.**

### 2. 변수 사용

- 사용할때는 `$변수` 형태로 사용한다.
- 문자열 내부에서 변수를 사용할때는, 큰따옴표""로 묶인 문자열 사이에서 `$변수`형태로 사용한다. 작은따옴표 사이에서는 단순히 $달린 문자로 취급된다.
- 명령문과 같이 변수를 사용할수도 있다.

```bash
#!/bin/bash

language="Korean"

# I love $language 출력
echo 'I love $language'

# I love Korean 출력
echo "I love $language"

# Korean 디렉터리 생성
mkdir $language

```

### 3. 함수

- `function functionName() {}`형태로 선언하고

- `functionName parmeter1 parameter2...`형태로 사용한다.

- parameter를 함수 내부에서 사용할 때는 `$1`, `$2`등으로 사용한다.
  - 스크립트 파일 실행시의 매개변수와 비슷하게 사용된다.

```bash
#!/bin/bash

function print() {
	echo $1
}

# I can speak korean 출력
print "I can speak korean"
```

### 4. 변수

#### 전역변수

- 스크립트 전체에서 변수에 저장한 값을 사용할 수 있는 변수
- 함수가 **선언되기 전**에 함수 밖에서 선언된 language라는 변수는 함수 내에서도 그 값이 유효하다.

#### 지역변수

- 함수 내에서만 변수에 저장된 값이 유효한 변수
- 변수 선언 앞에 `local`키워드를 붙여서 해당 함수 내에서만 변수를 유효하게 만든다.

- local 키워드 없이는 함수 안에서 선언된 변수라도 전역 변수로 취급되므로 주의하자

- 다른 언어와 마찬가지로 지역변수와 전역변수가 동일한 이름으로 선언된다면, 해당 함수 내에서는 전역변수가 더 먼저 선택된다.

#### 환경변수

- 시스템을 위해 사전에 미리 시스템에서 사용하고 있는 변수들
- 사전에 사용하고 있는 변수라서 예약변수라고 부르기도 한다.

- 종류
  - HOME: 사용자의 홈 디렉터리
  - PATH: 명령어나 셸 실행 시 실행 파일을 찾을 디렉터리 경로
  - FUNCNAME: 현재 함수 이름
  - LANG: 프로그램 사용 시 기본으로 지원되는 언어
  - PWD: 사용자의 현재 작업 중인 디렉터리
  - TERM: 로그인 터미널 타입
  - SHELL: 로그인해서 사용하는 셸
  - USER, USERNAME: 사용자 이름
  - GROUP: 사용자 그룹(/etc/passwd 값을 출력)
  - DISPLAY: X 디스플레이 이름
  - COLUMNS: 현재 터미널이나 윈도우 터미널의 컬럼 수
  - LINES: 터미널의 라인 수
  - PS1: 기본 프롬프트 변수
  - PS2: 보조 프롬프트 변수(기본값: >), 명령을 "`\`"을 사용하여 명령 행 연장 시 사용됨
  - PS3: 셸 스크립트에서 select 사용 시 프롬프트 변수
  - PS4: 셸 스크립트 디버깅 모드의 프롬프트 변수(기본값: +)
  - BASH: BASH 실행 파일 경로
  - BASH_VERSION: 설치된 BASH 버전
  - BASH_ENV: 스크립트 실행 시 BASH 시작 파일을 읽을 위치 변수
  - HISTFILE: history 파일 경로
  - HISTFILESIZE: history 파일 크기
  - HISTSIZE: history 저장되는 개수
  - HOSTNAME: 호스트 이름
  - HOSTTYPE: 시스템 하드웨어 종류
  - MACHTYPE: 머신 종류(HOSTTYPE과 같은 정보지만 더 상세히 표시)
  - MAIL: 메일 보관 경로
  - LOGNAME: 로그인 이름
  - TMOUT: 0이면 제한이 없으며 time시간 지정 시 지정한 시간 이후 로그아웃
  - SECONDS: 스크립트가 실행된 초 단위 시간
  - UID: 사용자 UID
  - OSTYPE: 운영체제 종류

#### 위치 매개변수

- 스크립트 실행 시 함께 넘어오는 파라미터
- 종류
  - $0: 실행된 스크립트 이름
  - $1, $2, ...: 실행 시 입력된 파라미터 순서대로 번호 부여, 10번부터는 ${10}같이 {}로 감싸주어야 함
  - $*: 입력된 전체 인자들
  - $@: 입력된 전체 인자들($*는 파라미터들을 하나의 문자열로 취급, $@는 문자열 배열로 취급)
  - $# 매개변수의 총 개수

- $*와 $@

  - 그냥 $*와 $@만 사용했을 경우에는, 차이점이 드러나지 않는다.

  ```bash
  #!/bin/bash
  
  for language in $*
  do
          echo "I can speak $language"
  done
  
  # 입력
  # sh my_language.sh Korean English "Japanese Chinese"
  
  # 출력
  # I can speak Korean
  # I can speak English
  # I can speak Japanese
  # I can speak Chinese
  
  #!/bin/bash
  
  for language in $@
  do
          echo "I can speak $language"
  done
  
  # 입력
  # sh my_language.sh Korean English "Japanese Chinese"
  
  # 출력
  # I can speak Korean
  # I can speak English
  # I can speak Japanese
  # I can speak Chinese
  ```

  - 하지만 스크립트 내부에서 큰따옴표와 함께 $*를 사용하면, 차이점이 드러난다.
    - $*는 매개변수를 하나의 문자열로, $@는 문자열 배열로 취급한다(단, ""로 묶은경우 제외)

  ```bash
  #!/bin/bash
  
  for language in "$*"
  do
          echo "I can speak $language"
  done
  
  # 입력
  # sh my_language.sh Korean English "Japanese Chinese"
  
  # 출력
  # I can speak Korean English Japanese Chinese
  
  ```

  ```bash
  #!/bin/bash
  
  for language in "$@"
  do
          echo "I can speak $language"
  done
  
  # 입력
  # sh my_language.sh Korean English "Japanese Chinese"
  
  # 출력
  # I can speak Korean
  # I can speak English
  # I can speak Japanese Chinese
  
  ```

#### 특수 매개변수

- 현재 실행 중인 스크립트나 명령어의, 프로세스 ID를 확인하거나 바로 앞에서 실행한 명령어나 함수 또는 스크립트 실행이 정상적으로 수행되었는지 여부를 확인할 수 있는 변수들을 의미한다.

- 종류
  - $$: 현재 스크립트 또는 명령어의 PID
  - $?: 최근에 실행한 명령어, 함수, 스크립트의 종료 상태 -> 정상일 경우 0
  - $!: 최근에 실행한 백그라운드(비동기) 명령의 PID
  - $~: 현재 옵션 플래그

#### 매개변수 확장

- 문자열 사이에서 변수를 사용할 때, 어디까지가 변수인지 확실히 정하기 위해 {}를 사용할 수 있다.
  - `$variable` == `${variable}`

