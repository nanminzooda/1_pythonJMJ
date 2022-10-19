# 자주 사용하는 리눅스 용어

'''

1. ls (list segments) : 현재 위치의 파일 목록 조회

ls - l : 파일의 상세정보
ls - a : 숨김 파일 표시
ls - t : 파일들 생성 시간순(최신순)으로 표시
ls - rt : 파일들 생성 시간순(제일 오랜된 것부터)으로 표시

2. cd (change directory) : 디렉터리 이동

cd 디렉터리경로 : 이동하려는 디렉터리로 이동
cd~ : 홈 디렉터리로 이동
cd/ : 최상위 디렉터리로 이동
cd. : 현재 디렉터리
cd.. : 상위 디렉터리로 이동
cd- : 이전 경로로 이동

3. touch : 0바이트 파일 생성,
            파일의 날짜와 시간을 수정
touch 파일명 : 파일명의 파일을 생성
touch -c filename : filename의 시간을 현재 시간으로 갱신!
touch -t 20221110142038 filename : filename의 시간을 날짜정보(YYYYMMDDhhmm)로 갱신
touch -r oldfile newfile : newfile의 날짜 정보를 oldfile의 날짜와 동일하게 변경

4. mkdir (make directory) : 디렉터리 생성

mkdir dirname : dirname 이라는 디렉터리 생성
mkdir dir1 dir2 : 한 번에 여러 디렉터리 생성
mkdir -p dirname/sub-dirname : dirname 생성 sur_dirame 하위 디렉터리 생성
mkdir -m 700 dirname : 특정 퍼미션(권한)을 갖는 디렉터리

8진수   2진수   권한 의미
0       000  ---   아무 권한 없음
1       001  --x   실행 권한만 있음
2       010  -w-   쓰기 권한만 있음
3       011  -wx   쓰기, 실행 권한만 있음
4       100  r--   읽기 권한만 있음
5       101  r-x   읽기, 실행 권한만 있음
6       110  rw-   읽기, 쓰기 권한만 있음
7       111  rwx   모든 권한 있음

-> 예를 들어 '777'의 경우 이진수로 11111111 이고
rwxrwxrwx 라는 의미를 가지므로
파일 소유자, 소유 그룹, 일반 사용자에게 읽기, 쓰기, 실행의 모든 권한을 주는 설정이다.

-> linux는 할 수 있어야 한다.

-> linux는 윈도우랑 같은 개념인 운영체제인데, 공짜라서 현업에서 많이 쓴다.
리눅스의 종류는 우분투, ... 우짤잘잘 ...

5. cp (copy) : 파일 복사

cp file1 file2 : file1을 file2라는 이름으로 복사
cp -f file1 file2 : 강제복사(file2라는 파일이 이미 있을 경우 강제로 기존 file2를 지우고 복사)
cp -r dir1 dir2 : 디렉터리 복사. 폴터 안의 모든 하위 경로와 파일들을 복사

6. mv (move) : 파일 이동

mv file1 file2 : file1 파일을 file2 파일로 변경
mv file1 /dir : file 파일을 dir 디렉터리로 이동
mv file1 file2 /dir : 여러 파일 dir 디렉터리로 이동
mv /dir1 /dir2 : dir1 디렉터리를 dir2 디렉터리로 이름 변경

7. rm (remove) : 파일 삭제

rm file1 : file1을 삭제
rm -f file1 : file1을 강제 삭제
rm -r dir : dir 디렉터리 삭제 (디렉터리는 -r 옵션 없이 삭제 불가)

8. cat (catenate) : 파일의 내용을 화면에 출력, 리다이렉션 기호('>')를 사용하여 새로운 파일 생성

cat file1 : file1의 내용을 출력
cat file1 file2 : file1과 file2의 내용을 출력
cat file1 file2 |more : file1과 file2의 내용을 페이지별로 출력
cat file1 file2 |head : file1과 file2의 내용을 처음부터 10번째 줄까지만 출력
cat file1 file2 |tail : file1과 file2의 내용을 끝에서부터 10번째 줄까지만 출력

9. redirection ('>', '>>') : 화면의 출력 결과를 파일로 저장

'>' 기호 : 기존에 있는 파일 내용을 지우고 저장
'>>' 기호 : 기존 파일 내용 뒤에 덧붙여서 저장
'<' 기호 : 파일의 데이터를 명령에 입력

10. head, tail : 파일 위(head) 아래(tail) 출력

# head, tail 자주 사용하는 옵션
head ./test.log #기본적으로 위(첫줄)에서부터 10줄까지 보여줌
head -n 5./test.log #위에서부터 5줄
head -n -5./test.log #밑에서부터 5줄 뺀 나머지 출력
cat./test.log | head -n 5 #cat 명령어 조합으로 사용

# 자주 사용되는 옵션
tail -n 10 ./test.log # 아래서부터 위로 10줄 출력
tail -n +5 ./test.log # 5번째 줄 부터 끝까지 출력
tail -f ./test.log #추가되는 내용 append 하여 출력됨


'''