Title: [번역] JSON API Specification v1.0 (3) - Document Structure (4)
Date: 2016-09-17 20:55
Modified: 2018-03-23 16:50
Category: Develop
Tags: json, api, specification, json api, 스펙 문서, transelate
Slug: json_api_specification_v1.0_(3)_-_document_structure_(4)
Summary: 문서 구조에서 리소스 오브젝트에 대한 내용을 정리한다. 검증, 필드 부분.

### 검증 (Identification)

모든 [resource object][resource_objects]는 `id` 멤버와 `type` 멤버는 포함하고 있어야 합니다. <**MUST**> `id`와 `type` 멤버 값은 문자열이어야 합니다. <**MUST**>

> Every [resource object][resource_objects] **MUST** contain an `id` member and a `type` member. The values of the `id` and `type` members **MUST** be strings.

주어진 API에서 각 리소스 오브젝트에서 `type`, `id` 쌍은 반드시 하나인 고유한 리소스임을 증명해야 합니다. <**MUST**> (서버 한 대이거나 단일 작업을 하는 여러 서버에서 제어되는 URI 집합으로 API를 구성합니다.)

> Within a given API, each resource object’s `type` and `id` pair **MUST** identify a single, unique resource. (The set of URIs controlled by a server, or multiple servers acting as one, constitute an API.)

`type` 멤버는 공통된 속성과 관계를 공유하는 [resource objects][resource_objects]를 설명하는 데 사용됩니다.

> The `type` member is used to describe [resource objects][resource_objects] that share common attributes and relationships.

`type` 멤버 값은 [member names][member_names]와 같은 제약에 따라야 합니다. <**MUST**>

> The values of `type` members **MUST** adhere to the same constraints as [member names][member_names].

> Note: 이 스펙은 inflection 법칙에 얽매이지 않습니다. 또한 `type` 값은 복수이거나 단수일 수 있습니다. 그러나 같은 값이 구현된 API 전체에서 일관되게 사용되어야 합니다.

> Note: This spec is agnostic about inflection rules, so the value of `type` can be either plural or singular. However, the same value should be used consistently throughout an implementation.

---

### 필드 (Fields)

리소스 오브젝트에서 [attributes][resource_object_attributes]과 [relationships][resource_object_relationships]는 “[fields][resource_object_field]”로 묶어서 부릅니다.

> A resource object’s [attributes][resource_object_attributes] and its [relationships][resource_object_relationships] are collectively called its “[fields][resource_object_field]”.

[resource object][resource_objects] 필드는 반드시 각기 다른 공통된 네임스페이스, `type`, `id`를 공유해야합니다. <**MUST**> 다른 말로는, 리소스는 동일한 이름으로 속성 값과 관계를 가질 수 없으나 `type`이나 `id`에대한 속성이나 관계는 동일한 이름을 가질 수 있습니다.

> Fields for a [resource object][resource_objects] **MUST** share a common namespace with each other and with `type` and `id`. In other words, a resource can not have an attribute and relationship with the same name, nor can it have an attribute or relationship named `type` or `id`.

[resource_object_attributes]: http://jsonapi.org/format/#document-resource-object-attributes
[resource_object_relationships]: http://jsonapi.org/format/#document-resource-object-relationships
[resource_object_field]: http://jsonapi.org/format/#document-resource-object-fields
[resource_objects]: http://jsonapi.org/format/#document-resource-objects
[member_names]: http://jsonapi.org/format/#document-member-names