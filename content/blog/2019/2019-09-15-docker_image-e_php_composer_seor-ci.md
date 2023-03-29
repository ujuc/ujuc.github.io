Title: Docker image에 php composer 설치
Date: 2019-09-15 22:26:26
Category: Develop
Tags: php, composer, package manager, docker
Slug: docker_image-e_php_composer_seor-ci
Summary: Dockerfile에서 composer를 설치하는 방법을 정리한다.

회사에서 PHP를 사용하다보니 composer를 사용하는 일이 많아졌다.
설치하는 방법들이 찾는데마다 달라서 우선 찾은 것들을 정리해서 둔다.

* shell를 이용하는 방법은 이전 composer의 기본 설치방식이었던걸로 기억하고, 많은 사람들이 이렇게 설치하도록 알려준다.
* PHP 인터프리터를 이용해서 설치하는 방법은 composer 공식 페이지에 적혀있는 방법이다.
* Composer docker 이미지에서 multi-builder 방식으로 구성하고 composer 파일만 땡겨오도록 하는 방법이다.

<script src="https://gist.github.com/ujuc/4d795e11b571c4c84b60851ff369b1a6.js"></script>
