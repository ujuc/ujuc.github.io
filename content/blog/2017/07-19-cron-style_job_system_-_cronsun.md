Title: Cron-Style Job System - cronsun
Date: 2017-07-19 17:08:01
Category: Software
Tags: go, cron, job system
Slug: cron-style_job_system_-_cronsun
Summary: Go 메일링을 보다가 cron과 비슷한 서비스라 말하기에 확인.

* [Github](https://github.com/shunfei/cronsun)
* Lang: Golang

분산 cron 스타일 잡 시스템이라고 한다. 대략적인 구성을 보고 싶어서 작성하는 것이니 만큼... 설치랑 해당 내용만 작성해두고 언제가 쓸일 있을때 사용 후기나 적어야겠다.

## 아키텍쳐

```
                                         [web]
                                           +
                                           |
                                 +---------+----------------+
                                 |                          |
(Add/Delete/Update/Execute jobs) |                          | (Query job exec result)
                                 +                          +
                               [etcd]                   [MongoDB]
                                 +                          ^
                      +----------------------+              |
                      +          +           +              |
                   [node.1]   [node.2]   [node.n]           |
                      +          +           +              |
                      +----------------------+              |
                                 |                          |
                                 |                          |
             (Job execute fail)  |   (Job execute result)   |
                                 |                          |
 [Send Mail]<--------------------+--------------------------+
```

Job을 매니징하고 등록하는 부분을 Web으로 구성해둬서 접근이 쉽게 되어있고, etcd를 이용해서 워커들의 작동을 정리하고, MongoDB에다가 job 실행 결과에 대한 부분을 저장해두는 방식으로 보여짐.
노드는 여러개를 사용할 수 있는 것인지... 보기로는 그렇게 되어있긴한데.. 뭐 이건 코드도 같이 봐야될듯함.


## 빌드

```shell
go get -u github.com/shunfei/cronsun
cd $GOPATH/src/github.com/shunfei/cronsun
sh build.sh
```

## 실행

1. MongoDB, etcd3 설치
2. `conf` 폴더에 있는 config 수정
  * 샘플은 `conf/files` 에 항목별로 존재한다. 확인이 필요.
3. Node 실행: `./cronnode -conf conf/base.json`
4. 웹서버 실행: `./cronweb -conf conf/base.json`
5. 접속은 `http://127.0.0.1:7079/ui/`
