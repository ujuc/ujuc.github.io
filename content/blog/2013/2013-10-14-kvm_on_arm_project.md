Title: KVM on ARM project
Date: 2013-10-14 11:29:17
Modified: 2018-03-11 11:29:17
Category: Hardware
Tags: arm, kvm, hypervisor
Slug: kvm_on_arm_project
Summary: ARM 칩에서 KVM을 사용하는 프로젝트가 있어서 정리한다.

[Project homepage](http://systems.cs.columbia.edu/projects/kvm-arm/)

ARM 프로세스에서 지원하는 Virtualization을 이용하여 KVM을 올리는 프로젝트 Cortex-15A에서 작업한 내용이 있음. ARM Core는 ARMv7.

Virtual Open Systems is an innovative, agile and dynamic start-up company operating in embedded Linux, Android, SMP Virtualization and Cloud Computing. 이란다.

얼마전에 ARMv8에서 KVM을 사용하는 방법도 추가해놨다. (4월에 추가되고 7월에 업데이트 됨.)

삼성 Exynos 5250를 사용하는 Arndale Board에서 KVM을 이용하여 올렸는데 보면 QEMU가 작동하는 것을 볼 수 있다. 그러나 확실히 속도는 빠르다. 몇배속으로 돌린것인지 아니면 내가 봐왔던 ARM이 느렸던건지..

 [Youtube 동영상](http://youtu.be/yB8bdA2hjYg)

 덧. 2013.01.11에 작성한 글을 옮기면서 변경사항들이 있어 추가함.
