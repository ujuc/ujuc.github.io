Title: I hate input gpgkey in JetBrains IDEAs
Date: 2018-11-27 01:31:32
Category: Software 
Tags: jetbrains idea, gpg suite, key mapping 
Slug: i_hate_input_gpgkey_in_jetbrains_ideas
Summary: JetBrains IDEA를 주력하여 사용 중인데. GPG 키가 계속 침범을 하네? 그래서 문제를 찾았다.

이모든 원흉은 나의 과욕이었음을...

모든 코딩을 JetBrains의 IDEA에서 한다. 아직 vim이 익숙하지 않아서 그렇기도 하고...

언젠가 GPG키를 이용해서 git sign을 위해서 GPG suite를 설치해놨는데. 이넘이 문제일줄이야..

## 증상

`shift + cmd +r` , `shift + cmd + f` 키를 누르면 아래 모습처럼 GPG 키가... 계속 복사가 된다.

![shift_cmd_r]({filename}/img/2018-11-27_shift_cmd_r.png) 

![shift_cmd_f]({filename}/img/2018-11-27_shift_cmd_f.png)


## 해결

간단하다. System Preferences 가서 키보드 단축키에서 GPG suite에 관련된 것들을 unchecked 한다.

![system_preferences]({filename}/img/2018-11-27_system_preferences.png) 
