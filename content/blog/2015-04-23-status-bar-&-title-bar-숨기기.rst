Status bar & Title bar 숨기기
####################################################

:date: 2015-04-23 01:25
:category: Develop
:tags: android, 기본, 난 모르겠다.
:slug: status-bar-&-title-bar-숨기기
:summary: Android 다 안다는 Status bar, Title bar 숨기기.

요즘 안드로이중이다. 오랜만에 했더니 봐야될께 많다. 특히 UI를 많이 안해서
그런가.. 감이 잘 안온다는 문제도...

SplashActivity를 추가해줘야되는데. 안드로이드에서 뭘 알아야지.. 그냥 예제에 있는
것들을 찾아서 변경해 추가를 했지만, 정리를 한번 해놔야되서... 뭐 간단하게 구성은
되어있다만. 이렇게라도 적어놔야 나중에 또 다른곳에서 엉뚱한것을 안찾지...

Title bar 숨기기
================

이것을 해줄려면 ``style`` 을 구성해서 해줘야된다. 뭔가 많이 불편해서 다른
곳에서도 가능한가를 찾아봤지만, 안된다. 뭐 특정 구역에서만 가능하게 해놨나보다.
그져 따라서 해놔야지...

``Styles.xml`` 에 추가한다.

.. code:: xml

   <resources>
       <style name="Theme.Splash" parent="android:Theme">
           <item name="android:windwoNoTitle">true</item>
       </stlye>
   </resources>


위와 같이 구성을 하고서 Activity에 작성을 해주면된다.

.. code:: c#

   [Activity (Theme = "@style/Theme.Splash", MainLauncher = true, NoHistory =
   ture)]
   brabra

이렇게 하고 필요한 내용들을 추가해주면 된다. 그러면 타이틂 바만 없어지는 것을
확인할 수 있다.

Status bar 숨기기
==================

동일한 ``Styles.xml`` 에 ``<item>`` 을 변경해주면된다.

.. code:: xml

   <item name="android:windowFullscreen">ture</item>

참고 사이트
-----------

* `전체화면 사용하기`_

.. _전체화면 사용하기: http://www.androidpub.com/4710
