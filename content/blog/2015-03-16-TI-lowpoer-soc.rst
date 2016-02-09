TI에서 베터리를 가장 적게 먹는 칩 출시
========================================

:date: 2015-03-16 23:56
:modified: 2015-04-02 23:05
:category: Hardware
:tags: ti, chip, iot, m3, arm, ble, low energy
:slug: ti-lowpwoer-soc-release
:summary: 뉴스가 나왔다. 베터리가 필요없는 SOC가 나왔다고, 믿지는 않았다. 그래서
          찾아봤다. 역시나... 그져 대기시에만 오랫동안 지낼수 있도록 가장 적은
          전력을 사용할뿐...


산업일보_ 에 "TI, 베터리 없는 IoT 커넥티비티 구현" 이라는 뉴스가 올라왔다.
뭔일인가 해서 봤더니만... SimpleLink라는 초전력 플랫폼을 개발했다는 소리였다.

.. _산업일보: http://www.kidd.co.kr/news/178946


기본 코어는 ARM® Cortext®-M3 MCU를 사용했고, 플래시 / RAM, ADC, 이것 저것들을
같이 묶은 것에 통신은 `Bluetooth Low Energy(BLE)`_, `ZigBee®`_, `6LoWPAN`_,
sub-1GHz, `ZigBee RF4CE™`_, 최대 5Mbps 고유모드로 지원한다고 한다.

.. _Bluetooth Low Energy(BLE): http://en.wikipedia.org/wiki/Bluetooth_low_energy
.. _ZigBee®: http://en.wikipedia.org/wiki/ZigBee
.. _6LoWPAN: http://en.wikipedia.org/wiki/6LoWPAN
.. _ZigBee RF4CE™:
   https://docs.zigbee.org/zigbee-docs/dcn/09/docs-09-5231-03-rmwg-understanding-zigbee-rf4ce.pdf


제목에서는 베터리가 없다고 말을 했지만.. 침 설계된 내용들을 확인해보면...

* Active-mode RX: 5.9 mA
* Active-mode TX at 0 dBm: 6.1 mA
* Active-mode Tx at +5 dBm: 9.1 mA
* Active-mode MCU: 61 µA/MHz
* Active-mode MCU: 48.5 CoreMark/mA
* Active-mode Sensor Controller: 8.2 µA/MHz
* Standby: 1 µA (RTC Running and RAM/CPU Retention)
* shutdown: 100 nA (Wakeup on External Events)

...

적게 먹기는 한다. 전력은 조금 먹지만, 전압이 1.8에서 3.8V라고 적혀있는 걸보면...
건전지 2개는 들어가야되는...

이 아이드은 셈플로 몇개 받을 수 있는지 한번 알아볼까... 최대 GPIO도 31개면
괜찮은데...

* CC2630_ : ZigBee, 6LoWPAN
* CC2640_ : Bluetooth Smart
* CC2650_ : Bluetooth Smart, ZigBee, 6LoWPAN, ZigBee RF4CE
* CC1310_ : Sub-1GHz
* CC2620_ : ZigBee RF4CE

.. _CC2630: http://www.ti.com/product/cc2630
.. _CC2640: http://www.ti.com/product/cc2640
.. _CC2650: http://www.ti.com/product/cc2650
.. _CC1310: http://www.ti.com/product/cc1310
.. _CC2620: http://www.ti.com/product/cc2620

