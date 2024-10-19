Title: Edison - Bluetooth 설정
Date: 2016-06-22 00:12
Category: Hardware
Tags: edison, bluetooth, iot
Slug: edison_-_bluetooth_seor-jeong
Summary: 오래된 글이다 그냥 내놓는다. IBM에서 나왔던 Edison 에서 bluetooth 설정에 관련된 내용이다.

오래된 글이다 잠시 IoT로 하면서 기본적으로 설정하면서 나왔던 것. 정리한 내용이다.

----

# Bluetooth 설정

* Edison 에서는 Bluetooth 제어 모듈로 BlueZ를 사용하고 있다.
* 리눅스에서 다쓴다.
* 그런데 개발이 중단된것같은 느낌이 들긴했다. 그냥 느낌임.
* 패키지 구조는 아래와 같다.

## 설정

* 간단하다. 기본적으로 Bluez가 설치가되어 있으니 그냥 켜주기만하면 된다.
* 먼저 `bluetooth` 데몬을 실행시켜준다.

```
# systemctl stop bluetooth
# systemctl start bluetooth
# systemctl status bluetooth
```

* 블루투스를 사용할 수 있도록 모듈을 활성화시켜준다.

```
# rfkill list
# rfkill unblock bluetooth
```

## 어플리케이션 사용

### `bluetoothctl`

* 쉘형식으로 접근하여 블루투스를 설정할 수 있다.
* `agent`를 설정하여 범위를 줄여서 확인할 수 있다.
* 나머지 사용법은 [블루투스 가이드][1]를 보도록 하자.

### `hciconfig`

* `ifconfig`와 같은 `hci`관련 디바이스들의 상태를 확인할 수 있는 툴이다.
* 사용법은 동일하며, 몇몇 설정이 되어있어야한다.
* `hciconfig hci0 sspmode 1`: `hci0`에 간단한 페어링 설정을 활성화 한다는 의미이다.
* `hciconfig hci0 sspmode`: `hci0`에 설정된 간략한 페어링 설정이 어떻게 되어있는지를 확인한다는 것.
* `hciconfig hci0 lestates`: LE 모듈 관련되서 설정들을 확인할 수 있음.

### `hcitool`

* 간단한 명령어로 `bluetoothctl`을 사용하지 않고서 작업을 진행할 수 있다.
* `hcitool scan`을 이용하여 블루투스 기기를 검색할 수 있다.
* 옵션들을 이용해서 더 다양한 작업들이 가능하게 해놨다.

### `pybluez`

* BlueZ의 Python 라이브러리인데...
* 사람들은 `hcitool`을 더 많이 쓰는 것으로...
* C맵핑을 해놔서 왠만한 작업들은 가능한 것으로 보이나 문서가 빈약하여 사용하기 쉽지 않다.
* 뭔가 추가를 하려면 코드를 봐야된다.
* 그래서 잘안쓰나...

## 참고자료

* [Intel Edison Board Getting Started with Bluetooth](https://software.intel.com/en-us/articles/intel-edison-board-getting-started-with-bluetooth)
* [Intel Edison Bluetooth Guide][1]
* [pybluez](https://github.com/karulis/pybluez)
* [edison-guies](https://github.com/intel-iot-devkit/edison-guides/wiki)
* [Connecting to Intel Edison from Android with Bluetooth LE](https://software.intel.com/en-us/articles/connecting-to-intel-edison-from-android-with-bluetooth-le-ble)

[1]: http://download.intel.com/support/edison/sb/edisonbluetooth_331704004.pdf