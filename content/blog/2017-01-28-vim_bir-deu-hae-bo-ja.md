Title: vim 빌드해보자
Date: 2017-01-28 22:46:29
Category: Develop
Tags: dev, vim, build, ubuntu, mac
Slug: vim_bir-deu-hae-bo-ja
Summary: 이번에 플러그인을 사용하기 위해서 했던 작업들을 구성해보자.

vim 플러그인중 jedi-vim 을 사용하는데. 설치된 vim 에서 python 플러그가 켜있지 않아 관련되서 플러그인을 사용하지 않는다는 아래와 같은 에러 메시지를 뿜고 있었다.

```
Error: jedi-vim failed to initialize Python: jedi#setup_py_version: \
        Vim(py3file):Traceback (most recent call last): \
        (in function jedi#init_python[3]..<SNR>72_init_python[50]..jedi
#setup_py_version, line 18)
```


## Ubuntu

회사에서는 ubuntu에서 개발 중이라 vim에 관련된 설정을 추가해주고 해야됐다.
가끔 열어보는 vim이지만 그래도 정말 급할때는 이거라도 설치해서 사용하니 구성을 해놓는걸로..

* 해당 구성은 [Building Vim from source](https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source) 를 이용해서 구성하는 것으로 했다.

vim을 빌드하기 전에 dev 패키지를 설치해준다.

```
sudo apt install python3-dev ruby-dev
```

그리고 기존 패키지로 설치되어 있는 vim을 삭제한다.

```
sudo apt remove vim vim-runtime
```

Vim 코드를 받고 컴파일을 해주자.

```
git clone https://github.com/vim/vim.git
cd vim
./configure --with-features=huge --enable-multibyte \
            --enable-rubyinterp=yes \
            --enable-python3interp=yes \
            --enable-cscope
sudo make install
```

설치가 제대로 되었는지 확인하려면 `vim --version` 으로 확인하면 된다.

시스템 기본으로 구성하려면 아래 명령어를 쳐주면된다.

```
sudo update-alternatives --install /usr/bin/editer editer /usr/bin/vim 1
sudo update-alternatives --set editer /usr/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1
sudo update-alternatives --set vi /usr/bin/vim
```

## Mac

Mac OS에서는 brew를 사용해서 설치하면된다. 설치할때 옵션을 붙여주면 되는데 그 옵션은 다음에서 처럼 확인이 가능하다.

```
brew options vim
--with-client-server
	Enable client/server mode
--with-custom-perl
	Build with a custom Perl instead of the Homebrew version.
--with-custom-python
	Build with a custom Python 2 instead of the Homebrew version.
--with-custom-ruby
	Build with a custom Ruby instead of the Homebrew version.
--with-lua
	Build vim with lua support
--with-luajit
	Build with luajit support
--with-mzscheme
	Build vim with mzscheme support
--with-override-system-vi
	Override system vi
--with-python3
	Build vim with python3 instead of python[2] support
--with-tcl
	Build vim with tcl support
--without-nls
	Build vim without National Language Support (translated messages, keymaps)
--without-perl
	Build vim without perl support
--without-python
	Build vim without python support
--without-ruby
	Build vim without ruby support
--HEAD
	Install HEAD version
```

이후 설치할때 필요한 옵션에 대해서 추가해주면된다.

```
brew install vim --with-client-server --with-override-system-vi --with-python3
```

그리고 이 옵션은 다음번 vim 업데이트에도 반영이 되는 사안이니 한번만 설정해서 설치해주기만 하면된다.

---

솔직히 리눅스에서는 내가 빌드를 할일이 없다. 빌드를 한다는건 내가 그 프로그램에 대해서 깊게 알고 있어야되고 그것들을 하나씩 변경을가하는 것이라 생각했었고, 몇몇 프로그램은 그정도까지 손을 안되더라도 구성에서 변경이 가능했으니까...
이번에 vim 빌드하면서 어쩔 수 없구나를 느끼게되고...
brew 참 편한데 옵션이 많지는 않구나라는... 그리고 저것말고는 딱히 추가할 이유가 없긴해서...
linux-brew 에서는 어떻게 될련지 모르겠지만 그것까지는 사용하지 않고 있어서 작성하지 않았다.
