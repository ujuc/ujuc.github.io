Title: Stderr check in zshell
Date: 2016-01-27 00:57
Category: Operation
Tags: zsh, operation
Slug: stderr-check-in-zshell
Summary: zsh 가상환경 설정한대서 계속 걸쩍지근하게 나오는 에러 문구를 없애고
        싶었다.

Shell로 zsh를 사용중이다. 얼마전부터 개발 환경 설정을 해놓고 이곳저곳에서
쓰다보니 해당 개발 환경이 꾸며져있지 않으면, 없다고 해당 문구가 출력된다.

![stderr]({static}/img/2016-01-26_shell_error.png)

은근히 신경쓰인다. 만약 두개를 설정해놨는데 둘다 없다면 줄이 두 줄로 늘어난다.

그래서 찾았다. 찾다보니 내가 무심코 사용했던 내용에대해 조금더 볼 기회가 생긴듯.

우선 Shell에서 기본 I/O 스트림을 통해서 나오는 값들에대해서 다음 숫자로 제어할
수 있다.

| Handle | Name | Description |
| :----: | :--: | :---------: |
| 0 | stdin | Standard input |
| 1 | stdout | Standard output |
| 2 | stderr | Standard error |

간단히 하자.
go가 설치되어 있는지 확인을 한다. 제대로 설치됐다면 stdout으로 설치된 경로가 나올 것이다.

    :::shell
    $ which go

![ex1_1]({static}/img/2016-01-26_ex1_1.png)

요놈을 안나오게 해보자.

    :::shell
    $ which go 1> /dev/null

![ex1_2]({static}/img/2016-01-26_ex1_2.png)

오~~~

stderr 값이 나오면 안나오게 할려고 보면... 이건 설치가 되어있으니... 없는걸로...

    :::shell
    $ which rbenv

![ex2_1]({static}/img/2016-01-26_ex2_1.png)

이걸 위와 같이 `1` 을 사용하면...

    :::shell
    $ which rbenv 1> /dev/null

![ex2_2]({static}/img/2016-01-26_ex2_2.png)

음... 출력되는 문구가 stderr로 나오는 건줄 알았는데 아닌갑다. `1`로 출력되는걸 막으라했더니...

그럼 Python에서는 어디로 나올까?

    :::python
    In: import subprocess as sub
    In: check_rbenv = sub.Popen('which rbenv', stdout=sub.PIPE,
                                stderr=sub.PIPE, shell=True).communicate()
    In: print(check_rbenv)
    Out: (b'', b'')

음?? 암것도 안나온다...

    :::python
    In: import os
    In: os.system('which rbenv')
    Out: 256

출력값이 256이라니... 혹시나 해서 봤더니 8bit밀란다. 저걸 밀면 1이 떨어지는데...
리눅스에서 반환값이 1이면 비정상 종료일때로 알고 있다. 고로니 저넘은 제대로
실행된 아이가 아니라는 말씀...

그럼 `which` 명령어를 사용하여 명령어를 실행하게 되면, 정상종료면 위치를
말해줄꺼고 비정상 종료면 stdout으로 없다는 메시지를 남기고 비정상 종료를
시킨다고 해석하면 될듯.

결국 내가 하고 싶은데로 안되는거네... 이런!

다른 방법으로 찾아야지 뭐 별수 있나... 그래도 이번에 건진건 저렇게 숫자를
사용해서 내가 원하는 값들만 넣을 수 있는 방법을 찾았다는거... 그정도면 1시간동안
작업한 것에 대한 내용은 될듯.
