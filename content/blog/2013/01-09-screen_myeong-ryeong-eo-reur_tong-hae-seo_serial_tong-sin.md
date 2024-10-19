Title: Screen 명령어를 통해서 Serial 통신
Date: 2013-01-09 11:39:40
Modified: 2018-03-11 11:39:40
Category: Develop
Tags: screen, serial communication
Slug: screen_myeong-ryeong-eo-reur_tong-hae-seo_serial_tong-sin
Summary: screen으로 serial 통신을 하는 프로그램으로 사용하자.

발단은 Coolterm이라는 Serial 통신 프로그램에서 Vi의 값을 변경할 수 없는 상황이 발생하여…

여기 저기 찾다가. `Screen`을 이용하여 Serial 통신을 할 수 있다는 포스팅을 찾아서 해보니.. 괜찮다.. 복잡하게 설정을 하지 않아도 되는 상황에서는 이것을 이용하는 편이 가장 편할 듯. `minicom`도 필요없다.

명령어 사용법 : `screen ‘디바이스 위치’ ‘전송속도’`

```
# Mac
screen /dev/tty.XXX 115200
# Linux
screen /dev/ttyXXX 115200
```

종료할때는 <Crtl>+<A> <Crtl+<\>로 종료할 수 있다.
