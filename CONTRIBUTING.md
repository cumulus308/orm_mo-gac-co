# 문제 리뷰 작성할 때 권장사항
 * 링크를 달아주세요!
 * 간단하게 주석을 달아주세요!
 안하셔도 괜찮지만 다른 분들에게 많은 도움이 됩니다!

# 터미널 명령어 모음 (깃에서도 사용가능합니다.)
| 명령어 | 명령어 내용                        |
|--------|------------------------------------|
| cd 폴더명 | Change Directory / 작업 위치를 폴더명으로 이동 |
| pwd    | Print Working Directory / 현재 작업중인 위치  |
| ls     | List / 현재 작업중인 디렉토리에 있는 파일 목록 |
| mkdir  | Make Directory / 디렉토리를 만듦     |
| .      | 현재 디렉토리                       |
| ..     | 상위 디렉토리                       |

# 깃 명령어 모음
| 명령어                        | 명령어 내용                                      |
|-------------------------------|-------------------------------------------------|
| git --version                 | 깃의 버전을 확인                                 |
| git status                    | 현재 상태를 확인(변경, 추가, 삭제 등)            |
| git add .                     | 파일을 스테이징 영역에 올림                      |
| git commit -m " "             | 스테이징 영역에 올린 파일을 커밋하고, 메시지 작성 |
| git push origin 브랜치명       | 원격저장소의 해당 브랜치로 푸시                  |
| git clone 주소                 | 깃허브 주소를 로컬(본인의 컴퓨터)에 연결함       |
| git reset --hard HEAD^        | 하드 리셋                                        |
| git pull                      | 깃허브에 작성되어 있는 것을 로컬로 당겨옴        |
| git checkout -b 브런치명      | branch가 있다면 거기로 이동 없다면 생성 후 이동  |
| git branch -d 브런치명         | 브렌치 삭제                                      |
| git checkout 브랜치명          | 해당하는 브랜치로 이동                           |


# branch
## branch를 사용하는 이유
* 안정성 :
  * main으로 바로 push했을 때, 버그가 있을 경우 main을 복구하기 어렵습니다. branch를 사용하면 원본을 건드리지 않고 작업을 할 수 있기 때문에 안정성이 증가합니다.
* 충돌 최소화 및 병행 작업 :
  * 여러 개발자가 작업을 수행하고 push를 할 경우, 충돌이 생길 가능성이 높아집니다. branch를 사용하면 개발자들은 서로 다른 작업을 진행할 수 있고, 이것으로 인한 충돌 가능성이 줄어듭니다.
* 버전 나누기:
  * 저희가 지금하는 repository는 버전 관리를 할 필요가 없지만, 대형 프로젝트에서는 버전을 나누기 위해 사용하고는 합니다.

## branch를 이용한 프로세스
git checkout main               작업환경을 메인으로 이동
git pull                        원격에 있는 자료를 로컬로 당겨옴
git checkout -b 브랜치명         브렌치 생성 후 이동
(필요시)git branch -d 브랜치명    브렌치 삭제
코드 작업
git status                       변경된 파일 확인
git add . or git add 파일명       파일을 개별적 또는 전체를 add하여 스테이징 영역에 올림
git commit -m ":memo: 메시지"     스테이징에 올린 파일을 커밋(:memo:)
git push origin 브랜치명         원격 저장소의 브랜치로 push를 함

깃허브 사이트로 이동
repository로 이동
상단에 있는 pull request 발행
---------여기부터는 원하시는 분들만------
merge버튼 누르기
merge완료 후 자신이 사용한 branch를 삭제

# 깃허브 프로젝트 기본 프로세스

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
