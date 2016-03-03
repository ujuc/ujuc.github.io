Title: [Google App Engine] NDB - Properties
Date: 2014-11-10 18:05
Modified: 2016-03-03 21:47
Category: Devlop
Tags: google, cloud, gcp, google cloud platform, ndb
Slug: google-app-engine-ndb-properties
Summary: NDB 문서를 번역해놓은 것.

* 관련해서 한글로되 문서가 없어서 [2014/10/27일자 문서][ndb-properties]를 가지고서 정리하였다.

## 소개
`Model`에서 사용할 수 있는 데이터 모델을 말한다. 모델 타입으로 생각하면 쉽겠다. 어려울 것도 없다만.

## Type
| Property type | 설명 |
| ------------- | --- |
| `IntegerProperty` | 64-bit signed 정수 값 |
| `FloatProperty` | Double-precision 부동 소수점 숫자 값 |
| `BooleanProperty` | Boolean 값 |
| `StringProperty` | 유니코드 스트링 값, 500자까지 가능, 인덱스 가능 |
| `TextProperty` | 유니코드 스트링 값, 길이 제한 없음, 인덱스 기능 없음 |
| `BlobProperty` | 해석되지 않은 (Uninterpreted) 바이트 스트링, `indexed=True`로 설정하게되면 500자로 제한, 인덱스 가능. <br>하지만 `False`(기본 값)으로 설정하게 되면, 길이 제한 없으며, 인덱스 기능 없음. (추가 속성으로 [`compressed`][compressed]를 사용할 수 있음) |
| `DateTimeProperty` | 날짜와 시간 (자세한 내용은 [Date and Time Properties][date-time]에서 확인) |
| `DateProperty` | 날짜 (자세한 내용은 [Date and Time Properties][date-time]에서 확인) |
| `TimeProperty` | 시간 (자세한 내용은 [Date and Time Propertyes][date-time]에서 확인) |
| `GeoPtProperty` | 지리적 정보데이터를 입력 받음. `ndb.GeoPt`객체인데, `lat`, `lon` 값(둘다 부동소수점으로 표기)을 가지고서 작업을 진행.<br>예, `ndb.GeoPt(52.37, 4.88)` or `ndb.GeoPt("52.37", "4.88")`형식.<br>([`db.GeoPt`][db-geopt]와 동일한 객체.) |
| `KeyProperty` | Datastore key 값<br>선택 키워드로 kind=_kind_ 형식으로 나오며, 할당된 키는 항상 kind를 지정해야함.<br>문자열이거나, 모델 클레스가 될수도 있음. |
| `BlobKeyProperty` | `Blobstore` 키 값<br>이전 DB API의 `BlobReferenceProperty`에 해당.<br>`BlobInfo`대신 `BlobKey`로 속성 값을 사용. `BlobInfo(blobkey)`를 사용하여 `BlobInfo`를 구성할 수 있긴함. |
| `UserProperty` | 유저 객체.<br>Google의 사용자 로그인으로 관련된 내용을 저장하여 사용할때 쓴다. |
| `StructuredProperty` | 하나의 kind 내부에 다른 모델을 추가하는 것.<br>`C`의 구조체와 비슷하다고 생각하자.<br>여러번 중복이 가능하고 값을 불러오게되면 JSON방식으로 불러오는 것이 편하다.<br>자세한 내용은 [Structured Properties][structuredproperties]에서 확인 |
| `LocalStructuredProperty` | `StructuredProperty`와 비슷하게 사용할 수 있으나, 인덱싱이 안된다. 자세한 내용은 [Structured Properties][structuredproperties]에서 확인.<br>추가 속성: [`compressed`][compressed] |
| `JsonProperty` | 파이썬 객체(리스트, 딕셔너리, 스트링) 값을 파이썬 `json`모듈을 이용하여 직열화함.<br>Datastore에서는 blob로 json 직렬화하여 저장.<br>인덱스 안됨.<br>추가 속성: [`compressed`][compressed] |
| `PickleProperty` | 파이썬 객체(리스트, 딕셔너리, 스트링) 값을 파이썬 pickle 프로토콜을 이용하여 직열화함.<br>Datastore에서는 blob로 pickle 직렬화하여 저장.<br>인덱스 안됨.<br>추가 속성: [`compressed`][compressed] |
| `GenericProperty` | 기본 값.<br>[Expando][expando]클래스에서 주로 사용되지만, 명시적으로 사용하기도함.<br>어떤 형식으로도 가능. (`int`, `long`, `float`, `bool`, `str`, `unicode`, `datetime`, `Key`, `BlobKey`, `GeoPt`, `User`, `None`) |
| `ComputeProperty` | 사용자가 정의한 함수에서 계산 값들을 처리하여 저장.<br>자세한 내용은 [Computed Properties][computeproperty] |

* `compressed` 옵션: `True`로 설정시, gzip으로 압축하여 디스크에 저장함. 이때 CPU 인/디코딩하는데 IO를 사용을 함. 

## Property Options
| Argument | Type | Default | 설명 |
| -------- | ---- | ------- | --- |
| `indexed` | `bool` | 사용하는 것만 `True` | `False`로 설정시 쿼리는 불가능해지나 쓰기 속도가 높아짐.<br>다 사용가능한건 아님.<br>인덱스 안하는게 인덱스하는 것보다 write 코스트가 적음. |
| `repeated` | `bool` | `False` | 파이썬 리스트 형식으로 값으로 표현.<br>중복이 필요한 작업에 사용.<br>[Repeated Properties][repeated] |
| `required` | `bool` | `False` | 꼭 필요한 값으로 표기.<br>`repeated=True`와 같이 사용하지 못하며, `default=True`와는 같이 사용할 수 있음. |
| `default` | Property 기본 유형 | `None` | 아무것도 지정하지 않을경우, 기본으로 들어감.<br>`repeated=True`와 같이 사용하지 못하며, `required=True`와 같이 사용할 수 있음 |
| `choices` | 기본 유형의 값 목록 | `None` | 값을 선택할 수 있는 목록 |
| `validator` | 함수 | `None` | 값을 함수에 맞게 검증하고 그것으로 입력하도록 설정합니다.<br>자세한 내용은 [Writing Property Subclasses][writing-property] |
| `verbose_name` | 문자열 | `None` | Jinja2와 같은 웹프레임 워크에서 사용되는 HTML label을 나타냄 |

* 이후 내용은 그냥 홈피보자.
	* 딱히 적을 내용도 없음.


[ndb-properties]: https://cloud.google.com/appengine/docs/python/ndb/properties
[compressed]: https://cloud.google.com/appengine/docs/python/ndb/properties#compressed
[date-time]: https://cloud.google.com/appengine/docs/python/ndb/properties#Date_and_Time
[db-geopt]: https://cloud.google.com/appengine/docs/python/datastore/typesandpropertyclasses#GeoP
[structuredproperties]: https://cloud.google.com/appengine/docs/python/ndb/properties#structured
[computeproperty]: https://cloud.google.com/appengine/docs/python/ndb/properties#computed
[expando]: https://cloud.google.com/appengine/docs/python/ndb/entities#expando
[repeated]: https://cloud.google.com/appengine/docs/python/ndb/properties#repeated
[writing-property]: https://cloud.google.com/appengine/docs/python/ndb/subclassprop
