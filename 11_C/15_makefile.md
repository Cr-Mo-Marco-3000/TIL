# Makefile

- 컴파일 과정
- 소스파일 -컴파일-> 목적파일 -링킹(기계어 + 라이브러리)-> 실행파일
- make 명령어를 입력하면, Makefile이라는 이름을 가진 파일 내부를 탐색하여 명령 실행

```Makefile
# Target: Dependency
#   command
# 기본적으로, 옵션 없이 make를 주었을 경우 첫 번째 Target만 실행 시키고 종료

#--- 변수 part ---
CC=gcc
TARGET=app.out
# OBJS는 내부 변수이긴 함
OBJS=main.o kor.o usa.o
# CFLAGS: 컴파일 옵션: -Wall: 모든 경고 띄움
CFLAGS = -Wall
# 링크 옵션
#LDFLAGS= -lc



```
