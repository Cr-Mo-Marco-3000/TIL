# Shared Memory

서로 다른 프로세스가 메모리를 공유하는 것.
같은 메모리를 읽거나 쓸 수 있다.

- 종류
  - File-Memory mapping(파일을 이용한 방법)
    - File mapping
    - Anonymous mapping
  - Shared memory(API 이용 방법)
    - SysV shared memory
    - POSIX shared memory

## I. Memory Mapping

- 파일을 메모리에 매핑
  - file descriptor나 file pointer streaming을 이용한 파일 읽고 쓰기는,
  access가 sequential하지 않은 경우(앞 뒤, 또는 자유로운 이동이 불가능) 매우 불편하기 때문에 사용.
- 파일의 특정 영역을 메모리상(Process address space)에 그대로 매핑
  - 메모리를 읽거나 수정할 경우, 파일 내용이 읽어지고 수정됨

### II. Memory-mapping APIs

1. void *mmap(void*addr, size_t length, int prot, int flags, int fd, off_t offset);

- parameter
  - addr: mapping 될 address -> mapping될 메모리의 시작주소, 지정을 할 수도, 랜덤으로 할 수도 있다.
    - 랜덤으로 할 때 NULL을 넘겨준다.
  - length: mapping 할 길이 -> 바이트 단위
  - prot: mapping된 메모리 영역에 대해 어떤 권한을 요청하는지 설정
    - PROT_EXEC
    - PROT_READ
    - PROT_WRITE
    - PROT_NONE: 아무 권한도 요청하지 않음
  - flags: 메모리 영역을 공유 메모리로 사용하기 위해서는 MAP_SHARED로 사용요
    - MAP_SHARED
    - MAP_PRIVATE
    - MAP_FIXED: addr에 특정 메모리 주소를 넘길 때 지정
    - MAP_ANONYMOUS
  - fd: mapping 할 file의 fd
  - offset: 반드시 page size의 배수 -> 파일의 시작점부터 얼마나 떨어져 있는지 설정
    - 예를들어 page size가 2kb면, offset은 2kb의 배수여야 한다.
- return
  - 성공: mapping된 주소
  - 실패: MAP_FAILED -> NULL 아님!

2. int munmap(void *addr, size_t length);

- parameter
  - addr: mapped address
  - length: mapped 길이
- return
  - 성공: 0
  - 실패: -1
