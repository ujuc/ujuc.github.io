Title: unattended-upgrade 써보자
Date: 2016-01-29 22:35
Category: Operation
Tags: ubuntu, manage, upgrade, security, command
Slug: unattended-upgrade-써보자
Summary: Ubuntu에서 보안 업데이트만 해보자.

AWS에서 서비스를 Ubuntu로 하고 있는데, 요즘 보안 이슈들이 계속 올라오고 있고,
그것에 대한 패치들도 많이 올라오고 있다. 사용하다가 서비스를 하고 있는 패키지들
을 업데이트를 할 수는 없고 (서비스에서 사용하는 패키지의 경우엔.. 답이 없다. 
했다가 무슨 소릴 들을지 모르기도하고 어디서 문제가 발생했는지 모르기도 하고)
보안 패치만큼은 하고 싶은데...

찾다보니 `unattended-upgrade`를 사용해서 할 수가 있다.

* [Ubuntu manpage - unattended-upgrade](http://manpages.ubuntu.com/manpages/lucid/man8/unattended-upgrade.8.html)

### 사용법

    :::shell
    $ sudo unattended-upgrade

하게되면 알아서 보안 패치를 업그레이드하고 관련된 내용들을 `/var/log/unattended-upgrades.log`에서 확인할 수 있다. 관련해서 추가적으로 만들어지는 내용들도 있고, 특정된 내용들을 구성할 수도 있다.

만약 설치를 하지 않고, 어떠한 보안업데트가 되는지를 확인하고 싶다면, 아래와 같은 명령어를 사용하여 업그레이드를 하면된다.

    :::shell
    $ sudo unattended-upgrade --dry-run

왠만해서는 `--dry-run` 옵션을 이용하여, 업그레이드를 할 수 있도록 확인해주면 되는데, 쉽지는 않지...

단점은 아직 1.0이 아니다. 그래서 그런지 외부로 출력되는게 없고, 전부 log파일로만 나온다...

