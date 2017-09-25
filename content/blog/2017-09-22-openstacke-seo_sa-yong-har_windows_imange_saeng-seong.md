Title: OpenStack에서 사용할 Windows imange 생성
Date: 2017-09-22 17:18:08
Category: Operation
Tags: openstack, nova, image, windows
Slug: openstacke-seo_sa-yong-har_windows_imange_saeng-seong
Summary: OpenStack에서 사용할 Windows 이미지를 생성해보자.

## 기본 준비사항

* Ubuntu 16.04
* [VirtIO driver](https://fedoraproject.org/wiki/Windows_Virtio_Drivers)
* [CloudBase init](https://cloudbase.it/cloudbase-init)
* Windows CD

## virt-manager 설치

```
$ sudo apt install -y kvm virt-manager
```

* virt-manager 설치 후에 VM을 생성한다.
* 이미지는 `qcow2`로 만들어야된다.

## VirtIO 드라이버 설치

* 가장 중요하다.
* 이 작업을 하지 않으면, OS 부팅할때 에러가 뜬다.
* **주의**
    - 하드로 사용할 이미지를 VirtIO로 설정해두면 설치는 모르겠는데 부팅이 되지 않는다.
    - 이것만큼은 바꾸지말고, 스토리지를 하나 더 만들어서 붙이면서 VirtIO로 설정해주고 드라이버를 설치해주도록 한다.

## CloudBase init 설치

* Cloud init 파일을 만들어주는 프로그램이다.
* 그냥 받아서 설치해주면 되는데 맨마지막 **일반화** 라는 항목이 있는데.
* 이것을 하게되면, Windows 첫 설치시 새로운 계정을 만들 수 있도록 이전 설정을 다날리는 작업을 해주기에 필요하다면 하고 아니라면 체크하지말고 설치를 하도록 하자.

## 디바이스 드라이버 확인

* 혹시나 없는 드라이버가 있는지 확인하고 하도록 하자.

## Glance에 Imange 업로드

* Hoizon
    - **주의** : `/var/tmp` 에다가 올린다. 그러니 `/var` 폴더에 용량이 있는지 확인하고 올리도록.
    - 편하게 올리자.
* CLI
    - `--disk-format`은 기본값이 `raw`이다. 그렇기에 `qcow2`로 변경해주고 올려야된다.

```
$ openstack image create --disk-format qcow2 --file windows.qcow2 windows
```

## 참고

* http://gotocloud.co.kr/?p=1575
* http://heavenkong.blogspot.kr/2014/04/create-windows7-virtual-machine-image.html
* https://fedoraproject.org/wiki/Windows_Virtio_Drivers

