Title: RSYSLOG - Templates
Date: 2018-03-01 18:45:41
Category: Operation
Tags: syslog, rsyslog, log, system, linux
Slug: rsyslog_-_templates
Summary: Rsyslog 에서 사용되는 template 에 관련된 내용을 정리합시다.

`/var/log/syslog`로 모여드는 서비스들의 로그를 다른 곳으로 옮기고, 해당 내용을 확인하기 위해 파싱을 할 수 있도록 변경하는 작업이 필요했다.
그래서 내가 필요한 로그를 syslog에서 때어낸후 다른 파일로 옮기는 작업을 성공. 하지만 그 이상의 작업을 하기위해서는 rsyslog에서 template을 작성하여야 내가 필요한 메시지만 작성할 수 있는 것을 확인하였기에 해당 부분을 찾아 변경하였다.

그러면서 참고하려고 했던 문서들이 전부 영문이라. 한국어로 내가 정리해두고 나중에 또 찾아봐야겠다는 생각에서 글을 작성한다.

## Template

Rsyslog에서는 기본적인 포맷이 아닌 사용자가 필요한 내용으로 포맷을 변경할 수 있는 옵션을 제공한다.

작성하는 포맷은 두가지가 있으며, 검색해보면 전부 Legacy 포맷으로 적도록 되어있으니 두개는 보기 편한걸로 작성해두면 될것으로 보인다.

### `template()` statement 
문서상으로는 7버전 이상에서 사용할 수 있는 포맷이다.

아래의 예제는 파일에 로그를 작성하는 기본 템플릿이다.

```
template(name="FileFormat" type="list") {
	property(name="timestamp" dateFormat="rfc3339")
	constant(value=" ")
	property(name="hostname")
	constant(value=" ")
	property(name="syslogtag")
	property(name="msg" spifno1stsp="on" )
	property(name="msg" droplastlf="on" )
	constant(value="\n")
	}
```

작성된 템플릿을 이용해서 분석해보자.

* `template(parameters) { list-descriptions }`
	* 이런 구조로 작성된다.

#### `parameters`

* `name`: 해당 템플릿의 이름이다.
* `type`: 템플릿을 어떤 용도로 사용할 것인가에 대한 내용을 작성한다고 보면된다.
* `option`: 템플릿을 어떤 형식으로 출력할 것인지에대해서 추가로 정할 수 있다.

##### `type`

