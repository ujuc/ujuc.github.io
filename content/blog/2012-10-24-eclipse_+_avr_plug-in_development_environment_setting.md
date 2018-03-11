Title: Eclipse + AVR Plug-in Development Environment Setting
Date: 2012-10-24 11:34:15
Modified: 2018-03-11 11:34:15
Category: Develop
Tags: avr, eclipse, development environment, environment, arch
Slug: eclipse_+_arm_plug-in_development_environment_setting
Summary: Eclipse를 이용해서 AVR 코딩할 수 있는 환경 만들기.

Eclipse로 AVR 프로그램을 코딩할 수 있다는 소리를 듣고서 곧장 검색을 해서 필요한 것들을 깔았었다.
그런데 뭔가 프로젝트에 x표가 나타나서 신경쓰이게 하던것을 한 블로그에서 찾았다!!!!

그래서 이렇게 남긴다. 까먹을까봐서..

[공식 홈페이지](http://avr-eclipse.sourceforge.net/wiki/index.php/The_AVR_Eclipse_Plugin)

리눅스에서는 기본적으로 컴파일러는 gcc를 이용해서 작동을 시키게 된다.

```
yaourt -S gcc-avr avr-libc avrdude binutils-avr
```

을 설치해줬다. Arch Linux에서는 이렇게 해주고 더 필요한 패키지들이 있으면,

```
yaourt -Ss avr
```

로 해줘 찾을 수 있다.

Eclipse를 설치 해주는데 이때 Eclipse는 C/C++용으로 설치해준다.
그리고서 프로젝트 만드는 것은

[Don’t panic! WinAVR + Eclipse + AVR Plug-in Developement Environment Setting](http://hoyoung2.blogspot.com/2010/07/avr-developement-environment-setting.html)

에서 확인하면 끝…