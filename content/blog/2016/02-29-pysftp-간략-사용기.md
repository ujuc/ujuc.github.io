Title: pysftp 간략 사용기
Date: 2016-02-29 21:55
Category: Develop
Tags: python, sftp, lib, 
Slug: pysftp-간략-사용기
Summary: pysftp를 사용하여 파일을 가져오는 것에 대해 이야기한다.

처음 작성해놓은게 2013년 11월 달이다. 그때 사용한 것을 Evernote 정리중 확인하여 남겨뒀는데 새로 써야겠다. 다 바겼다.ㅡ.ㅡ....

우선 이 패키지는 14년 5월 이후로 [pypi 프로젝트](https://pypi.python.org/pypi/pysftp)에서는 업로드가 되고 있지 않으며, [Project repo](https://bitbucket.org/dundeemt/pysftp)의 업로드는 이루워지고 있으며, 3.4까지 테스팅을 해봣단다. 파일만 올리기위해서 사용했던 라이브러리라 간단히 sftp를 이용하여 파일을 올리고 받기를 원한다면 괜찮을 듯.

## Package

1. SFTP를 python에서 직접 사용할 수 있도록 도와주며, 내부는 C로 구성되어있다.
	* 그 덕분에 설치시 `python-dev` 페키지가 필요하다. (Ubuntu 리눅스 기준)
2. 사용하는 원격지에 ssh가 설치되어있는지 확인하자. 가끔 설치가 안되어있는 경우도 있다.

## 사용법

간단히 적겠다. 모자르면 [문서](http://pysftp.readthedocs.org/en/release_0.2.8/cookbook.html)를 보자.

	:::python
	import pysftp

	cinfo = {'host': 'hostname', 'username': 'ujuc',
			 'private_key': '/path/to/keyfile', 'port': 2222}
	with pysftp.Connection(**cinfo) as sftp:
		sftp.get('mybackupfile')
		sftp.put('myoriginfile')

		with sftp.cd('static'):
			sftp.chdir('here')
			sftp.chdir('there')

이정도 주석 달다가 지웠다. 그것이 없어도 sftp를 사용하고 있다면 간단히 상요할 정도로 sftp 명령어에서 사용하는 내용들을 추가해놓았다.

아직 pypi 측으로 버전업된 것이 반영되지 않아 새버전을 사용하고 싶으면 레포로 가서 작업을 진행하는 것을 추천한다.

