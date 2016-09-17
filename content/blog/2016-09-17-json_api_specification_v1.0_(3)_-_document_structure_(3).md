Title: JSON API Specification v1.0 (3) - Document Structure (3)
Date: 2016-09-17 20:46
Category: Develop
Tags: json, api, specification, json api, 스펙 문서
Slug: json_api_specification_v1.0_(3)_-_document_structure_(3)
Summary: 문서 구조에서 리소스 오브젝트에 대한 내용을 정리한다.

## 5.2. 리소스 오브젝트 (Resource Objects)

---

“리소스 오브젝트”는 자원을 나타내는 데 사용되는 JSON API에 표시됩니다.

> “Resource objects” appear in a JSON API document to represent resources.

리소스 오브젝트는 적어도 다음 최상위 멤버가 포함되어 있어야 합니다. <**MUST**> :

- `id`
- `type`

> A resource object **MUST** contain at least the following top-level members:

> - `id`
> - `type`

예외: 리소스 오브젝트가 클라이언트에서 고안되고, 서버에서 생성된 새로운 리소스를 나타낼 때는 `id` 멤버는 필요하지 않습니다.

> Exception: The `id` member is not required when the resource object originates at the client and represents a new resource to be created on the server.

추가로 리소스 오브젝트는 다음 최상위 멤버 중 하나가 포함될 수도 있습니다. <**MAY**> :

- `attributes`: [attributes object][resource_object_attributes]는 리소스 데이터 일부를 나타냅니다.
- `relationships`: [relationships object][resource_object_relationships]는 리소스와 다른 JSON API 리소스간 관계를 표현합니다.
- `links`: [links object][links]는 리소스와 관련된 링크를 포함합니다.
- `meta`: [meta object][meta]는 속성과 관계로는 나타낼 수 없는 리소스에 대한 비표준 메타 정보를 포함합니다.

> In addition, a resource object **MAY** contain any of these top-level members:

> - `attributes`: an [attributes object][resource_object_attributes] representing some of the resource’s data.
> - `relationships`: a [relationships object][resource_object_relationships] describing relationships between the resource and other JSON API resources.
> - `links`: a [links object][links] containing links related to the resource.
> - `meta`: a [meta object][meta] containing non-standard meta-information about a resource that can not be represented as an attribute or relationship.

여기서 아티클(즉, “articles” 타입)이 문서에 표시될 수 있습니다. 그 방법은 다음과 같습니다:

> Here’s how an article (i.e. a resource of type “articles”) might appear in a document:

```
// ...
{
 "type": "articles",
  "id": "1",
  "attributes": {
	"title": "Rails is Omakase"
  },
  "relationships": {
	"author": {
	  "links": {
		"self": "/articles/1/relationships/author",
		"related": "/articles/1/author"
	  },
	  "data": { "type": "people", "id": "9" }
	}
  }
}
	// ...
```

[resource_object_attributes]: http://jsonapi.org/format/#document-resource-object-attributes
[resource_object_relationships]: http://jsonapi.org/format/#document-resource-object-relationships
[links]: http://jsonapi.org/format/#document-links
[meta]: http://jsonapi.org/format/#document-meta