* [`list`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#list)
	* [`constant`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#constant-statement)
		* 상수 텍스트에 대한 내용들을 작성한다.
		* `\n`, `\ooo`, `\xhh`, ` ` 와 같은 내용들을 작성해 둘 수 있다.
		* 그리고 다음 파라미터를 입력하여 사용할 수도 있다.
			* `value` - 사용하는 상수 값
			* `outname` - 출력 필드 이름
			* `format` - `jsonf`나 그냥 빈칸
	* [`property`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#property-statement)
		* 속성에 대한 내용들을 작성한다.
		* 해당 내용은 종류가 많아서 넘어간다.
		* Legacy format에서 `%property%` 형식으로 들어가는 내용과 동일하다고 보면 될것같다.
* [`subtree`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#subtree)
	* 7.4.1 버전이후로 나온 타입이다.
	* 예제를 보면 더 쉽게 알수 있을 것이다.

```
set $!usr!tpl2!msg = $msg;
set $!usr!tpl2!dataflow = field($msg, 58, 2);
template(name="tpl2" type="subtree" subtree="$!usr!tpl2")
```

* [`string`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#string)
	* Lagacy format 형식으로 쭉 적는거다.
	* 예제를 보자

```
template(name="tpl3" type="string"
         string="%TIMESTAMP:::date-rfc3339% %HOSTNAME% %syslogtag%%msg:::sp-if-no-1st-sp%%msg:::drop-last-lf%\n"
        )
```

* [`plugin`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#plugin)
	* 플러그인을 만들때 사용한다고 하는데... 쓸일이 있을까??

#### [`option`](http://www.rsyslog.com/doc/v8-stable/configuration/templates.html#options)

예제로 이해하자. 필요하면 링크를 타고 보고.

```
template(name="outfmt" type="list" option.jsonf="on") {
         property(outname="@timestamp" name="timereported" dateFormat="rfc3339" format="jsonf")
         property(outname="host" name="hostname" format="jsonf")
         property(outname="severity" name="syslogseverity-text" caseConversion="upper" format="jsonf")
         property(outname="facility" name="syslogfacility-text" format="jsonf")
         property(outname="syslog-tag" name="syslogtag" format="jsonf")
         property(outname="source" name="app-name" format="jsonf")
         property(outname="message" name="msg" format="jsonf")

 }
```

이렇게 작성하면,

```
{
  "@timestamp": "2018-03-01T01:00:00+00:00",
  "host": "172.20.245.8",
  "severity": "DEBUG",
  "facility": "local4",
  "syslog-tag": "tag",
  "source": "tag",
  "message": " msgnum:00000000:"
}
```

### Legacy Format

6 이전 버전에서 사용하던 포멧이다. rsyslog template으로 해서 검색을 하면 가장 많이 나오는 포멧. 공식 문서에서는 사용하지 않을 것을 권고하고있다.

아래의 예제는 파일에 로그를 작성하는 기본 템플릿이다.

```
$template FileFormat,"%TIMESTAMP:::date-rfc3339% %HOSTNAME% %syslogtag%%msg:::sp-if-no-1st-sp%%msg:::drop-last-lf%\n"
```

작성 요령은 `$template` 변수, `template 이름`, `"%PROPERTY_NAME[:FROM_CHAR:TO_CHAR:OPTION]%"`. 필요한 내용들을 작성하면된다.

* `Property` 내용은 [도큐먼트](http://www.rsyslog.com/doc/v8-stable/configuration/properties.html)에 작성되어있다.
* `FROM_CHAR`, `TO_CHAR` 부분은 어디서 어디까지... `%msg:1:2%`라고 작성했다면 메시지에서 첫번째 문자에서 두번째 문자까지 보여달라고 하는것. `FROM_CHAR` 을 작성하고 맨끝열까지 하고 싶다면, `TO_CHAR`에다가 숫자가 아닌 `$`를 입력하면 문자열의 맨마지막까지 보여주게 된다.
	* `FROM_CHAR` 부분에 `F` 입력
		* `%msg:F:2%` 라고 입력하면 `test\tchar`라면 `[test, char]`로 분리하고 `char`만 보여주게된다.
		* `F,ASCII_CODE`로 입력하면, 해당 문자로 나누게 된다.
	* `FROM_CHAR` 부분에 `R` 입력
		* 정규식을 사용한다는 것.
		* 해당 내용은 man 페이지를...
* `OPTION`은 [man 페이지](http://manpages.ubuntu.com/manpages/xenial/en/man5/rsyslog.conf.5.html) Property Options 항목을 확인하자.


### 동적 파일 이름 생성

두가지 방식이 있다만, 첫번째 방식으로 작성해서 템플릿 구성을 맞추는게 좋을것으로 보인다.

```
template (name="DynFile" type="string" string="/var/log/system-%HOSTNAME%.log")

$template DynFile,"/var/log/system-%HOSTNAME%.log"
```

## 결.

Rsyslog는 지금 리눅스에서 기본적으로 사용되는 System logging 프로그램이다. 그렇기에 사용하기가 쉽고 쉽게 다가갈 수 있다.
이런 것으로 우선 1차 정리하고 더 설정할 수 없는 것들은 프로그램에서 정리를 하거나 다른 프로그램을 사용하거나 해도 될듯. 무작정 패키지를 추가할 수 없는 시스템에서는 어쩔 수 없는 선택이긴하다만...

삽질한 내용을 작성해 두려고 한건데... 글쓰는데 더 삽질을... ㅡ.ㅡa

다음번엔 원격 서버로 로컬 서버 로그를 넘기는 방법에 대해서 정리를 해볼까... 이 내용은 많던데...

## 참고 페이지

* [rsyslog doc homepage](http://www.rsyslog.com/doc)
