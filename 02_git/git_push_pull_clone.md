# Git push / pull / clone

## Git push

### git remote 등록

1. git remote
   
   - 로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
   1. **원격 저장소 등록**
      
      `git remote add <이름> <주소>` 형식으로 작성합니다.
      
      ```bash
      $ git remote add origin <https://github.com/edujustin-hphk./TIL.git>
      
      [풀이]
      git 명령어를 작성할건데, remote(원격 저장소)에 add(추가) 한다.
      origin이라는 이름으로 <https://github.com/edujustin-hphk./TIL.git라는> 주소의 원격 저장소를
      ```
   
   2. **원격 저장소 조회**
      
      `git remote -v` 로 작성합니다.
      
      ```bash
      $ git remote -v # verbose
      origin  https://github.com/edujustin-hphk./TIL.git (fetch)
      origin  https://github.com/edujustin-hphk./TIL.git (push)
      
      add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력됩니다.
      ```
   
   3. **등록된 원격 저장소 주소 삭제**
      
      `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성합니다.
      
      > 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 게 아닙니다.
      
      ```bash
      $ git remote rm origin
      
      # 또는
      
      $ git remote remove origin
      
      [풀이]
      git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
      그 원격 저장소의 이름은 origin이다.
      ```

### 저장소 업로드

- 실습 때 작성했던 TIL 파일을 Github 원격 저장소에 업로드 해보겠습니다.

- **정확히 말하면, 파일을 업로드하는 게 아니라 커밋을 업로드 하는 것입니다!**

- 따라서 먼저 로컬 저장소에서 커밋을 생성해야 원격 저장소에 업로드 할 수 있습니다.
1. **로컬 저장소에서 커밋 생성**
   
   ```bash
   # 현재 상태 확인
   
   $ git status
   On branch master
   
   No commits yet
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           day1.md
   
   nothing added to commit but untracked files present (use "git add" to track)
   ```
   
   ```bash
   $ git add day1.md
   ```
   
   ```bash
   $ git commit -m "Upload TIL Day1"
   [master (root-commit) f3d6d42] Upload TIL Day1
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 day1.md
   ```
   
   ```bash
   # 커밋 확인
   
   $ git log --oneline
   f3d6d42 (HEAD -> master) Upload TIL Day1
   ```

### git push

- 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
- `git push <저장소 이름> <브랜치 이름>` 형식으로 작성합니다.

```bash
$ git push origin master

[풀이]
git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
```

## Git pull & Git clone

pdf 자료 참고

```bash
$ git clone [원격저장소 주소]

$ git pull origin master
```



### 1. 레포지토리 복사

- 복사할 때 사용할 수 있는 옵션에는
  
  - `--mirror`, `--bare` 두 가지가 존재
  
  - `--mirror`를 사용한 옵션만 서술

```bash
$ git clone --mirror {old repo}
$ cd {기존 리파지토리 명}.git
$ git remote set-url --push origin {new repo}
$ git push --mirror
```


