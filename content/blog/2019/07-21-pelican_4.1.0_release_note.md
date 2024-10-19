Title: Pelican 4.1.0 Release Note
Date: 2019-07-21 15:23:10
Category: Operation
Tags: pelican, static blogging tools, python
Slug: pelican_4.1.0_release_note
Summary: pelican 4.1.0 이 업글이 되었다.

블로그 정리하다가 업그레이드가 된 걸 알았다.

### [4.1.0 - 2019-07-14](https://docs.getpelican.com/en/stable/changelog.html#id1)

- 변경된 파일이 있으면 reload 가능 (Invoke 태스크를 통해 제공됨)
    - [github - `task.py.jinja2`](https://github.com/getpelican/pelican/blob/master/pelican/tools/templates/tasks.py.jinja2#L93) 에서 확인하면 `livereload` 패키지를 사용하여 새롭게 띄울 수 있도록 작업을 해뒀다.
- Poetry를 사용하여 패키지 관리
    - `pyproject.toml` 를 이용하게 됨.
- `python -m pelican` 형태로 호출 가능
    - env 환경에서 굳이...
- 콘텐츠 상대 소스 경로 속성 추가
- `EXTRA_PATH_METADATA` 디렉토리 허용
- 템플릿에서 사용 가능한 `all_articles` 변수가 추가됨.
    - [Common variables](https://docs.getpelican.com/en/stable/themes.html?highlight=all_articles#common-variables) 항목 확인 가능
    - 최근 소식 전달을 위한 기능 용...?
- 디버그 모드에서 출력 화면 향상
- Atom 피드에서 비었거나 중복된 summary 항목 삭제
- 페이지네이션, pelican-import, pelican-quickstart, 피드 임포터 버그 수정
