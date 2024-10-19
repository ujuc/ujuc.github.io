Title: Linux 우선순위 설정
Date: 2018-09-28 18:47:14
Category: Operation
Tags: linux, priority, scheduler
Slug: linux_u-seon-sun-wi_seor-jeong
Summary: Linux에서 프로세스 우선순위를 정하는 방법에 대해서 알아보도록 하자... 

리눅스에서는 두가지 숫자를 이용하여 task(process)에 대한 우선순위를 정할 수 있다.

1. Priority (PR)
Task에 대한 스케쥴링 우선순위에 대한 값을 나타낸다. `rt` 항목은 리얼타임 항목에 대한 내용을 나타냄
2. Nice (NI)
Task에 대한 nice 값을 나타낸다. 사용자 레벨에서 수정이 가능하다. -20 ~ +19 까지의 값을 가지고 있으며, -20값이 우선순위가 가장 높은 값이고 양수로 올라갈수록 낮은 값이다. 0은 `PR` 값과 동일한 설정을 나타낸다.

### Rriority 계산

```
PR = 20 + (-20 ~ +19)
```

해당 계산식을 이용하면 0 ~ 39 사이의 값이 되는데 이것은 Priority 값의 100 ~ 139 사이 값에 대응된다.

## Rriority

Linux에서는 Task에 대한 우선 순위를 정할 수 있다. 물론 User task priority 만 가능하다. RT task priority 부분은 사용자 권한으로 접근이 안된다.

자세한 내용을 확인하려면 다음 URL에서 확인을 하도록하자.

- [IBM - Inside the Linux scheduler](https://www.ibm.com/developerworks/linux/library/l-scheduler/)
    - 리눅스 커널 2.6 버전이상에서 사용하는 스케쥴러에 대한 내용이 정리되어있다.
    - 여기서는 다음 그림을 참조하면된다.

    ![The Linux 2.6 scheduler runqueue structure
](https://www.ibm.com/developerworks/linux/library/l-scheduler/figure1.gif)

- [SUSE - Tuning the Task Scheduler](https://www.suse.com/documentation/sles11/book_sle_tuning/data/cha_tuning_taskscheduler.html)
    - SUSE 11 버전에서 튜닝하는 것에 대한 내용 중 하나이다. 12 버전에 대한건 딴문서가 있으니 확인.

## 우선순위 설정

### Daemon 구성 파일에서 설정

- `/etc/init.d` 에서 서비스 파일을 이용하여 `--nicelevel` 옵션 추가
    - [Setting up init.d service daemon priority (with or without monit)](https://unix.stackexchange.com/a/123926)

- `/etc/init.d` 에서 서비스 파일에 주석으로 `# chkconfig:` 옵션 추가
    - [how to change the startup order of linux init scripts in Redhat, Centos](https://serverfault.com/questions/754676/how-to-change-the-startup-order-of-linux-init-scripts-in-redhat-centos)

- Systemd 에서 설정하는 방법
    - [systemd.exec](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Scheduling)

### `limits.conf` 파일에서 지정

- 특정 사용자에 대한 모든 프로세스에대한 값을 정할때 사용한다.

```
Username    hard/soft    priority    10
```

다음 링크에서 자세하게 확인하도록 하자.

- [Set default nice value for a given user (limits.conf)](https://unix.stackexchange.com/questions/8983/set-default-nice-value-for-a-given-user-limits-conf)
- [limits.conf man page - pam | ManKier](https://www.mankier.com/5/limits.conf)

### `nice` 명령을 이용하여 동적으로 할당하는 방법

- 일반적인 사용법
    - `nice -n {nice_value} {program_name}`
    - [Process 'niceness' vs. 'priority'](https://askubuntu.com/questions/656771/process-niceness-vs-priority)
    - [Setting process CPU priority with nice and renice | Benjamin Cane](http://bencane.com/2013/09/09/setting-process-cpu-priority-with-nice-and-renice/)
    - [How do I start a process with a nice value of -20 and not give it root privilege?](https://unix.stackexchange.com/questions/72934/how-do-i-start-a-process-with-a-nice-value-of-20-and-not-give-it-root-privilege)

### 특정 프로그램으로 Daemon을 이용하여 관리하는 방법

- [Auto nice daemon](http://and.sourceforge.net/)
    - 업그레이드가 2005년 이후로 안되고 있다.
    - 그러니 사용하기 꺼림직...
    - 찾다가 나왔으니 뭐...
    - [Reddit 글](https://www.reddit.com/r/linuxquestions/comments/4ctr5c/is_the_autonice_daemon_and_safe_to_use/) 에서는 사용하기가 불안하다는 내용도...
- [Ananicy](https://github.com/Nefelim4ag/Ananicy)
    - Another Auto nice daemon
    - 지금까지 개발중이다.
    - Role 값을 JSON 형식으로 작업이 가능하다.

PS. IO Priority를 변경하고 싶다면 `ionice`를 확인하도록 하자. ([manpage](https://linux.die.net/man/1/ionice))
