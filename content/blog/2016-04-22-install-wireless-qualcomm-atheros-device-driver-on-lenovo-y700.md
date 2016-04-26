Title: Install wireless Qualcomm Atheros device driver on Lenovo Y700
Date: 2016-04-22 22:59
Category: Operation
Tags: lenovo, ubuntu, qualcomm, driver, wireless, 16.04
Slug: install-wireless-qualcomm-atheros-device-driver-on-lenovo-y700
Summary: Qualcomm Atheros device driver on Lenovo Y700

새롭게 컴퓨터를 구입했다. Lenovo ideapad Y700. 문제는 다른 컴퓨터들은 다른 모듈이 연결되어있는데. 이 컴만 그런건지 아니면 일정 라인이상만 그런건지 모르겠으나, Qualcomm Atheros가 연결되어있어 커널에서 wifi를 잡지못하는 문제가 발생했다.

Ubuntu 16.04를 사용했음에도 불구하고 잡히지 않았던건, 커널버전 4.4.2이상이어야 해당 드라이버가 돌아가는데... Ubuntu 16.04버전이 4.4.0... 그래서 백포트하고, 드라이버를 옮겨주는것으로 해결.

[Qualcomm Atheros Device [168c:0042] (rev 30) Wi-Fi dirver installation](http://ask.ubuntu.com/questions/708061/aualcomm-atheros-device-168c0042-rev-30-wi-fi-driver-installation) 에서 말하는 작업을 설치해주면된다.

	:::shell
	sudo apt install build-essential linux-headers-$(uname -r) git
	echo "options ath10k_core skip_otp=y" | sudo tee /etc/modprobe.d/ath10k_core.conf
	wget https://www.kernel.org/pub/linux/kernel/projects/backports/stable/v4.4.2/backports-4.4.2-1.tar.gz
	tar -zxvf backports-4.4.2-1.tar.gz
	cd backports-4.4.2-1
	make defconfig-wifi
	make
	sudo make install
	git clone https://github.com/kvalo/ath10k-firmware.git
	sudo cp -r ath10k-firmware/QCA9377 /lib/firmware/ath10k/
	sudo cp /lib/firmware/ath10k/QCA9377/hw1.0/firmware-5.bin_WLAN.TF.1.0-00267-1 /lib/firmware/ath10k/QCA9377/hw1.0/firmware-5.bin

그리고 하나더...

이건 위에껄 하고 안되면 추가해주도록 하자.

	:::shell
	echo blacklist ideapad_laptop | sudo tee /etc/modprobe.d/blacklist.conf

