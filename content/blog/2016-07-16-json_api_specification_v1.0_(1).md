Title: JSON API Specification v1.0 (1)
Date: 2016-07-16 12:08
Category: Develop
Tags: json, api, specification, json api, 스팩 문서
Slug: json_api_specification_v1.0_(1)
Summary: API 쪽 문서를 볼일 이있어서 JSON API를 확인하였다. 그것에 대한 기능 문서 번역본. 나중에 보고 해야지...

JSON API 문서이다. 해당 문서는 [여기서](http://jsonapi.org/format/) 확인이 가능하다. 라이센스는[퍼블릭 도메인 라이센스](https://creativecommons.org/publicdomain/zero/1.0/).

나중에 번역한 것이 도움이 되길 바라며...

---

# 1. 문서 상태 (Status)

이 페이지는 JSON API 마지막으로 공개된 버전 내용을 담고 있습니다. 현재버전은 1.0 입니뀋¤. JSON API 새로운 버전에서는 **이전 문서와 호환을 위해** 삭제하지 않고, 오로지 추가만 됩니다. 추가 사항들은 우리 [discussion forum](http://discuss.jsonapi.org/)에서 확인할수 있습니다.
스펙 문서상 에러를 발견하거나, 구현한다면 이슈를 등록하거나 PR을 [GitHub repository](https://github.com/json-api/json-api)로 해주면 됩니다.

This page represents the latest published version of JSON API, which is currently version 1.0. New versions of JSON API **will always be backwards compatible** using a never remove, only add strategy. Additions can be proposed in our [discussion forum](http://discuss.jsonapi.org/).
If you catch an error in the specification’s text, or if you write an implementation, please let us know by opening an issue or pull request at our [GitHub repository](https://github.com/json-api/json-api).

---

# 2. 소개 (Introduction)

JSON API는 클라이언트에서 요구하는 리소스를 제공하거나 수정하는 것에 대해 서버가 어떻게 대응 할 것인지에 대한 사양입니다.
JSON API는 클라이언트와 서버사이에서 전송되는 데이터 총량과 요청 수에대해 최소화하도록 설계되었습니다. 가독성, 유연성, 검색 기능을 잃지 않고 효율성을 높일수 있습니다.
JSON API는 데이터를 변경하여 JSON API 미디어 타입 (application/vnd.api+json) 을 사용하게 하는것이 필요합니다.

JSON API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests.
JSON API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is achieved without compromising readability, flexibility, or discoverability.
JSON API requires use of the JSON API media type ([application/vnd.api+json](http://www.iana.org/assignments/media-types/application/vnd.api+json)) for exchanging data.

---

# 3. 규칙 (Conventions)

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119) ([RFC 2119 한국어 번역](http://techhtml.github.io/rfc/RFC2119.html)).

