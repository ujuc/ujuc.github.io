Title: Git flow, GitHub flow, GitLab flow
Date: 2015-12-16 08:50
Category: Develop
Tags: git, workflow, github, gitlab
Slug: git-flow-github-flow-gitlab-flow
Summary: Git flow, GitHub flow, GitLab flow 에대해서 좀 알아보자. 머리아프다.

회사에서  `git`을 가지고서 버전관리를 본격적으로 하면서, 너무 많은 부분에서 문제가 발생을 하는 것을 보고 이걸 어떤 방식으로 사용하면 조금더 꼬이는 것을 방지할 수 있을까라는 생각을 하고 있다. 
물론 새로운 프로젝트를 진행하면서 어떤 방법으로 진행하는 것이 맞는 것인지도 필요하기도 했고, 그러다가 [이상한 모임 Slack]()에서 관련 이야기가 나오면서 커밋을 하기위한 방법론 중 하나인 `git-flow`의 종류가 3가지나 된다는 것을 보고 이놈들의 다른 점이 무엇인지 어떤 방법에서 편한 것인지에 대한 내용을 확인하고 싶어졌다.

## [Git Flow](https://github.com/nvie/gitflow)

> [Vincent Driessen이 말한 branching model](http://nvie.com/posts/a-successful-git-branching-model/)를 구현한 Git 확장 모듈이다. - [nvie/gitflw](https://github.com/nvie/gitflow)

기본 브랜치는 5가지를 이야기한다. `feature > develop > release > hotfix > master` 브랜치가 존재하며, 머지 순서는 앞에서 뒤로 진행된다. `release` 브랜치와 `hotfix` 브랜치의 경우, `develop` 브랜치의 오른쪽에 존재하기에 모두 `develop` 브랜치도 머지를 하도록 구성이 되어있다.

Vincent Driessen은 관련하여 스크림트로 명령을 구성해놨으며, 그냥 설치를 하여 CLI에서 명령으로 작업을 하여도 되고, GUI 툴들에서 기본 내장 git-flow 명령이나 플러그인을 설치하여 작업을 진행할 수 있도록 보편화되어잇는 브런칭 모델이다.

![Git Flow model](http://nvie.com/img/git-model@2x.png)

### 구조와 흐름

가장 중심이되는 브랜치는 `master`랑 `develop` 브랜치이며, 이 두개의 브랜치는 무조건 있어야된다고 보면된다. 이름은 바뀔수 있다만 왠만해서는 변경하지 않고 진행하도록 하자. Git도 Production에서 사용하는 브랜치는 `master`를 사용하게 되니 관련된 부분을 변경하면 새로운 사람이 왔을때 스터디 커브가 존재할 수 있다.

머지된 `feature`, `release`, `hotfix` 브랜치는 삭제하도록 한다.

#### Feature 브랜치

* 브랜치 나오는 곳 : `develop`
* 브랜치가 들어가는 곳 : `develop`
* 이름 지정 : `master`, `develop`, `release-*`, `hotfix-*`를 제외한 어떤 것이든 가능.

새로운 기능을 추가하는 브랜치이다.
`feature`브랜치는 `origin`에는 반영하지 않고, 개발자의 reop애만 존재하도록 한다.

여기서 머지를 할때, `--no-ff` 옵션을 이용하여 브랜치에서 머지가 되었음을 git 기록에 남겨두도록 한다. 이렇게되면 나중에 히스토리 관리가 어려워지는 부분이 존제한다고 한다만... 그것을 확인할 수 있는 방법들은 많으니 뭐...

#### Release 브랜치

* 브랜치 나오는 곳 : `develop`
* 브랜치가 들어가는 곳 : `develop`, `master`
* 이름 지정 : `release-*`

새로운 Production 릴리즈를 위한 브랜치이다.
지금까지 한 기능을 묶어 `develop` 브랜치에서 `release` 브랜치를 따내고, `develop` 브랜치에서는 다음번 릴리즈에서 사용할 기능을 추가한다.
`release` 브랜치에서는 버그픽스에 대한 부분만 커밋하게되고, **릴리즈가 준비되었다고 생각하면** `master`로 머지를 진행한다. (이때도 `--no-ff` 옵션을 이용하여 머지하였음을 남긴다.) 
`master`로 머지 후 `tag` 명령을 이용하여 릴리즈 버전에 대해 명시를 하고, `-s` 나 `-u <key>` 옵션을 이용하여 머지한 사람의 정보를 남겨두도록 한다. 그런뒤 `develop` 브랜치로 머지하여, `release` 브랜치에서 수정된 내용이 `develop` 브랜치에 반영이되도록 한다.

#### Hotfix 브랜치

* 브랜치 나오는 곳 : `master`
* 브랜치가 들어가는 곳 : `develop`, `master`
* 이름 지정 : `hotfix-*`

Production에서 발생한 버그들은 전부 여기로... 수정 끝나면, `develop`, `master` 브랜치에 반영하고, `master`에 다가는 `tag` 를 추가해준다.
만약 `release` 브랜치가 존재한다면, `release` 브랜치에 `hotfix` 브랜치를 머지하여 릴리즈될때 반영이 될 수 있도록 한다.

### 장점
* 명령어가 나와있다.
* 왠만한 에디터와 IDE에는 플러그인으로 존재한다.

### 단점
* 브랜치가 많아 복잡하다.
* 안쓰는 브랜치가 있다. 그리고 몇몇 브랜치는 애매한 포지션이다.

### 참고
* [A successful Git branching model - Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/)
* [git-flow cheatsheet](http://danielkummer.github.io/git-flow-cheatsheet/index.ko_KR.html)
* [nvie/gitflw](https://github.com/nvie/gitflow)
* [gifflow, 쉬운 git brunch 관리 - 개발왕 김코딩](http://huns.me/development/1131)
* [git 브랜칭 전략과 git flow - 꿀벌개발일지](http://ohgyun.com/402)

## GitHub Flow

Scott chacon은 [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html)에서 Git flow가 좋은 방식이긴 하지만 GitHub에서 사용하기에는 복잡하다 여겨 사용하지 않고 `GitHub Flow`라는 내용으로 사용을 하고 있다고 한다. 그리고 **자동화의 계념이 들어가 있다는 점**. 자동화가 안되어있는 곳에서는 수동으로 관련 작업을 진행하면 된다.

흐름이 단순한만큼 룰도 단순하다. `master` 브랜치에대한 `role`만 정확하다면 나머지 브랜치들에는 관여를 하지 않는다. 그리고 `pull request` 기능을 사용하도록 권장을 한다.

![GitHub Flow Model](http://cdn-ak.f.st-hatena.com/images/fotolife/s/shoma2da/20151104/20151104223339.png)

### 특징
* `release` 브랜치가 명확하지 않는 시스템에서 사용에 맞게 되어있다. 
  * 여기에는 GitHub의 서비스 특성상. 릴리즈라는 개념이 없는 서비스를 진행하고 있어서 그런것으로 보이며, 웹 서비스들이 릴리즈라는 개념이 없이지고 있으니 사용하기 편할 것으로 보인다.
* `hotfix`와 가장 작은 기능을 구분하지 않는다. 어짜피 둘다 개발자가 수정해야되는 일중에 하나이다. 단지 우선 순위가 어디가 높냐라는 단계이다.

### 그럼 어떻게 사용할 것인가?

#### 1. `master` 브랜치는 어떤 때든 배포가 가능하다.
`master` 브랜치는 항상 최신의 상태이며, stable 상태로 Product에 배포되는 브랜치이다. 그리고 이 브랜치에 대해서는 업격한 *role*를 주어 사용한다. 

#### 2. 새로운 일을 시작하기 위해 브랜치를 `master`에서 딴다면 이름은 어떤일을 하는지 명확하게 작성한다.
`git flow` 와는 다르게 `feature` 브랜치나 `develop` 브랜치가 존재하지 않는다. 그렇기에 새로운 기능을 추가하거나 버그를 해결하기 위한 브랜치의 이름은 자세하게 어떤 일을 하고 있는지에 대해서 작성해주도록 하자. Github 페이지에서 보면 어떤 일들이 진행되고 있는지를 확인하기 쉽게 말이다.

#### 3. 원격지 브랜치로 수시로 push를 한다.
`git flow` 와 가장 상반되는 방식이다. 항상 원격지에 자신이 하고 있는 일들을 올려 다른 사람들도 확인할 수 있도록 해준다.
이 방법의 좋은점은 하드웨어에 문제가 발생하여 작업하던 부분이 날라가더라고 원격지에 있는 소스를 받아서 작업을 할 수 있도록 해준다.

#### 4. 피드백이나 도움이 필요할때, 그리고 머징 준비가 완료되었을때는 `pull request`를 생성한다.
`pull request` 는 코드 리뷰를 도와주는 시스템이다. 
그렇기에 이것을 이용하여 자신의 코드를 공유하고, 리뷰를 받을 수 있도록 한다. 물론 머지가 준비 완료되어 `master` 브랜치로 반영을 요구하여도 된다.

#### 5. 기능에 대한 리뷰와 사인이 끝난후 `master`로 머지한다.
곧장 product로 반영이될 기능이기에 이해관계가 연결된 사람들과 충분한 논의 이후 반영하도록 한다.

#### 6. `master`로 머지되고 푸시되었을때는 즉시 배포되어야 한다.
**GitHub Flow**의 핵심인듯한 `master`로 머지가 일어나면 `hubot`을 이용하여 자동으로 배포가 되도록 설정 해놓는다.

### 장점
* 브랜치 전략이 단순하다.
  * 처음 git을 접하는 사람에게 정말 좋은 시스템이 된다.
* Github 사이트에서 제공하는 기능을 모두 사용하여 작업을 진행한다.
* 코드리뷰를 자연스럽게 사용할 수 있다.
* CI가 필수적이며, 배포는 자동으로 진행할 수 있다.
* Github가 작업을 할때 이렇게 작업하고 있다.

### 단점
* CI와 배포 자동화가 되어있지 않은 시스템에서는 사람이 관련된 업무를 진행한다.
  * 많은 것들이 올라오기 시작하면... 그때부터는 헬이...
* 너무 간단하니... 이거 단점이 있나 싶다...

### 참고
* [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html)
* [Understanding the GitHub Flow](https://guides.github.com/introduction/flow/)
* [GitHub Flow - dogfeet](https://dogfeet.github.io/articles/2011/github-flow.html)
* [Github-flowを分かりやすく図解してみた](http://b.pyar.bz/blog/2014/01/22/github-flow/)
* [Git Flow vs Github Flow](http://lucamezzalira.com/2014/03/10/git-flow-vs-github-flow/)
* [GitHub Flow in teh Browser](https://github.com/blog/1557-github-flow-in-the-browser)

## GitLab Flow

Github에서 말하는 flow는 너무나도 간단하여 배포, 환경구성, 릴리즈, 통합에 대한 이슈를 남겨둔 것이 많았다. 그것을 보안하기위해 GitLab에서 관련 내용들을 추가적으로 덧붙여 설명한것을 일컷는다.

### Production branch with GitLab flow
![GitLab Flow Model - production branch](https://about.gitlab.com/images/git_flow/production_branch.png)

`production` 브랜치가 존재하여 커밋한 내용들을 일방적으로 디플로이를 하는 형태. GitHub에서 브랜치 하나를 더 구성하여 사용하는 이것도 조금은 간단한 구성이다.
이렇게 구성하면 배포 자동화가 되어있지않은 구성에서 어떻게 배포를 진행할 것인가에 대한 내용을 담았다. 물론 이걸로 부족하여 다음의 것도 추가되었다.

### Environment branches with GitLab flow
![GitLab Flow Model - environment branch](https://about.gitlab.com/images/git_flow/environment_branches.png)

`master`와 `production` 사이에 `pre-production`을 두어 개발한 내용을 곧장 반영하지 않고 시간을 두고 반영을 하는 것을 말한다. Staging을위한 공간을 만드는거지...

### Release branches with GitLab flow
![GitLab Flow Model - Release branch](https://about.gitlab.com/images/git_flow/release_branches.png)

`release`한 브랜치를 두고서 보안상 문제가 발생한 것이나 백포트를 위해서 작업을 할 경우, cherry-pick을 이용해서 작업을 진행할 수 도 있다. 아니면 해당 릴리즈에서 발생하는 버그들을 묶어서 수정하는 방식을 진행하며된다. 일반적으로 말하는 'upstream first' 정책이라고 보면된다.

### Merge/pull requests with GitLab flow
Pull request를 사용하는 방법이다. GitHub Flow에서 하는 방법과 동일하다. 원문은 길게 적어놨는데... 딱히...

### Issues with GitLab flow
Issue 트러커와 연결하여 사용하는 것을 말한다. 긴~~ 시간동안 작업을 할 경우, 이슈를 생성하여 작업을 진행하는 것으로... 브랜치 이름에는 이슈번호를 적어 작업중인 이슈가 어떤 것인지를 명확하게 해주는 것이 필요하다.
작업이 끝나거나 코드 공유가 필요한 시점이면 Merge/pull requsts를 보낸다. 

다적을려고 봤더니 그냥 GitLab 사용법에 대해서만 추가적으로 말하고 있어서 이쯤적고 영어로 읽자. 영어가 어렯다면... 일본어를 번역해서 읽으면 좀 더 쉽게 읽을 수 있다.

### 참고
* [GitLab Flow](https://about.gitlab.com/2014/09/29/gitlab-flow/)
* [GitLab flowから学ぶワークフローの実践](http://postd.cc/gitlab-flow/)
* [GitLab Document](http://doc.gitlab.com/ee/workflow/gitlab_flow.html)
* [GitLab Flow FTW](http://www.cloudsoftcorp.com/blog/2015/01/gitlab-flow-ftw/)
* [アプリ開発にはGitlab flowが合うと思います](http://shoma2da.hatenablog.com/entry/2015/11/04/233534)

## 끝

하... 길었다. 모든 자료는 공식적으로 첫번째로 작성된 포스트의 내용을 가져와 작성하였다. 그쪽의 내용이 가장 먼저 말한사람의 생각이 들어가 있다고 생각했기때문이다. 그리고 찾으면서 발견한 글들의 경우, 참고 사이트로 작성을 해놨으니 그것을 확인하면 될듯. 

Git flow가 편한줄 알았더니... GitHub나 GitLab을 사용하고 있다면, 굳이 Git flow가 아니더라도 괜찮겠다는 생각이드는데 딱히 OpenSource를 하는 그룹에서도 Git flow를 사용하기보다는 자신의 코드가 들어가있는 플랫폼을 가지고서 작업을 하는 경우가 많아서... 뭐. 업스트림에 작업을 할 수 있는 사람이 한정되어있으니까...

이런 방법들을 어떻게 사용해보는 것이 좋을련지를 고민해보는 것도 필요하지 않을까 한다. 간단하게 하는 방법도 있고 하니까.. 그리고 내꺼나 차근차근 구축해 나가야되는데... 

### 참고
* [Using GitHub inside a company - Gist](https://gist.github.com/nzakas/5511916)
* [GitHub workflows inside of a company](https://www.nczonline.net/blog/2013/05/21/github-workflows-inside-of-a-company/)
* [Git利用時のフローはどれを使うか](http://qiita.com/tkhm/items/cc7855d32d640687b43c)
* [The gitworkflows(7)](http://www.slideshare.net/ktateish/the-gitworkflows7-illustrated)
