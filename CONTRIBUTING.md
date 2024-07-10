# 깃 브렌치 사용 방법

git pull
git checkout -b 브렌치명   브렌치로 이동됨
코드작업
git status
git add . or git add 파일명          파일들이 스테이징됨?
git commit -m " :memo: 메시지"
git push origin 브렌치명


깃허브 사이트로 이동
레포지토리로 이동
상단에 있는 pull request 발행
원하시는 분은 merge까지 하셔도 됩니다.



# 깃허브 프로젝트 기본 프로세스
---------------------------------
명령어들
cd 폴더명                            작업 위치를 폴더명으로 이동
git status                              현재 상태(?)를 확인
 git add .                             파일을 스테이지에 올림
git commit -m " "               스테이지에 올린 파일을 커밋하고, 메시지 작성
git push origin main           본인의 깃허브에 푸시 함
git clone 주소                 깃허브 주소를 로컬(본인의 컴퓨터)에 연결?함
git reset --hard HEAD^       하드 리셋
git pull origin main             깃허브에 작성되어 있는 것을 로컬로 당겨옴
git --version                        깃의 버전을 확인
git checkout -b 브런치명    branch가 있다면 거기로 이동 없다면 생성 후 이동
git branch -D 브런치명    브렌치 삭제
git checkout 브렌치명        브렌치나 메인으로 이동




글을 작성하는 순서
Issues를 작성해서 내가 작업한다고 알리기
sync를 해서 깃허브 동기화
powershell 키기
cd 원하는폴더위치
code . 으로 vscode 열기( code 다음에 띄어쓰기 하고 .)
git pull로 변경사항 가져오기
CONTRIBUTING 형식으로 글을 작성
git status 로 변경된 파일 확인
git add . 또는 git add 파일위치 를 이용해서 수정된 파일을 스테이지에 올림
git status를 이용해서 스테이지에 올라갔는지 확인
git commit -m "커밋에 들어갈 말"
git push origin main 으로 깃허브에 푸쉬
자신의 깃허브 포크해온 Repositories에 들어간다.
Contribute를 누른 후 Open pull request를 누름
제목 작성, 설명을 작성 (설명을 작성할 때, 이슈의 번호를 기입해야  한다.)
다 작성한 다음 Create pull request를 눌러 pull request를 요청한다.
