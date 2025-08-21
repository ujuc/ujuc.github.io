Title: py.typed 파일은 무엇인가?
Date: 2025-08-21 21:15
Modified: 2025-08-21 21:15
Category: Develop
Tags: python, type-hinting, type
Slug: pytyped-파일은-무엇인가
Summary: uv에서 라이브러리를 만들려고 명령어를 입력하니 `py.typed` 파일을 만들어줬다. 이것은 무엇인가?

# 들어가기

MCP 공부를 하려고 Python으로 Roam Research MCP를 만들어보려고 했는데, Roam Research API를 위한 공식 코드가 패키지화되지 않은 상태로 각각 따로 사용하고 있었다.
그럼 Python 라이브러리를 만들어볼까 하고 한달째 (귀찮아...) 찬찬히 만들어가고 있다.

[uv][1]를 이용해서 `uv init --lib` 를 하였더니, `py.typed`라는 파일을 만들어줬다. 이건 뭐지?
파이썬으로 단순 스크립트를 만들거나, 그냥 간단한 cli를 만들어서 사용하던 나에겐 낯선 파일이었다.

# PEP 561 - Distributing and Packaging Type Information

구글에서 검색하니 [PEP 561][2] 에 명시된 내용이라고 뜸.

> 타입 검사를 지원하는 패키지를 배포하고자 하는 개발자는 타입 검사를 지원하는 패키지에 `py.typed`라는 마커 파일을 추가해야 합니다. 이 마커는 재귀적으로 적용되므로 최상위 패키지에 이 마커가 포함되어 있으면 모든 하위 패키지에서도 유형 검사를 지원해야합니다. 이 파일을 패키지와 함께 설치하려면 관리자는 아래와 같이 `distutils`에서 `package_data`와 같은 기존 패키징 옵션을 사용할 수 있습니다.
> (중략)
> 네임스페이스 패키지 ([PEP 420][3])의 경우, 충돌을 피하고 명확성을 위해 `py.typed` 파일은 네임스페이스의 서브모듈에 있어야 합니다.
> 이 PEP는 모듈 전용 배포 또는 네임스페이스 패키지 내의 단일 파일 모듈의 일부로 타이핑 정보를 배포하는것을 지원하지 않습니다.
> 단일 파일 모듈은 패키지로 리팩터링하고 위에서 설명한 대로 패키지가 타이핑을 지원하다는 것을 표시해야 합니다.
([원문][4])

# `py.typed` 파일이란?

- 이 라이브러리는 타입 힌팅을 완전히 지원한다는 내용을 명시하는 데 사용된다.
- 내용은 안써도 됩니다.
- `.pyi` ([Stub Files][5]) 파일이 있는 경우엔 `py.typed` 파일을 필요가 없습니다.


# TMI

- 2017-11-12 일에 `.typeinfo` 에서 `py.typed`로 파일명이 변경되었다.

# 참고

- [PEP 561][2]
- [Distributing type information](https://typing.python.org/en/latest/spec/distributing.html#type-information-in-libraries)
- [Typing Python Library](https://typing.python.org/en/latest/guides/libraries.html#providing-type-annotations)


[1]: https://docs.astral.sh/uv/concepts/projects/init/#libraries
[2]: https://peps.python.org/pep-0561/
[3]: https://peps.python.org/pep-0420/
[4]: https://peps.python.org/pep-0561/#packaging-type-information
[5]: https://typing.python.org/en/latest/spec/distributing.html#stub-files
