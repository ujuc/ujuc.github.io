Title: [번역] JSON API Specification v1.0 (3) - Document Structure (1)
Date: 2016-07-26 02:06
Modified: 2019-03-23 16:50
Category: Develop
Tags: json, api, specification, json api, 스펙 문서, transelate
Slug: json_api_specification_v1.0_(3)_-_document_structure_(1)
Summary: JSON API에서 사용하는 문서 구조에 대해서 이야기한다. 너무 길어서 잘개 나눴다.

# 5. 문서 구조 (Document Structure)

---

이 세션에서는 미디어 타입 [`application/vnd.api+json`][application/vnd.api+json]에서 확인가능한 JSON API 문서 구조에 대해 설명합니다. JSON API 문서는 JavaScript Object Notation (JSON) [RFC7159][RFC7159]에 정의 되어있습니다.

> This section describes the structure of a JSON API document, which is identified by the media type [`application/vnd.api+json`][application/vnd.api+json]. JSON API documents are defined in JavaScript Object Notation (JSON) [RFC7159][RFC7159].

동일한 미디어 타입은 요청과 응답 문서에서 모두 사용되지만, 특정 상황에서는 한 곳에서나 다른 곳에 적용이 가능합니다. 이런 차이를 다음 내용으로 부릅니다.

> Although the same media type is used for both request and response documents, certain aspects are only applicable to one or the other. These differences are called out below.

별도로 명시하지 않는한, 사양에 정의된 객체는 임의의 추가 멤버를 포함할 수 없습니다. <**MUST NOT**> 클라이언트와 서버 구현시 이 사양에서 인식되지 않는 멤버는 무시합니다. <**MUST**>

> Unless otherwise noted, objects defined by this specification **MUST NOT** contain any additional members. Client and server implementations **MUST** ignore members not recognized by this specification.

---

> Note: 이러한 조건은 사양에 이것저것 더하고 변경을 통한 진화를 허용합니다.

> Note: These conditions allow this specification to evolve through additive changes.

[application/vnd.api+json]: http://www.iana.org/assignments/media-types/application/vnd.api+json
[RFC7159]: http://tools.ietf.org/html/rfc7159
