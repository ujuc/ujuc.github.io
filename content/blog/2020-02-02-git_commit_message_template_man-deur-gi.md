Title: Git commit message template 만들기
Date: 2020-02-02 18:41
Modified: 2020-02-02 18:41
Category: Develop
Tags: git, commit, template
Slug: git-commit-message-template-man-deul-gi
Summary: Git commit message 에 변화를 만들고 싶었서 찾아봤다.

뭐때문에 여기까지 왔던건지 모르겠다.
그져 git commit message를 바꿔볼까 라는 생각에서 지금 여기로 온듯.

## 만들어보자!

### 1. Git config 에 추가

`.gitconfig` 파일에 `commit.template` 항목에 기본 값으로 등록할 내용을 추가해준다.
여기서 나는 `~/.gitmessage`라는 것을 전체 프로젝트에서 사용하도록 구성하겠다.

```
git config --global commit.template ~/.gitmessage
```

명령을 실행다면 `.gitconfig` 파일에 다음과같이 설정이된다.

```
[commit]
  template = ~/.gitmessage
```

### 2. Commit message Template 작성

`~/.gitmessage` 작성을 하자.

```
# <type>: <subject>
##### Subject 50 characters ################# -> |


# Body Message
######## Body 72 characters ####################################### -> |

# Issue Tracker Number or URL

# --- COMMIT END ---
# Type can be
#   feat    : new feature
#   fix     : bug fix
#   refactor: refactoring production code
#   style   : formatting, missing semi colons, etc; no code change
#   docs    : changes to documentation
#   test    : adding or refactoring tests
#             no productin code change
#   chore   : updating grunt tasks etc
#             no production code change
# ------------------
# Remember me ~
#   Capitalize the subject line
#     제목줄은 대문자로 시작한다.
#   Use the imperative mood in the subject line
#     제목줄은 명령어로 작성한다.
#   Do not end the subject line with a period
#     제목줄은 마침표로 끝내지 않는다.
#   Separate subject from body with a blank line
#     본문과 제목에는 빈줄을 넣어서 구분한다.
#   Use the body to explain what and why vs. how
#     본문에는 "어떻게" 보다는 "왜"와 "무엇을" 설명한다.
#   Can use multiple lines with "-" for bullet points in body
#     본문에 목록을 나타낼때는 "-"로 시작한다.
# ------------------
```

- 제목은 50자 이하로...
- 본문은 72자 이하로...
- 이슈는 남겨주는게 좋아서 트래커를 입력할 수 있도록...
- **NOTE**: `#` 으로 시작하는 줄은 삭제된다. 그리니 알아서 잘 띄우두도록하자.

## 레포마다 다르게 설정하기

다음 명령을 레포에서 입력한다.

```
git config commit.template ./path/to/.gitmessage
```

그리고 `.git/gitmessage`에 template을 작성해준다.

## 참고 사이트

- [Git Manual - Customizing Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
- [Create A Custom Git Commit Template](https://medium.com/@alex.wasik/create-a-custom-git-commit-template-84468232a459)
- [Better Commit Messages with a .gitmessage Template](https://thoughtbot.com/blog/better-commit-messages-with-a-gitmessage-template)
- [gist - adeekshith/.git-commit-template.txt](https://gist.github.com/adeekshith/cd4c95a064977cdc6c50)
- [Conventional Commits](https://www.conventionalcommits.org/ko/v1.0.0-beta.4/)
