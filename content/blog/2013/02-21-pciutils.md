Title: PCIutils
Date: 2013-02-21 12:00:45
Modified: 2018-03-11 12:00:45
Category: Develop
Tags: pci, linux,
Slug: pciutils
Summary: `pciutils` 패키지에 대해서 알아본다.

[홈페이지](http://mj.ucw.cz/sw/pciutils/) 에서 말하는 건 아래의 영문내용!

>> The PCI Utilities are a collection of programs for inspecting and manipulating configuration of PCI devices, all based on a common portable library libpci which offers access to the PCI configuration space on a variety of operating systems.

PCI 구성을 위한 것도 이것이 해주고, PCI 관련된 프로그램 모음들도 가지고있는. 그런 페키지 pciuils 여기서 정해주지 않으면 아무리 컴퓨터에 좋은걸 끼웠거나… 이전에 사용하지 않았던 제품을 끼웠다고 해서 리눅스에서 먹어주는 것은 아니다.

[4월 9일자 pci.ids](http://pci-ids.ucw.cz/v2.2/pci.ids) 를 검색해보면 아마.. 지원하는 부품들 안에 자신이 사용하는 보드나 이름들이 없다면… 우리 리눅스 버전업을 그만두자.ㅡ.ㅡ…

PCI 슬롯에서 못읽어들이는데 어쩔수 있냐…..

뭐 따로 받아서 저것을 추가 해준다면야 사용이 가능하겠지만…………
 왠지 외국에서는 해줄 것같은데.. 우리나라에서는…………

*만약에 추가가 안되어있으면, 내가 추가하면 되겠네?*라는 생각이 문득들어…
찾아봤다. `/usr/share/misc/pci.ids` 여기에 있다. 그런데.. 이것만 바꿔주면 되는 것일까??

음.. 또 찾았다. 어디냐면..

pciutils 최신버전을 다운받아서 풀었더니 `update_pciids.sh`가 있다.ㅡ.ㅡ
그냥 이걸 실행시켜주면 알아서 설치가 될듯한데..
