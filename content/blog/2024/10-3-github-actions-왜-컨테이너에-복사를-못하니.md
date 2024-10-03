Title: [GitHub Actions] 왜 컨테이너에 복사를 못하니?
Date: 2024-10-03 09:40:58
Modified: 2024-10-03 09:40:58
Category: Operation
Tags: GitHub, Actions, docker, container, ci, cd
Slug: github-actions-왜-컨테이너에-복사를-못하니
Summary: [docker/build-push-action][1]를 이용해서 컨테이너 이미지를 생성하도록 해놨는데. 왜 runner에서 생성한 파일을 가져오지 못하지?

회사에서 CI/CD 환경으로 GitHub Actions를 이용하여 컨테이너 이미지를 만들도록 구현을 해뒀다.

컨테이너를 만들때 사용한 Action은 [docker/build-push-action][1]. Docker 에서 `docker buildx build`를 명령어를 한번 랩핑 해서 사용할 수 있도록 해놓은 Action 인데...
이게 multi-stage 빌드로 이미지를 빌드하게되면 잘 가져오던 파일을 runner에서 직접 빌드하여 복사하려고 하면 안되는 문제점을 확인해서 왜 안되는지에 대해서 정리하려고 한다.

또 삽질하기 싫다.

시작은 이게 아니라 GitHub Cache 를 사용해서 빌드시간 줄이도록 해놨는데 컨테이너 레이어로 cache 가 남아서 용량 제한(10G)에 도달했던걸 해결하고 있었는데 ... ㅠ.ㅠ

---
[TOC]

# 하고 싶었던 작업

- Workflow

```yaml
- uses: actions/checkout@v4

- run: npm i && npm run build

- uses: docker/build-push-action@v6
```

- Dockerfile

```dockerfile
WORKDIR /app

COPY ./node_modules ./node_modules
```

# 결과

```
ERROR: failed to calculate checksum 
  of ref e029::mclu: "/node_modules": not found
```

빌드된 `node_modules` 폴더를 찾을 수 없다!

# 뭐가 문젠지 보자.

## Action Job 로그

- [actions/checkout][1]

```
## Run actions/checkout@v4
Temporarily overriding 
  HOME='/home/runner/work/_temp/4d270f53-51a0-434e-aa52-9f4e95bf278a' 
  before making global git config changes
```

- [docker/build-push-action][2]

```
## Run docker/build-push-action@v6
/usr/bin/docker buildx build 
    --cache-from type=gha --cache-to type=gha,mode=max 
    --iidfile /home/runner/work/_temp/docker-actions-toolkit-cB7XtZ/build-iidfile-2d520664a2.txt 
    --platform linux/amd64 
    --attest type=provenance,mode=min,inline-only=true,builder-id= 
    --secret id=GIT_AUTH_TOKEN,src=/home/runner/work/_temp/docker-actions-toolkit-cB7XtZ/tmp-1978-917X1YS1aV1W 
    --tag bd6e 
    --metadata-file /home/runner/work/_temp/docker-actions-toolkit-cB7XtZ/build-metadata-74e703f218.json 
    --push 
```

*싸늘하다.* 왜 두개의 work 폴더가 다르지...?
[actions/checkout][1]에서는 `runner/work/_temp/4d270f53-*` 이라는 디렉토리에서 코드를 옮겨다 놨는데 [build-push-action][2]는 `runner/work/_temp/docker-actions-toolkit-cB7XtZ` 로 다시 코드를 땡겨서 넣어뒀다.

하 뭐가 잘못된걸까 [build-push-action][2]의 `README`에서 확인해보자

## [docker/build-push-action][2] - Git context

> By default, this action uses the [Git context][3], so you don't need to use the `[actions/checkout][1]` action to check out the repository as this will be done directly by [BuildKit](https://github.com/moby/buildkit).

위의 내용으로 나의 삽질이 왜 하게되었는지에 대해서 보여지는데... [build-push-action][2]의 경우, [actions/checkout][1] 을 통해서 코드를 받아오지 않더라도 동작하도록 구성해놨다고 한다.

해당 부위에대한 문서 수정한 가장 최근 일자가 2년전이니... 내가 채크하지 못한걸로...

# 그래서

- **매번 사용할때마다 읽지만, 다시금 `README`를 잘읽어보자.**
- 일부 엑션은 동작중에 checkout을 하는 경우가 있구나...


왜 넣는거냐 도대체...


[1]: https://github.com/actions/checkout/
[2]: https://github.com/docker/build-push-action
[3]: https://docs.docker.com/engine/reference/commandline/build/#git-repositories
