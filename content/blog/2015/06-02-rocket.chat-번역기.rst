Rocket.Chat 번역기
##############################

:date: 2015-06-02 22:45
:category: Chat
:tags: 자랑질, chat, rocketchat, 번역, javascript, meteo
:slug: rocket.chat-번역기
:summary: 어제 짧아서 번역을 했는데...

어제 //build/ Seoul 행사를 끝내고, 곧장 내려와 메일을 읽던 중, Github 데일리 메
일링에 추가된 `Rocket.Chat`_.

.. _Rocket.Chat: https://github.com/RocketChat/Rocket.Chat

심심해서 코드 보던 중 발견한 ``i18n``. 클클클 번역이나 해야지 짧을 꺼야... 그런 심보
로 시작. 10분 만에 issue_ 등록.

.. _issue: https://github.com/RocketChat/Rocket.Chat/issues/89

이유는 영어와 한국어의 어순이 반대다 보니... ``%s by %s`` 의 경우, 한국어로 ``%s에서
%s로`` 로 번역이 되어야 되는데. 어떤 놈이 앞의 ``%s`` 인지 한국어에서는 알 수 없는 문제
가 발생. 그래서 짧은 영어로 적었더니. 친절하게 제목도 바꿔주고, 테스트할 수 있게 
PR해줄 수 있느냐기에 신속하게 PR_.

.. _PR: https://github.com/RocketChat/Rocket.Chat/issues/89

그렇게 issue_ 는 해결되었고, 번역은 반영되었다.

소스 중에 번역 페이지가 있으면 항상 보지는 않았는데... 이번에는 우연히 번역
을 보았고, PR을 뒤져보니 PR을 보내면 웬만해서는 받아주는 듯하여 issue_ 부터 날리
고 어떻게 할지 기다린 게 잘 된듯하다.
뭐 이렇게 녹색 상자 한 칸 더 체우 는기지... ㅋㅋㅋㅋㅋ
