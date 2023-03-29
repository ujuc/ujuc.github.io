Title: [번역] PSR-1: Basic Coding Standard
Date: 2018-11-17 12:11:55
Modified: 2019-03-22 16:50:00
Category: Develop
Tags: php, psr-1, psr, transelate
Slug: psr-1:_basic_coding_standard
Summary: PSR-1, 기본 코딩 표준 번역

[PSR-1: Basic Coding Standard - PHP-FIG](https://www.php-fig.org/psr/psr-1/)

---

이 표준에 대한 섹션은 공유하는 PHP 코드 간의 높은 수준의 기술적인 상호 운용성을 보장하기 위해 표준 코딩 요소로 간주되어야 하는 것에 대해서 설명합니다.

> This section of the standard comprises what should be considered the standard coding elements that are required to ensure a high level of technical interoperability between shared PHP code.

이 문서에서 사용하는 키워드 "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL"은 [RFC 2119](https://techhtml.github.io/rfc/RFC2119.html)에서 설명하는 대로 해석한다.

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”,“SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

## 1. 개요

- [MUST] 파일은 `<?php` 와 `<?=` 태그만 사용해야 합니다.

    > Files MUST use only `<?php` and `<?=` tags.

- [MUST] 파일은 PHP 코드에 BOM 없이 UTF-8만 사용해야 합니다.

    > Files MUST use only UTF-8 without BOM for PHP code.

- [SHOULD] 파일에는 심벌 (classes, functions, constants, 등)을 선언*하거나* 사이드 이펙트 (예, 출력 생성, .ini 설정 변경, 등)을 발생시키는 작업 중 하나만 하여야 합니다. [SHOULD NOT] 둘이 같이 선언되면 안됩니다.

    > Files SHOULD *either* declare symbols (classes, functions, constants, etc.) *or* cause side-effects (e.g. generate output, change .ini settings, etc.) but SHOULD NOT do both.

- [MUST] Namespaces와 classes는 반드시 "autoloading" 해야 합니다. PSR: [[~~PSR-0~~](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md), [PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)]

    > Namespaces and classes MUST follow an “autoloading” PSR: [[PSR-0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md), [PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)].

- [MUST] 클레스 이름은 반드시 `StudlyCaps` 로 선언되어야 합니다.

    > Class names MUST be declared in `StudlyCaps`.

- [MUST] 클래스 상수는 모두 대문자로 밑줄 구분 기호로 선언해야 합니다.

    > Class constants MUST be declared in all upper case with underscore separators.

- [MUST] 메소드 이름은 `camelCase` 로 선언되어야 합니다.

    > Method names MUST be declared in `camelCase`.

## 2. 파일

### 2.1. PHP 태그

[MUST] PHP 코드는 긴 태그인 `<?php ?>` 또는 짧은 에코 태그 `<?= ?>` 를 사용해야 합니다. 다른 태그 변형을 사용해서는 안됩니다.
    
> PHP code MUST use the long `<?php ?>` tags or the short-echo `<?= ?>` tags; it MUST NOT use the other tag variations.

### 2.2 문자 인코딩

[MUST] PHP 코드는 [BOM(Byte Order Mark)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%ED%8A%B8_%EC%88%9C%EC%84%9C_%ED%91%9C%EC%8B%9D) 없이 UTF-8 만 사용해야 합니다.

> PHP code MUST use only UTF-8 without BOM.

### 2.3 부작용 (Side Effects)

[SHOULD] 파일은 새로운 심벌 (클래스, 함수, 상수 등)을 선언하고 다른 사이드 이펙트를 일으키지 않아야 합니다. [SHOULD] 또는 파일에서 사이트 이펙트를 줄 수 있는 로직이 포함될 수 있습니다. [SHOULD NOT] 그러나 이 두 가지가 모두 발생하지 않아야 합니다.

> A file SHOULD declare new symbols (classes, functions, constants,etc.) and cause no other side effects, or it SHOULD execute logic with side effects, but SHOULD NOT do both.

"Side effects" 라는 말은 클래스, 함수, 상수 등을 선언하는 것과 직접적으로 관련없는 로직 실행을 *단지 파일에 포함하는 것*을 의미 합니다.

> The phrase “side effects” means execution of logic not directly related to declaring classes, functions, constants, etc., *merely from including the file*.

"Side effects"에는 다음 내용들이 포함되지만 이것만 있는 것은 아닙니다: 출력 생성, `require` 또는 `include` 의 명시적 사용, 외부 서비스 연결, ini 설정 수정, 에러 출력 또는 예외, 전역 또는 정적 변수 수정, 파일 읽기나 쓰기 등등...

> “Side effects” include but are not limited to: generating output, explicit use of `require` or `include`, connecting to external services, modifying ini settings, emitting errors or exceptions, modifying global or static variables,reading from or writing to a file, and so on.

다음은 부작용이 모두 포함된 코드의 예입니다. 즉, 피해야 할 예:

> The following is an example of a file with both declarations and side effects;i.e, an example of what to avoid:

```php
<?php
// side effect: change ini settings
ini_set('error_reporting', E_ALL);

// side effect: loads a file
include "file.php";

// side effect: generates output
echo "<html>\n";

// declaration
function foo()
{
    // function body
}
```

다음 예제는 부작용이 없는 내용이 포함된 코드의 예입니다. 즉, 참고해야 할 예:

> The following example is of a file that contains declarations without side effects; i.e., an example of what to emulate:

```php
<?php
// declaration
function foo()
{ 
    // function body
}

// conditional declaration is *not* a side effect
if (! function_exists('bar')) {
    function bar()
    { 
        // function body
    }
}
```

## 3. 네임스페이스(Namespace)와 클래스 이름

[MUST] 네임스페이스와 클래스는 반드시 "autoloading" PSR 문서에 따라야 합니다: [[PSR-0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md), [PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)]

> Namespaces and classes MUST follow an “autoloading” PSR: [[PSR-0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md), [PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)].

각 클래스는 하나의 파일에 있으며, 최상위 벤더 이름인 네임스페이스가 있어야 합니다.

> This means each class is in a file by itself, and is in a namespace of at least one level: a top-level vendor name.

[MUST] 클래스 이름은 반드시 `StudlyCaps` 로 선언되어야 합니다.

> Class names MUST be declared in `StudlyCaps`.

[MUST] PHP 5.3 이후 버전에서 사용될 코드는 정식 네임스페이스를 사용해야 합니다.

> Code written for PHP 5.3 and after MUST use formal namespaces.

For example:

```php
<?php
// PHP 5.3 and later:
namespace Vendor\Model;

class Foo
{
}
```


[SHOULD] 5.2.x 이하에서 작성하는 코드에서는 클래스 이름에 `Vendor_` 접두사를 이용하는 네임스페이스 규칙을 사용해야 합니다.

> Code written for 5.2.x and before SHOULD use the pseudo-namespacing convention of `Vendor_` prefixes on class names.

```php
<?php
// PHP 5.2.x and earlier:

class Vendor_Model_Foo
{
}
```

## 4. 클래스 상수, 속성, 메서드

"Class" 라는 용어는 모든 클래스, 인터페이스, 특성을 나타냅니다.

> The term “class” refers to all classes, interfaces, and traits.

### 4.1 상수 (Constants)

[MUST] 클래스 상수는 모두 대문자로 밑줄 구분 기호를 사용하여 선언해야 합니다. 예:

> Class constants MUST be declared in all upper case with underscore separators. For example:

```php
<?php
namespace Vendor\Model;

class Foo
{
    const VERSION = '1.0';
    const DATE_APPROVED = '2012-06-01';
}
```

### 4.2 속성 (Properties)

이 가이드에서는 `$StudlyCaps`, `$camelCase`, `$under_score` 와 같은 방식으로 속성 이름을 사용하는 것에 대해서 권장 사항을 지정하지 않습니다.

> This guide intentionally avoids any recommendation regarding the use of `$StudlyCaps`, `$camelCase`, or `$under_score` property names.

[SHOULD] 어떤 명명 규칙이 사용되든 합당한 범위 내에서 일관되게 적용되어야 합니다. 여기서 정의하는 범위는 벤더 레벨, 패키지 레벨, 클래스 레벨, 메서드 레벨을 일컷습니다.

> Whatever naming convention is used SHOULD be applied consistently within areasonable scope. That scope may be vendor-level, package-level, class-level,or method-level.

### 4.3 메서드 (Methods)

[MUST] 메서드 이름은 `camleCase()` 방식으로 선언되어야 합니다.

> Method names MUST be declared in `camelCase()`.
