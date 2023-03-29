Title: MacOS Mojave에서 Google Drive Stream 오류
Date: 2018-11-17 10:35:17
Category: Software
Tags: google drive stream, macos, mojave
Slug: macos_mojavee-seo_google_drive_stream_o-ryu
Summary: Google Drive Stream이 실행은 커녕 죽어버린다.

Google Drive Stream을 사용하고 있다. 그런데 Mojave로 OS를 업로드한 뒤부터는 실행이 안되고 어느 정도 작동하다가 죽어버리는 현상을 확인하였다.

사진도 못 옮기고 이것저것 텍스트들도 제대로 작업을 못하던 중에 혹시나 그냥 앱만 지우면 안 되는 건가라는 생각에서 매뉴얼을 찾아서 보고 작동이 되는 것을 확인하였다.

그냥 이렇게 하면 된다고 말 한마디면 되는 건데... G Suite 쪽은 제대로 알려주는 것이 없으니...

터미널이 편하다면 터미널로 아니라면 해당 위치에 있는 파일들을 삭제하면 된다.

    $ sudo rm -rf /Applications/Google\ Drive\ File\ Stream.app/
    $ sudo rm -rf ~/Library/Application Support/Google/DriveFS/

위의 내용처럼 작업하고 재시작하면 잘 실행된다.

