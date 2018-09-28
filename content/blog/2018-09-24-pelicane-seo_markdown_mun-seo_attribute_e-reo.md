Title: Pelican에서 Markdown 문서 Attribute 에러
Date: 2018-09-24 22:45:00
Modified: 2018-09-28 18:58:00
Category: Develop
Tags: pelian, markdown, 
Slug: pelicane-seo_markdown_mun-seo_attribute_e-reo
Summary: Pelican을 새로 설치하였더니 markdown 문서들이 전부 컴파일이 안된다.

블로그를 python 3.7로 업그레이드로 진행하고 나서 다음과 같은 에러가 발생한다.

```bash
pelican /Users/ujuc/repos/ujuc.github.io/content -o /Users/ujuc/repos/ujuc.github.io/output -s /Users/ujuc/repos/ujuc.github.io/pelicanconf.py 
ERROR: Could not process blog/2017-10-22-pa-i-sseon-eu-ro_ri-nug-seu_bae-po-pan_hwag-in-ha-gi.md
  | AttributeError: 'Registry' object has no attribute 'keys'
ERROR: Could not process blog/2014-02-23-pylint.md
  | AttributeError: 'Registry' object has no attribute 'keys'
```

git으로 버전을 관리하고 있어 해당 변경점을 확인하였더니 확인했더니 Markdown 라이브러리 문제다. 그것도 메이저로 업그레이드되면서 무언가가 변경이 되었고, 그게 Pelican 에서 사용하는 어떤 키와 잘못 설정된 부분이 있어서 발생한 것으로 파악된다.

나는 pipenv 를 사용하니 `Pipfile` 에서 `Markdown` 라이브러리 버전을 다음과 같이 수정을 하였다.

```text
[packages]
Markdown = {version = "<3.0"}
```
