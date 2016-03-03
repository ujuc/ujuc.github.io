Title: [Python] Paramiko
Date: 2014-04-07 01:56
Modified: 2016-03-03 22:00
Category: Devlop
Tags: python, paramiko, ssh, lib
Slug: python-paramiko
Summary: Python ssh 모듈인 paramiko에 대한 내용을 작성함.

한글로된 글이 없어서 우선 내가 알아낸 곳과 사용한 곳까지 작성을 해둘려고한다.

[Paramiko][1]
=====

* Python 2.6+, 3.3+에서 사용할 수 있는 SSHv2 구현체이다.
* 물론 Client, Server를 둘다 사용이 가능하다.
* 저 레벨 암호화를 위해서 [PyCrypro][2](이부분은 Python C 확장으로 구현)를 제외한 나머지 부분들은 전부 Python으로만 구현되어있다.

## 사용

### 1. 사용 예제
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.connect('127.0.0.1', username='ujuc', password='lol')
```

### 2. Host Keys
* 첫 접근시 받아오는 Host Keys가 있다. 이것을 받아서 저장하던 날려먹던 상관은 하지 않지만 있어야지 접근이 가능하다.
  - 처음 `ssh`로 접근시 무의식적으로 `yes`를 누르는 그것!!
* 그러다보니 여기서도 그것에 관련된 내용을 사용할 수 있다. 
* `set_missing_host_key_policy(policy)`를 이용하여 host keys를 받아 저장할 것인지 아닌지를 판단하게 되는데. 기본값은 `RejectPolicy`로 되어있으며, `yes`를 받아와야한다면 `AutoAddPolicy`를 사용하도록 한다.

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='ujuc', password='lol')
```

* 물론 Public key를 이용해서 비밀번호 없이 접근이 가능하도록 할 수 있을듯 한데 그건 좀 확인이 필요할듯.

### 3. 실행
* 실행 명령어 `exec_command`를 실행하게되면, 값을 3개를 `tuple`로 받아온다.
* `stdin`, `stdout`, `stderr`이다.
*명령어에 대한 값들을 받아와 확인할때는 아래와 같이 작성을 하면된다.

```python
stdin, stdout, stderr = ssh.exec_command()
stdout.readlines()
['test\n']
```

* 만약 `sudo`명령어가 필요한 경우,

```python
stdin, stdout, stderr = ssh.exec_command('sudo')
stdin.write('lol\n')
stdin.flush()
data = stdout.read()
```

  - 위와 같이하여 작성을 하도록 한다.
  - 그리고 `write`다음에는 `flush`를 꼭 해줘야 작동을 하니 그점은 주의하도록 한다. 관련 내용은 [여기][3]에 있다

### 4. 연결 끊기
* 작업이 끝났으면 연결을 끊어야된다.
* 그냥 `close()`를 불러오면 알아서 끊어준다.

### 5. SFTP 사용.
* 어찌보면 `ssh`를 사용하면서 편했던 것이 `sftp`의 사용이다. 간단한 사용방법과 `ssh`가 설치가되어있으면 따로 `ftp`를 생성하지 않더라도 간단한 파일을 주고 받을 수 있도록 되어있기 때문이다.
* 먼저 `ssh`로 접속한 다음, `open_sftp()`후 파일을 가져올때는 `get('localfile.py', 'remotefile.py')`를 이용하고, 올려둘때는 `put('localfile.py', 'remotefile.py')`를 사용하면된다.

## 참고 자료
* [Paramiko Homepage][1]
* [Docs paramiko][4]
* [SSH Programming With Paramiko | Completely Different][5]
* [Paramiko: SSH and SFTP With Python][6]

[1]:http://www.paramiko.org/
[2]:http://pycrypto.org/
[3]:http://docs.paramiko.org/en/latest/api/file.html#paramiko.file.BufferedFile.write
[4]:http://docs.paramiko.org/en/latest/index.html
[5]:http://jessenoller.com/blog/2009/02/05/ssh-programming-with-paramiko-completely-different
[6]:http://segfault.in/2010/03/paramiko-ssh-and-sftp-with-python/


