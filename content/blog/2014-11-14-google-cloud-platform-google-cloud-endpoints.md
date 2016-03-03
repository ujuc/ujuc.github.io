Title: [Google Cloud Platfrom] Google Cloud Endpoints
Date: 2014-11-14 15:05
Modified: 2016-03-01 00:38
Category: Devlop
Tags: google, cloud, gcp, google cloud platform, google cloud endpoint
Slug: google-cloud-platform-google-cloud-endpoints
Summary: Google Cloud Endpoints 간략하게 확인하기.

* App의 API를 구성하기 쉽도록 제공하는 서비스
* Remote Procedure Call(RPC)를 이용하여 작업을 진행할 수 있도록 구성.

## 사용

* 2가지 방법이 존재
    * RPC의 `message` 클래스를 이용하는 방법.
    * RPC를 통하지 않고 직접 작업하는 방법. 
    * 사용은 RPC를 통하지 않는 방법이 간단하긴하다.

## 예제

1. [appengine-endpoints-helloendpoints-python](https://github.com/GoogleCloudPlatform/appengine-endpoints-helloendpoints-python)
    * RPC `message` 클래스를 이용하도록 되어있음.
    * 랩핑하는 것에 대한 내용이 포함.
2. [appengine-endpoints-angular-todos-python](https://github.com/GoogleCloudPlatform/appengine-endpoints-angular-todos-python)
    * RPC `message` 클래스를 사용하지 않음.
    * Angular.js를 이용하도록 예제가 되어있어서 확인해보면 될듯함.
3. [appengine-endpoints-tictactoe-python](https://github.com/GoogleCloudPlatform/appengine-endpoints-tictactoe-python)
    * 게임 예제로 보이나 아직 테스트해보지 않음.

## 필요 패키지

* [endpoints-proto-datastore](https://github.com/GoogleCloudPlatform/endpoints-proto-datastore)
* ProtoRPC 를 사용하지 않아도 된다고 함. [^1]
* 지금은 NDB만 지원. 추후 DB지원은 모르겠음.
* DB를 사용하려면 전부 분해하고 설정하는 것이 필요할 것으로 보임.

## API 구성

* `/_ah/spi/.*` URL은 `app.yaml` 파일에 하나만 가능함.
* 여러 API를 사용하고 싶으면 `main.py` 에 일반 예제들처럼 API클래스를 생성하고 다음과 같이 설정해주면됨.

        :::python
        # app.yaml
        - url: /_ah/spi/.*
          script: main.application

        # main.py
        application = endpoints.api_server([App1_api, App2_api, ...])

* 하나의 API에 여러 클래스를 두고 싶다면 아래의 방법으로 구성

        :::python
        # API를 종류별로 나눔 
        test_api_v1 = endpoints.api(name='test', version='v1.0')
        test1_api_v1 = endpoints.api(name='test1', version='v1.0')
      
        # API를 처리할 Class구성
        @test_api_v1.api_class(resource_name='hello')
        class Hello(remote.Service):
            pass
  
        @test_api_v1.api_class(resource_name='bye')
        class Bye(remote.Service):
            pass
  
        @test1_api_v1.api_class(resource_name='todo')
        class Todo(remote.Service):
            pass

        @test1_api_v1.api_class(resource_name='plan')
        class Plan(remote.Service):
            pass

        application = endpoints.api_server([Hello, Bye, Todo, Plan])

## API 등록확인

* `project-id.appspot.com/_ah/api/explorer` 로 접근하여 확인.
* 업로드되어 표시되는 시간이 오래걸리니(최소 5분은 걸리는듯.) 올라갔는지 확인을 하려면 Google Developers Console에서 로그로 확인하면된다.
* 올라갔다면 아래와 같이 표시된다.

        :::shell
        https://1-dot-project-id.appspot.com/_ah/api/test@v1.0 Saved
        https://1-dot-project-id.appspot.com/_ah/api/test1@v1.0 Saved

[^1]: http://endpoints-proto-datastore.appspot.com/
