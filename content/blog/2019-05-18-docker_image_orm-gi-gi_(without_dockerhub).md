Title: Docker Image 옮기기 (without DockerHub)
Date: 2019-05-18 11:59:45
Category: Operation
Tags: docker, docker image
Slug: docker_image_orm-gi-gi_(without_dockerhub)
Summary: 반강제 폐쇄망에 이미지를 올리자.

외부로 나가서는 안되는 Docker 이미지를 만들게 되었다. 그러다보니 Docker Hub를 사용하거나 AWS ECR을 사용하는건 제외. 

개발 과정에서 실제 OS에서 작동하는지 확인을 위한것이라 올리고 인증하고 귀찮다.

뭘로 검색했는지는 기억이 없지만 다음과 같은 글을 확인했고, 다음과 같은 명령을 사용하면 인터넷이나 Docker 레포없이 작업이 가능하다.

* 출처: [How to copy Docker images from one host to another without using a repository](https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository)

우선 로컬에서 Docker 이미지를 빌드한다. 명령어는 알꺼니 넘어가자.

다름 명령을 이용해서 tar 파일을 만들자.

```shell
docker save -o <path for generated tar file> <imange name>:<tag>
```

만들어진 tar 파일을 원하는 곳에 업로드 시킨다.

이제 올린 노드에서 사용할 수 있도록 이미지를 docker에 등록해주면 끝.

```shell
docker load -i <path to image tar file>
```

### 참고

* [docker save](https://docs.docker.com/engine/reference/commandline/save/)
* [docker load](https://docs.docker.com/engine/reference/commandline/load/)
