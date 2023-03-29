Title: AWS RDS Proxy 간단하게 보기
Date: 2020-07-11 11:01:43
Modified: 2020-07-11 11:01:43
Category: Cloud
Tags: rds, aws, rds proxy, cloud
Slug: aws-rds-proxy-gan-dan-ha-ge-bo-gi
Summary: AWS RDS Proxy를 간략하게 정리해보자.

회사에서 사용을 하자고 말이 나와서 진짜 간략하게 정리한걸 조금 정리하는 겸. 만들었는데 블로그도 쓸겸.

### 설명서

[Aurora User Guide - RDS proxy](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html)

### 간략 설명

- 대량의 컨넥션이 이뤄져서 컨넥션 풀 관리가 힘들다...
- 우리는 DB를 엄청 크게 쓰고 있어요!
- 하는데만 쓰자...

### 조금 자세하게

DB와 애플리케이션 사이에 존재하여 DB 컨넥션에 대한 처리를 해준다.

원래는 프로그램상에서 컨넥션 풀을 생성하여 풀 관리를 하면서 작업을 진행해야 하나. 몇몇 언어나 일반 사용자들이 컨넥션 풀에 대해서 인지를 못하고 제대로 사용하고 있지 못하다. 그것을 proxy에서 일정한 컨넥션 풀을 생성하고 연결을 할 수 있도록 도와 주게 된다.

IAM과 AWS Secrets Manager 를 이용하여 DB 연결하는 비밀번호를 암호화하여 작업할 수 있다.
