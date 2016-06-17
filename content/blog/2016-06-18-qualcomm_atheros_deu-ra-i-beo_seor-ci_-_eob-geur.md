Title: Qualcomm Atheros 드라이버 설치 - 업글
Date: 2016-06-18 02:13
Category: Operation
Tags: lenovo, ubuntu, qualcomm, driver, wireless, 16.04
Slug: qualcomm_atheros_deu-ra-i-beo_seor-ci_-_eob-geur
Summary: 이전 글에서 설치한건 너무 느렸다. 그러나 정식 버전이 패키지로 들어가면서 조금 나아졌다.

[이전글](http://ujuc.github.io/2016/04/22/install-wireless-qualcomm-atheros-device-driver-on-lenovo-y700/)로 글로 설치를 하고 썼으나 제대로된 펌웨어가 아닌지 설정을 해주고 설치했어야 했는데 그렇지 않아서 인지 1Mbps 로만 작동을 하였다.

몇번 재설치 끝에 귀찮아서 다시 우분투를 설치중. [스택오프플로 글](http://ask.ubuntu.com/questions/708061/aualcomm-atheros-device-168c0042-rev-30-wi-fi-driver-installation)이 업데이트가 되어있어 설치를 하였더니 원 속도까지 나오더라.

그런데 이게 좀 그런게...

커널은 4.2이상. 16.04가 버전업되면서 커널도 업글이되어서 이건 넘어갔다.

Qualcomm atheros 10k 드라이버가 들어있는 패키지는 `linux-firmware 1.158`. 16.04에서 공식 지원하는 버전은 `1.157`. 아마 6개월쯤 지나면 이것도 올라가겠지만 지금은 올라가지 않았으니. `1.158`은 16.10에 추가될 패키지로 지금은 테스팅 버전이다. 이것을 가져다가 설치하면 된다.

어짜피 기본 내용만 맞으면되니 `dpkg`를 이용해서 설치해주면된다.

	::shell
	wget http://mirrors.kernel.org/ubuntu/pool/main/l/linux-firmware/linux-firmware_1.158_all.deb
	sudo dpkg -i linux-firmware_1.158_all.deb

그리고 리붓해주면 손쉽게... 설치가 가능하다.

* 참고: [Ubuntu package](http://packages.ubuntu.com/search?keywords=linux-firmware)
