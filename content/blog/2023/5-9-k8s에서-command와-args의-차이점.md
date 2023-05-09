Title: k8s에서 command와 args의 차이점
Date: 2023-05-09 22:03:30
Modified: 2023-05-09 22:03:30
Category: Operation
Tags: k8s, docker
Slug: k8s에서-command와-args의-차이점
Summary: k8s에서 command랑 args 가 뭐가 다른지 정리한다. Docker에도 비슷한게 있다네...?

어플리케이션에 데이터를 주입하는 내용중 하나인 [컨테이너에 command 와 args 정의하기](https://kubernetes.io/ko/docs/tasks/inject-data-application/define-command-argument-container/).

다른건 아니었다.

Dockerfile에서 다음과 같은 설정이 되어있었다.

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

그리고 `app.py`에서는 `profile` 인자를 받도록 되어있어서 컨테이너가 실행이 안된더라.

외부에서 인자를 넣어줘야하는 권한이 필요해서 위에서 말한 문서를 이용해서 작업을 하였다.

그런데...

나 잘못 사용한거 같다.?

잘읽어보니 `command` 필드는 Dockerfile에서 `ENTRYPOINT`란다.
가방끊이 짧아 다시 검색...
`ENTRYPOINT`는 컨테이너가 실행될때 무조건 실행되는 명령어를 작성하는 부분.
그렇기에 항상 특정 명령어를 실행하여야 할때는 `ENTRYPOINT`를 사용.

그럼 `args` 필드는? Dockerfile에서 `CMD`에 대응된다고 한다.
매번 검색...
`CMD`는 컨테이너 실행시 기본 값으로 동작할 내용을 입력.
그렇기에 컨테이너 실행시 인자를 넣어주고 싶을때는 `CMD`를 이용하여 컨테이너 생성.

`ENTRYPOINT`랑 `CMD`를 같이 사용할떄는 다음과 같이 사용하는게 좋은듯.

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--profile", "dev"]
```

k8s 필드에서는 다음과 같이 사용.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
spec:
  containers:
  - name: command-demo-container
    image: python
    command: ["python", "app.py"]
    args: ["--profile", "${ENV}"]
```

요로코롬 정리.
