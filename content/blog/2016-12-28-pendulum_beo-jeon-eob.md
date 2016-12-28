Title: Pendulum 버전업
Date: 2016-12-28 23:36:13
Category: Develop
Tags: pendulum, datetime, date, module
Slug: pendulum_beo-jeon-eob
Summary: datetime 패키지중 하나인 Pendulum이 업그래이드 했다. 그래서... 에러가 발생했다

기본 패키지 인 datetime 이 영 불편해서 회사 프로젝트에서 사용중이던 date 파일을 [Pendulum](https://pendulum.eustace.io)으로 변경하여 구성하고 잘 쓰고 있었는데... 패키지 업그레이드로 사용하던 기능이 deprecate 되어버렸다.
아직 정식 1.0 버전이 나오지 않았기에 내용들이 계속 바뀌고 있다보니... 속이...

---

## 0.7.0

* [원본](https://pendulum.eustace.io/history/#0-7)

### Added
* `Date` 클라스 추가됨.
* `Time` 플라스 추가됨.
* Python 3.6에서 소개된 [`fold`](https://www.python.org/dev/peps/pep-0495/#the-fold-attribute) 속성에대한 실험적 지원이 추가됨.
* `Interval` 클라스에 `remaining_days` 속성이 추가됨
* `Pedulum` 클라스에 `int_timestamp` 속성을 추가하여 지금은 사용되지 않는 `timestamp` 속성에 대한 동작을 진행함.
* `start_of()`/`end_of()` 에서 새로운 `hour`, `minute`, `second` 단위를 지원.
* `astimezone()`에 시간대 문자열을 지원함.
* `in_words()`는 다른 단위를 사용할 수 없을때 잠깐 보여짐.

### Changed
* `Period` 속성이 (특히 `years`와 `months`) 정확히 표현.
* `Interval.seconds`는 호환성을 위해 `timedelta`와 같은 나머지 초에 대한 전체 값을 반환. `remaining_seconds`를 사용하면 이전에 작동하였던 것과 같이 작동함.
* 일반적인 형식에대한 구문 분석 성능이 향상됨.
* 더이상 `pytz` 라이브러리를 사용하지 않습니다. 타임존 데이터베이스로 [pytzdata](https://github.com/sdispater/pytzdata))를 사용.
* Locale, 테스트 인스턴스, formatter는 이제 해당 모듈 메소드를 사용할때 모듈 수준이 gobally 수준으로 설정됨.

### Deprecated
* `timestamp`는 이제 메소드로 사용되며 더이상 프로퍼티로 사용되지 않음. 다음 버전에서 기본 방법으로 사용될 예정임.
* 년, 월과 관련된 `Interval` 속성과 메소드는 더이상 사용되지 않음.
* `Interval.days_exclued_weeks`는 더 이상 사용되지 않음. 대신 `remaining_days`를 사용.

### Fixed
* 특정 시간대를 불러올 때 발생하는 예외가 수정됨.
* `end_of('day')`는 이제 마이크로 초를 999999으로 바르게 설정함.
* `Period` 인스턴스 프로퍼티 정확도가 향상됨.
* 일부 시간대에서 Pendulum 인스턴스를 초기화할때 정확도가 밀리초 단위로 수정되었음.
* Period는 `pickle`로 직렬화가 가능함.
* 시간 단위를 변경하는 `minute_()`, `second_()`, `microsecond_()` 에대한 setter 가 수정됨.
* Windows 지원이 수정됨.

---

## 0.8.0

* [원본](https://pendulum.eustace.io/history/#0-8)

### Added
* `with_date()`와 `with_tim()`을 대신하는 `on()`, `at()` 메소드가 추가됨.
* 구문 분석된 문자열과 일치하는 형식을 얻기위한 `parse()`에 `strict` 키워드 인수를 추가.
* 시간 간격 길이를 제어하기 위한 `range()` 메소드에 시간 량을 더하는 기능 추가.
* `Timezone` 클라스에 `datetime()` 헬퍼 메소드 추가.

### Changed
* [ISO 8601](https://ko.wikipedia.org/wiki/ISO_8601) 문자열 구문 분석이 개선 됨.

### Deprecated
* `with_date()`, `with_time()`은 더이상 사용되지 않고, `on()`, `at()` 으로 사용.
* `create_from_date()`, `create_from_time()`은 더이상 사용되지 않고, `create()`으로 사용.

