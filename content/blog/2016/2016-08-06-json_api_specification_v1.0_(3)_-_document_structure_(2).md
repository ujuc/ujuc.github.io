Title: [번역] JSON API Specification v1.0 (3) - Document Structure (2)
Date: 2016-08-06 14:40
Modified: 2019-03-23 16:50
Category: Develop
Tags: json, api, specification, json api, 스펙 문서, transelate
Slug: json_api_specification_v1.0_(3)_-_document_structure_(2)
Summary: 문서 구조에서 Top level에 대한 내용을 정리한다.

## 5.1. 최상위 (Top Level)

---

JSON 오브젝트는 데이터를 포함한 JSON API 요청과 응답에 대한 근본(root) 입니다. <**MUST**> 이 오브젝트를 문서의 “최상위”라 정의합니다.

> A JSON object **MUST** be at the root of every JSON API request and response containing data. This object defines a document’s “top level”.

문서에서는 최소한 다음 최상위 멤버중 하나를 포함해야 합니다 <**MUST**>:

- `data`: 문서에서 “일차 데이터”
- `errors`: [error objects][error] 에대한 배열
- `meta`: 비표준 메타 정보가 포함되어있는 [meta object][meta].

> A document **MUST** contain at least one of the following top-level members:

> - `data`: the document’s “primary data”
> - ​`errors`: an array of [error objects][error]
> - `meta`: a [meta object][meta] that contains non-standard meta-information.

`data`와 `errors` 멤버는 동일한 문서에 공존할 수 없습니다. <**MUST NOT**>

> The members `data` and `errors` **MUST NOT** coexist in the same document.

문서에서는 다음 내용과 같은 최상위 멤버가 포함될 수 있습니다 <**MAY**>:

- `jsonapi`: 서버에서 구현을 기술하는 오브젝트
- `links`: [links object][links]는 일차 데이터와 연결됩니다.
- `included`: 포함된 리소스중 각기 다르거나 일차 데이터와 관련된 [resource objects][resource]에 대한 배열.

> A document **MAY** contain any of these top-level members:

> - `jsonapi`: an object describing the server’s implementation
> - `links`: a [links object][links] related to the primary data.
> - `included`: an array of [resource objects][resource] that are related to the primary data and/or each other (“included resources”).

문서에 최상위 `data` 키가 포함되지 않은 경우, `included` 멤버 중 하나에 존재할 수 없습니다. <**MUST NOT**>

> If a document does not contain a top-level `data` key, the `included` member **MUST NOT** be present either.

최상위 [links object][links]는 다음 맴버를 포함할 수 있습니다 <**MAY**>:

- `self`: 현재 응답 문서를 생성한 [link][links].
- `related`: 일차 데이터와 리소스간 관계를 나타내는 [related resource link][related_resource_link].
- 일차 데이터에 대한 [pagination][pagination] 링크.

> The top-level [links object][links] **MAY** contain the following members:

> - `self`: the [link][links] that generated the current response document.
> - `related`: a [related resource link][related_resource_link] when the primary data represents a resource relationship.
> - [pagination][pagination] links for the primary data.

문서에서 “일차 데이터”는 요청에의해 대상이되는 자원의 컬렉션이나 자원 관계를 나타냅니다.

> The document’s “primary data” is a representation of the resource or collection of resources targeted by a request.

일차 데이터는 다음 중 하나 입니다 <**MUST**>:

- 단일 자원을 대상으로 요구하는 단일 [resource object][resource], 단일 [resource identifier object][resource_identifier_object], `null`을 나타냅니다.
- 타겟 리소스 컬렉션 요청에 대한 [resource objects][resource] 배열, [resource identifier objects][resource_identifier_object] 배열, 빈 배열 (`[]`)를 나타냅니다.

> Primary data **MUST** be either:

> - a single [resource object][resource], a single [resource identifier object][resource_identifier_object], or `null`, for requests that target single resources
> - an array of [resource objects][resource], an array of [resource identifier objects][resource_identifier_object], or an empty array (`[]`), for requests that target resource collections

예를 들어, 다음 일차 데이터는 단일 리소스 오브젝트를 나타냅니다:

> For example, the following primary data is a single resource object:

```
{
 "data": {
	"type": "articles",
	"id": "1",
	"attributes": {
	  // ... this article's attributes
	},
	"relationships": {
	  // ... this article's relationships
	}
  }
}
```

다음 일차 데이터는 동일한 리소스를 참조하는 단일 [resource identifier object][resource_identifier_object]입니다:

> The following primary data is a single [resource identifier object][resource_identifier_object] that references the same resource:

```
{
 "data": {
	"type": "articles",
	"id": "1"
  }
}
```

리소스에 대한 논리 컬렉션은 아이템 하나만 있거나 비어있더라도 배열로 표현합니다. <**MUST**>

> A logical collection of resources **MUST** be represented as an array, even if it only contains one item or is empty.

[error]: http://jsonapi.org/format/#errors
[meta]: http://jsonapi.org/format/#document-meta
[links]: http://jsonapi.org/format/#document-links
[resource]: http://jsonapi.org/format/#document-resource-objects
[related_resource_link]: http://jsonapi.org/format/#document-resource-object-related-resource-links
[pagination]: http://jsonapi.org/format/#fetching-pagination
[resource_identifier_object]: http://jsonapi.org/format/#document-resource-identifier-objects
