Title: 파이썬으로 리눅스 배포판 확인하기
Date: 2017-10-22 18:21:49
Category: Develop
Tags: python, linux, distribution, lib
Slug: pa-i-sseon-eu-ro_ri-nug-seu_bae-po-pan_hwag-in-ha-gi
Summary: 파이썬으로 cmd 툴을 만들다보니 리눅스 배포판을 구분해야되는 경우가 발생했다!

요즘 코딩을 안하니... 머리가 멍해져가는지라.
컴퓨터를 밀고 나면 새롭게 설정하기위해서 만들어뒀던 셸  스크립트를 파이썬 cmd 라이버리를 가지고 변경하는중. (이건 따로 작성하자. 새로운 기능을 많이써서...)

리눅스 배포판 별로 설치하는 프로그램 명령어가 다르니 배포판을 구분하여 명령어를 다르게 적용할수 있도록 구현이 필요했다.

찾다보니 [`platform`](https://docs.python.org/3/library/platform.html) 라이브러리가 내부에 존재하고 해당 라이브러리에서 Unix 환경에서 사용이 가능한 `dist`, `linux_distribution` 메소드가 존재를 한다. 그런데 이거 3.5때 방출에 대한 논의 ([issue 1322](https://bugs.python.org/issue1322))가 되었고, 3.7에서 삭제되는 걸로 끝...

이런. 난 매번 버전 업데이트되면 최신으로 맞출껀데...

댓글을 읽다보니 해당 기능을 따로 빼내어 다른 서비스로 만들어둔 용자가 있었다. 이름은 [`distro`](https://pypi.python.org/pypi/distro).

그런데 이건 Unix 환경에서만 작동이된다. 맥에서는 패키지는 깔리지만 사용할 수 없다.

원리는 간단하다. `/etc/*-release` 파일에 작성되어있는 내용을 가져와 표시해주는 것으로 보인다. 뭐 Todo로 `lsb_release` 파일을 만들 수 있는게 있어보이지만... 언제될지는 모르겠고.

## 사용법

### `linux_distribution(full_distribution_name=True)`

* Output : `(id_name, version, codename)`
* `platform.linux_distribution()` 와 동일하다.

### `id()`

* 리눅스 배포판 id를 반환한다.

### `name(pretty=False)`

* 리눅스 배포판 이름을 반환한다.
* `pretty` 옵션을 사용하면 자세하게 나온단다.

### `version(pretty=False, best=False)`

* 배포판 버전이다. (16.04, 17.05 이런거…)

### `codename()`

* 배포판 코드네임

### `info(pretty=False, best=False)`

* 리눅스 배포판에 대한 정보를 보여준다.
* 여기에 키값으로 되어있는 것들이 메소드 명과 1:1 매칭된다.

다른 것도 많으니 [문서](http://distro.readthedocs.io/en/latest/) 확인하자.

