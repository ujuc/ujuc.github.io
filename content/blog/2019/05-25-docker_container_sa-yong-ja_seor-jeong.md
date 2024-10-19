Title: Docker container 사용자 설정
Date: 2019-05-25 12:38:45
Category: Develop
Tags: docker, container, ubuntu, linux
Slug: docker_container_sa-yong-ja_seor-jeong
Summary: Docker container를 사용할때 발생한 에러에 대해서 작성하였다.

회사에서 개발한 소스들을 Docker 이미지를 만들어서 ubuntu 18.04에서 작업을 할 수 있도록 구성을 했다.

인프라 작업을 하고 있지만, OS나 인프라는 매번 내가 생각했던 대로 잘 안 해준다.

이번에도 에러가 났다...

### 문제

실행중인 Docker container에 접속해서 그 폴더를 사용하는 스크립트를 만든 다음 실행하였더니 Docker container에서 mount 해서 사용하는 볼륨 권한 문제.

폴더에 접근할 방법이 없단다.

Docker container에서 사용하는 사용자는 root. 이 root는 패이크 루트라서 GID는 호스트의 root와 동일하지만, container에서만 root이지 실제로 호스트에서는 제대로 작동하지 않는다.

해당 내용을 다른 분들에게 물었더니 그 폴더 권한을 `0777` 로 변경해서 작업을 하라고 해서 기각.

어떤 넘이 어떻게 들어올 줄 모르는데 모든 걸 열라니!!!

### 해결

그래서 딴짓을 했다.

우선 호스트에서 필요한 dir을 생성했다. → 그러면 해당 폴더의 `gid`와 `uid`는 호스트 사용자의 `uid/gid`를 사용하게 된다.

그리고 Docker에게서 새로운 사용자를 만들고 그에게 호스트 사용자와 동일한 `gid/uid` 를 가질 수 있도록 하였다.

이건 Ubuntu에 하나의 유저만 있는 상태에서 가능한 설정이다. 만약 호스트에서 여러 사용자를 만들어서 사용한다면, 이 설정은 힘들다. `gid/uid`가 다를 수 있다. Container 에서의 사용자는 root이외에 `www-data` 와 같은 시스템 User 등급만 있지 실제 User 등급은 없어서 `gid : 1000`, `uid : 1000`을 가져가게된다.

다른 사용자가 있다면... 다른 작업을 하도록 하자.

뒤지다 뒤지다 발견한 하나의 글.

*[How to set user of Docker container](https://codeyarns.com/2017/07/21/how-to-set-user-of-docker-container/)*

- 이 글의 문제점은 Docker다. 난 Docker-compose를 사용하고 있어서 다른 작업이 필요했다.
- 내 생각에는 이 옵션에 대한 Docker-compose 옵션이 있을 꺼라 생각하는데. 나중에 다른 작업할때 찾아봐야겠다.

