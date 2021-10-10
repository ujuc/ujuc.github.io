Title: minikube로 docker를 대신해볼까?
Date: 2021-10-10 09:50:45
Modified: 2021-10-10 09:50:45
Category: Operation
Tags: minikube, kube, docker
Slug: minikube로-docker를-대신해볼까
Summary: minikube로 docker에서 벗어날까한다.

전에 docker가 유료화로 바뀐다고 한뒤 뭔가 docker 대신으로 할 것을 찾는게 유행인듯.

이것저것 해보다가 minikube로 작업하는게 좋다는 소릴 들었고 세팅을 하긴했는데... `docker-compose` 항목을 어떻게 바꾸지 하다가 검색에 들어갔다.

[minikube로 docker와 docker-compose를 대체하기](https://novemberde.github.io/post/2021/09/02/podman-minikube/)

역시 누군가 먼저 해주셨고. 그걸보고 있는데...

생각보다 `minikube`는 말그대로 `docker-desktop`이고 `kubectl`을 이용해서 작업을 해야하는구나... 명령어를 찾아서 작업할 수 있게 구성을 하고 손에 익혀나가면 좋을듯.

그런데 이미지 빌드는 어떻게 하는걸까?? `docker-compose` 처럼 만들면 이미지가 추가되려나...
테스트로 진행한 airflow에 있는 `docker-compose`는 복잡해서 못하는듯.
사람이 생성을 해줘야 하는 부분이라 `kompose` 패키지를 좀더 보고 한번 정리를 해야할꺼같다.
