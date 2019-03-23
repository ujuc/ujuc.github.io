Title: [번역] JSON API Specification v1.0 (2)
Date: 2016-07-16 14:53
Modified: 2019-03-23 16:50
Category: Develop
Tags: json, api, specification, json api, 스펙 문서, transelate
Slug: json_api_specification_v1.0_(2)
Summary: JSON API를 사용하는 서버와 클라이언트에서 처리를 해야되는 것들에 대해서 이야기한다.

JSON API를 사용하는 서버와 클르이언트에서 처리를 해야되는 것들에 대해서 이야기한다.

---

# 4. 컨텐츠 처리 (Content Negotiation)

---

## 클라이언트 의무 사항 (Client Responsibilities)

클라이언트는 해더에 `Content-Type: application/vnd.api+json`를 포함하고 다른 미디어 타입 매개변수를 포함하지 않는 요청 문서를 생성하여 모든 JSON API 데이터를 보내야 합니다. <**MUST**>

> Clients **MUST** send all JSON API data in request documents with the header `Content-Type: application/vnd.api+json` without any media type parameters.

클라이언트는 `Accept` 해더에 작성된 미디어 타입 매개변수 중 맨마지막 하나를 지정하여 JSON API 미디어 타입을 포함해야 합니다. <**MUST**>

> Clients that include the JSON API media type in their `Accept` header **MUST** specify the media type there at least once without any media type parameters.

클라이언트는 응답 문서에 대한 `Content-Type` 해더에서 받은 `application/vnd.api+json` 미디어 타입에대해 어떠한 매개변수라도 무시합니다. <**MUST**>

> Clients **MUST** ignore any parameters for the `application/vnd.api+json` media type received in the `Content-Type` header of response documents.

---

## 서버 의무 사항 (Server Responsibilities)

서버는 모든 미디어 타입 매개 변수를 지정하지 않고서 해더 `Content-Type: application/vnd.api+json`​와 함께 응답 문서에 모든 JSON API 데이터를 전송합니다. <**MUST**>

> Servers **MUST** send all JSON API data in response documents with the header `Content-Type: application/vnd.api+json` without any media type parameters.

서버는 요청이 임의의 미디어 타입 매개변수를 가지는 헤더 `Content-Type: application/vnd.api+json`로 지정하면 `415 Unsupported Media Type` 상태 코드로 응답합니다. <**MUST**>

> Servers **MUST** respond with a `415 Unsupported Media Type` status code if a request specifies the header `Content-Type: application/vnd.api+json` with any media type parameters.

서버는 요청한 `Accept` 해더에 JSON API 미디어 타입을 포함하고 있으며 해당 미디어 타입에대한 모든 인스턴스에서 미디어 타입 매개변수가 수정된 경우, `406 Not Acceptable` 상태 코드로 응답합니다. <**MUST**>

> Servers **MUST** respond with a `406 Not Acceptable` status code if a request’s `Accept` header contains the JSON API media type and all instances of that media type are modified with media type parameters.

> Note: 컨텐츠 처리 요구사항은 향후 버전에서 확장된 처리 방법과 버전 관리를 위한 미디어 타입 매개 변수를 사용할 수 있도록 존재합니다.

> Note: The content negotiation requirements exist to allow future versions of this specification to use media type parameters for extension negotiation and versioning.

