Title: [번역] PSR-2: Coding Style Guide
Date: 2019-02-05 02:02:45
Modified: 2019-03-23 16:45:00
Category: Develop
Tags: php, psr, prs-2, transelate
Slug: psr-2:_coding_style_guide
Summary: PSR-2, 코딩 스타일 가이드. PSR-1 내용에서 확장하여 정리하고 있다.

[PSR-2: Coding Style Guide - PHP-FIG](https://www.php-fig.org/psr/psr-2/)

---

이 가이드는 기본 코딩 표준인 PSR-1을 확장하여 설명합니다.

> This guide extends and expands on [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md), the basic coding standard.

이 가이드의 목표는 다른 개발자가 코드를 읽을 때, 인지 마찰을 줄이는 것입니다. 그 방법으로 PHP 코드 형식을 지정하는 방법에 대한 규칙과 예외 사항을 열거하는 것입니다.

> The intent of this guide is to reduce cognitive friction when scanning code from different authors. It does so by enumerating a shared set of rules and expectations about how to format PHP code.

이 스타일 규칙들은 여러 커뮤니티 회원들의 프로젝트들 간의 공통점을 정리하였습니다. 다양한 개발자들이 여러 프로젝트에서 공통 작업을 할 때, 모든 프로젝트에서 사용하는 묶음 지침을 사용하는 것이 편합니다. 따라서 이 가이드의 좋은 점은 규칙 자체가 아니라 이 규칙들을 공유하는 것에 의의를 둡니다.

> The style rules herein are derived from commonalities among the various member projects. When various authors collaborate across multiple projects, it helps to have one set of guidelines to be used among all those projects. Thus, the benefit of this guide is not in the rules themselves, but in the sharing of those rules.

이 문서에서 사용하는 키워드 "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL"은 [RFC 2119](https://techhtml.github.io/rfc/RFC2119.html)에서 설명하는 대로 해석한다.

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”,“SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

# 1. 개요

- [MUST] 코드는 PSR "코딩 스타일 가이드" [PSR-1]에 따릅니다.

    > Code MUST follow a “coding style guide” PSR [[PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md)].

- [MUST] 코드는 인던트를 스페이스 4를 사용합니다. 탭을 사용하지 않습니다.

    > Code MUST use 4 spaces for indenting, not tabs.

- [MUST NOT] 줄 길이에 대한 엄격한 제한이 있어서는 안 됩니다; [MUST] 가벼운 제한은 반드시 120자여야 합니다; [SHOULD] 라인의 길이는 80자 이하여야 합니다.

    > There MUST NOT be a hard limit on line length; the soft limit MUST be 120 characters; lines SHOULD be 80 characters or less.

- [MUST] `namespace` 선언 다음에는 빈 줄이 하나 있어야 합니다; [MUST] `use` 선언한 블록 다음에는 빈 줄이 하나 있어야 합니다.

    > There MUST be one blank line after the `namespace` declaration, and there MUST be one blank line after the block of `use` declarations.

- [MUST] 클래스 여는 중괄호는 반드시 다음 줄로 가야 합니다; [MUST] 닫는 중괄호는 본문 뒤에 오는 다음 줄로 가야 합니다.

    > Opening braces for classes MUST go on the next line, and closing braces MUST go on the next line after the body.

- [MUST] 메서드를 여는 중괄호는 반드시 다음 줄로 가야 합니다; [MUST] 닫는 중괄호는 반드시 본문 맨 끝에서 다음 줄로 가야 합니다.

    > Opening braces for methods MUST go on the next line, and closing braces MUST go on the next line after the body.

- [MUST] 가시성 (Visibility)는 모든 속성과 메서드에서 반드시 선언되어야 합니다; [MUST] `abstract` 와 `final` 은 가시성 이전에 반드시 선언되어야 합니다; [MUST] `static` 은 반드시 가시성 뒤에 선언되어야 합니다.

    > Visibility MUST be declared on all properties and methods; `abstract` and `final` MUST be declared before the visibility; `static` MUST be declared after the visibility.

- [MUST] 제어 구조 키워드 뒤에는 반드시 공백을 가져야 합니다; [MUST NOT] 메서드와 펑션 사용할 때는 공백을 추가해서는 안됩니다.

    > Control structure keywords MUST have one space after them; method and function calls MUST NOT.

- [MUST] 제어 구조에서 여는 중괄호는 반드시 같은 줄에 있어야 합니다. [MUST] 닫는 괄호는 반드시 본문 뒤의 다음 줄로 가야 합니다.

    > Opening braces for control structures MUST go on the same line, and closing braces MUST go on the next line after the body.

- [MUST NOT] 제어 구조에서 여는 괄호 뒤에는 공백이 없어야 합니다. [MUST NOT] 제어 구조에서 닫는 괄호 전에는 공백이 없어야 합니다.

    > Opening parentheses for control structures MUST NOT have a space after them, and closing parentheses for control structures MUST NOT have a space before.

## 1.1 예제

아래의 예는 위의 규칙 중 일부를 간략하게 설명합니다:

> This example encompasses some of the rules below as a quick overview:

```php
<?php
namespace Vendor\Package;

use FooInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class Foo extends Bar implements FooInterface
{
    public function sampleMethod($a, $b = null)
    {
    	if ($a === $b) {
            bar();
    	} elseif ($a > $b) {
            $foo->bar($arg1);
    	} else {
            BazClass::bar($arg2, $arg3);
        }
    }

    final public static function bar()
    {
        // method body
    }
}
```

# 2. 일반적인 것들

## 2.1. 기본 코딩 표준

[MUST] 코드는 반드시 [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md)에 표기된 모든 규칙을 따라야 합니다.

> Code MUST follow all rules outlined in [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md).

## 2.2. 파일

[MUST] 모든 PHP 파일은 반드시 Unix LF (linefeed) 줄 끝 문자를 사용해야 합니다.

> All PHP files MUST use the Unix LF (linefeed) line ending.

[MUST] 모든 PHP 파일은 반드시 하나의 빈 줄로 끝나야 합니다.

> All PHP files MUST end with a single blank line.

[MUST] 닫는 태그인 `?>` 태그는 PHP만 포함된 파일에서는 생각해야 합니다.

> The closing `?>` tag MUST be omitted from files containing only PHP.

## 2.3. 줄

[MUST NOT] 라인 길이에는 엄격한 제한이 있어서는 안 됩니다.

> There MUST NOT be a hard limit on line length.

[MUST] 줄 길이에 대한 가벼운 제한은 120자입니다; [MUST] 자동화된 스타일 체커는 반드시 경고해야 합니다만 [MUST NOT] 가벼운 제한을 오류로 표현해서는 안됩니다.

> The soft limit on line length MUST be 120 characters; automated style checkers MUST warn but MUST NOT error at the soft limit.

[SHOLD NOT] 행은 80자를 넘지 않아야 합니다; [SHOULD] 그보다 긴 행은 각각 80자 이하의 여러 행으로 나눠야 합니다.

> Lines SHOULD NOT be longer than 80 characters; lines longer than that SHOULD be split into multiple subsequent lines of no more than 80 characters each.

[MUST NOT] 비어 있지 않은 줄 끝에는 공백 문자가 없어야 합니다.

> There MUST NOT be trailing whitespace at the end of non-blank lines.

[MAY] 가독성을 높이고 관련 코드 블록을 나타내기 위해 빈 줄을 추가할 수 있습니다.

> Blank lines MAY be added to improve readability and to indicate related blocks of code.

[MUST NOT] 한 줄에 하나 이상의 문장이 있어서는 안 됩니다.

> There MUST NOT be more than one statement per line.

## 2.4. 들여쓰기

[MUST] 코드는 반드시 4개의 스페이스로 들여 쓰기를 허용해야 하며, [MUST NOT] 들여 쓰기에 탭을 사용하지 않아야 합니다.

> Code MUST use an indent of 4 spaces, and MUST NOT use tabs for indenting.

주의하세요: 탭과 스페이스를 섞어 쓰지 않고 스페이스만 사용한다면, diff, 패치, 이력, 주석에서 발생하는 문제를 피할 수 있습니다. 스페이스를 이용하면 행간 정렬을 위해 세분화된 하위 들여 쓰기를 쉽게 추가할 수 있습니다.

> N.b.: Using only spaces, and not mixing spaces with tabs, helps to avoid problems with diffs, patches, history, and annotations. The use of spaces also makes it easy to insert fine-grained sub-indentation for inter-line alignment.

## 2.5. 키워드와 True/False/Null

[MUST] PHP [키워드](http://php.net/manual/en/reserved.keywords.php)는 반드시 소문자로 표기합니다.

> PHP [keywords](http://php.net/manual/en/reserved.keywords.php) MUST be in lower case.

[MUST] PHP 상수인 `true`, `false`, `null` 은 반드시 소문자로 표기합니다.

> The PHP constants `true`, `false`, and `null` MUST be in lower case.

# 3. Namespace와 사용 선언

[MUST] Namespace가 존재하는 경우, `namespace` 정의된 다음에 한 줄은 비워 둬야 합니다.

> When present, there MUST be one blank line after the `namespace` declaration.

[MUST] Namespace가 존재하는 경우, `namespace` 정의된 이후 라인에 모든 `use` 가 정의되어야 합니다.

> When present, all `use` declarations MUST go after the `namespace` declaration.

[MUST] `use` 키워드는 정의마다 하나씩 있어야 합니다.

> There MUST be one `use` keyword per declaration.

[MUST] `use` 블록 다음에 한 줄을 비워 둬야 합니다.

> There MUST be one blank line after the `use` block.

예를 들어:

> For example:

```php
<?php
namesapce Vender\Package;

use FooClass;
use BarClass as Bar;
use OhterVender\OtherPackage\BazClass;

// ... additinal PHP code ...
```

# 4. 클래스, 속성, 메서드

"class"라는 용어는 모든 클래스, 인터페이스, 특성을 나타냅니다.

> The term “class” refers to all classes, interfaces, and traits.

## 4.1. 확장과 구현

[MUST] `extends` 와 `implements` 키워드는 클래스 이름과 같은 줄에서 선언되어야 합니다.

> The `extends` and `implements` keywords MUST be declared on the same line as the class name.

[MUST] 해당 클래스를 여는 중괄호는 홀로 다음 줄에 있어야 합니다; [MUST] 클래스 닫는 중괄호는 본문 끝 다음 줄에 있어야 합니다.

> The opening brace for the class MUST go on its own line; the closing brace for the class MUST go on the next line after the body.

```php
<?php
namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements \ArrayAccess, \Countable
{
    // constants, properties, methods
}
```

[MAY] `implements` 목록은 여러 줄에 걸쳐 나눠질 수 있으며, 각 줄은 한 번만 들여 써질 수 있습니다. [MUST] 그렇게 표현할 때, 목록의 첫 번째 항목은 다음 줄에 있어야 하며, [MUST] 한 줄에 하나의 인터페이스만 있어야 합니다.

> Lists of `implements` MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one interface per line.

```php
<?php
namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements\ArrayAccess, \Countable, \Serializable
{
    // constants, properties, methods
}
```

## 4.2. 속성

[MUST] 모든 속성에서 가시성을 반드시 선언해야 합니다.

> Visibility MUST be declared on all properties.

[MUST NOT] 속성을 선언하는데 `var` 키워드를 사용하면 안 됩니다.

> The `var` keyword MUST NOT be used to declare a property.

[MUST NOT] 명령문마다 하나 이상의 속성이 선언해서는 안 됩니다.

> There MUST NOT be more than one property declared per statement.

[SHOULD NOT] protected 나 private 가시성을 나타내기 위해 `_` 로 속성 이름을 시작하면 안 됩니다.

> Property names SHOULD NOT be prefixed with a single underscore to indicate protected or private visibility.

속성 선언은 다음과 같습니다.

> A property declaration looks like the following.

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public $foo = null;
}
```

## 4.3. 메서드

[MUST] 모든 메서드는 가시성을 선언해야 합니다.

> Visibility MUST be declared on all methods.

[SHOULD NOT] protected 나 private 가시성을 나타내기 위해 `_` 로 메서드 이름을 시작하면 안 됩니다.

> Method names SHOULD NOT be prefixed with a single underscore to indicate protected or private visibility.

[MUST NOT] 메서드 이름 뒤에 스페이스를 추가해서는 안 됩니다. [MUST] 여는 중괄호는 반드시 메서드 선언 다음 줄에 있어야 하고, [MUST] 닫는 중괄호는 그 다음 줄에 있어야 합니다. [MUST NOT] 여는 중괄호 뒤에 스페이스가 있어서 안되며, [MUST NOT] 닫는 괄호 앞에 스페이스가 있어서는 안됩니다.

> Method names MUST NOT be declared with a space after the method name. The opening brace MUST go on its own line, and the closing brace MUST go on the next line following the body. There MUST NOT be a space after the opening parenthesis, and there MUST NOT be a space before the closing parenthesis.

메서드 선언은 다음과 같습니다. 괄호, 쉼표, 스페이스, 중괄호의 배치에 조심해서 사용합니다:

> A method declaration looks like the following. Note the placement of parentheses, commas, spaces, and braces:

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function fooBarBaz($arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

## 4.4. 메서드 인수

인수 목록에서는 [MUST NOT] 쉼표 앞에 공백이 있으면 됩니다. [MUST]  쉼표 뒤에 공백을 두어야 합니다.

> In the argument list, there MUST NOT be a space before each comma, and there MUST be one space after each comma.

[MUST] 기본 값을 가진 메서드 인수는 인수 목록의 마지막에 위치해야 합니다.

> Method arguments with default values MUST go at the end of the argument list.

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function foo($arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

[MAY] 인수 목록은 여러 줄에 걸쳐 나눌 수 있으며, 각 줄은 한 번만 들여 쓰기 할 수 있습니다. [MUST] 여러 줄로 나눠 표기할 때는 첫 번째 항목은 다음 줄에 있어야 합니다. [MUST] 한 줄에 하나의 인수만 있어야 합니다.

> Argument lists MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one argument per line.

[MUST] 인수 목록이 여러 줄에 걸쳐 분할되어 있으면, 닫는 괄호와 여는 괄호는 스페이스 하나로 하나의 라인에 같이 있어야 합니다.

> When the argument list is split across multiple lines, the closing parenthesis and opening brace MUST be placed together on their own line with one space between them.

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function aVeryLongMethodName(
        ClassTypeHint $arg1,
        &$arg2,
        array $arg3 = []
    ) {
        // method body
    }
}
```

## 4.5. abstract, final, static

[MUST] `abstract` 와 `final` 선언은 가시성 선언 앞에 와야 합니다.

> When present, the `abstract` and `final` declarations MUST precede the visibility declaration.

[MUST] `static` 선언은 가시성 선언 뒤에 와야 합니다.

> When present, the `static` declaration MUST come after the visibility declaration.

```php
<?php
namespace Vendor\Package;

abstract class ClassName
{
    protected static $foo;

    abstract protected function zim();

    final public static function bar()
    {
        // method body
    }
}
```

## 4.6. 메서드와 펑션 사용

[MUST NOT] 메서드나 함수 호출을 할 경우, 메서드 상에 공백이 없어야 합니다. 또는 [MUST NOT] 함수 이름과 여는 괄호 뒤에는 공백이 있어서는 안 됩니다. 그리고 [MUST NOT] 닫는 괄호 앞에는 공백이 없어야 합니다. [MUST NOT] 인수 목록에는 쉼표 앞에 공백이 있어서 안되며, [MUST] 쉼표 뒤에 공백이 와야 합니다.

> When making a method or function call, there MUST NOT be a space between the method or function name and the opening parenthesis, there MUST NOT be a space after the opening parenthesis, and there MUST NOT be a space before the closing parenthesis. In the argument list, there MUST NOT be a space before each comma, and there MUST be one space after each comma.

```php
<?php
bar();
$foo->bar($arg1);
Foo::bar($arg2, $arg3);
```

[MAY] 인수 목록은 여러 줄에 걸쳐 나눠질 수 있으며, 각 줄은 한번 들여 쓰일 수 있습니다. [MUST] 이렇게 할
 때 목록의 첫 번째 항목은 다음 줄에 있어야 합니다. [MUST] 한 줄에 하나의 인수만 있어야 합니다.

> Argument lists MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one argument per line.

```php
<?php
$foo->bar(
    $longArgument,
    $longerArgument,
    $muchLongerArgument
);
```

# 5. 제어문

제어문에 대한 일반적인 스타일 규칙은 다음과 같습니다:

> The general style rules for control structures are as follows:

- [MUST] 제어문 키워드 다음에 스페이스가 하나 있어야 합니다.

    > There MUST be one space after the control structure keyword

- [MUST NOT] 여는 괄호 뒤에 스페이스가 있어서는 안 됩니다.

    > There MUST NOT be a space after the opening parenthesis

- [MUST NOT] 닫는 괄호 앞에 스페이스가 있어서는 안 됩니다.

    > There MUST NOT be a space before the closing parenthesis

- [MUST] 닫는 괄호와 여는 중괄호 사이에 스페이스가 하나 있어야 합니다.

    > There MUST be one space between the closing parenthesis and the opening brace

- [MUST] 제어문 내부는 반드시 한번 들여 쓰기 해야 합니다.

    > The structure body MUST be indented once

- [MUST] 닫는 중괄호는 제어문이 끝나는 다음 줄에 있어야 합니다.

    > The closing brace MUST be on the next line after the body

[MUST] 제어문 본체는 중괄호로 묶어야 합니다. 중괄호를 이용하여 제어문이 어떻게 보여줄지를 표준화하고, 개행이 되었을 때, 오류가 발생할 가능성을 줄여 줍니다.

> The body of each structure MUST be enclosed by braces. This standardizes how the structures look, and reduces the likelihood of introducing errors as new lines get added to the body.

## 5.1. if, elseif, else

`if` 문 구조는 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다. `else` 와 `elseif` 는 이전 문구의 닫는 중괄호와 같은 줄에 있습니다.

> An `if` structure looks like the following. Note the placement of parentheses, spaces, and braces; and that `else` and `elseif` are on the same line as the closing brace from the earlier body.

```php
<?php
if ($expr1) {
    // if body
} elseif ($expr2) {
    // elseif body
} else {
    // else body;
}
```

[SHOULD] `else if` 대신 `elseif` 키워드를 사용하여 모든 제어 키워드가 단일 단어처럼 보이도록 해야 합니다.

> The keyword `elseif` SHOULD be used instead of `else if` so that all control keywords look like single words.

## 5.2. switch, case

`switch` 문의 구조는 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다. [MUST] `case` 문은 `switch` 보다 한번 들여 쓰기가 되어야 합니다. [MUST] `break` 키워드 (또는 다른 종료 키워드)는 `case` 문과 같은 수준에서 들여 쓰기가 되어야 합니다. [MUST] 비어 있지 않은 `case` 문에서 다음 문으로 넘어가야 될 경우, `// no break` 와 같은 주석이 있어야 합니다.

> A `switch` structure looks like the following. Note the placement of parentheses, spaces, and braces. The `case` statement MUST be indented once from `switch`, and the `break` keyword (or other terminating keyword) MUST be indented at the same level as the `case` body. There MUST be a comment such as `// no break` when fall-through is intentional in a non-empty `case` body.

```php
<?php
switch ($expr) {
    case 0:
        echo 'First case, with a break';
        break;
    case 1:
        echo 'Second case, which falls through';
        // no break
    case 2:
    case 3:
    case 4:
        echo 'Third case, return instead of break';
        return;
    default:
        echo 'Default case';
        break;
}
```

## **5.3. while, do while**

`while` 문은 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> A `while` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```php
<?php
while ($expr) {
    // structure body
}
```

마찬가지로 `do while` 문은 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> Similarly, a `do while` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```php
<?php
do {
    // structure body;
} while ($expr);
```

## **5.4. for**

`for` 문은 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> A `for` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```php
<?php
for ($i = 0; $i < 10; $i++) {
    // for body
}
```

## **5.5. foreach**

`foreach` 문은 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> A `foreach` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```php
<?php
foreach ($iterable as $key => $value) {
    // foreach body
}
```

## **5.6. try, catch**

`try catch` 블록은 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> A `try catch` block looks like the following. Note the placement of parentheses, spaces, and braces.

```php
<?php
try {
    // try body
} catch (FirstExceptionType $e) {
    // catch body
} catch (OtherExceptionType $e) {
    // catch body
}
```

# 6. Closures

[MUST] 클로저는 `function` 키워드 뒤에 공백과 `use` 키워드 앞뒤 공백으로 선언해야 합니다.

> Closures MUST be declared with a space after the `function` keyword, and a space before and after the `use` keyword.

[MUST] 여는 중괄호는 반드시 같은 줄에 있어야 하며, [MUST] 닫는 중괄호는 반드시 그다음 줄에 있어야 합니다.

> The opening brace MUST go on the same line, and the closing brace MUST go on the next line following the body.

[MUST NOT] 인수 목록이나 변수 목록에서의 여는 괄호 뒤에는 공백이 있어서는 안 되며, [MUST NOT] 닫는 괄호 앞에서도 공백이 있어서는 안 됩니다.

> There MUST NOT be a space after the opening parenthesis of the argument list or variable list, and there MUST NOT be a space before the closing parenthesis of the argument list or variable list.

[MUST NOT] 인수 목록과 변수 목록에 있는 쉼표 앞에는 스페이스가 있어서는 안되며, [MUST] 쉼표 뒤에 스페이스가 들어가야 합니다.

> In the argument list and variable list, there MUST NOT be a space before each comma, and there MUST be one space after each comma.

[MUST] 기본 값을 가진 클로저 인수는 인수 목록의 끝에 와야합니다.

> Closure arguments with default values MUST go at the end of the argument list.

클로저는 다음과 같습니다. 괄호, 공백, 중괄호의 위치를 유의해서 보시길 바랍니다.

> A closure declaration looks like the following. Note the placement of parentheses, commas, spaces, and braces:

```php
<?php
$closureWithArgs = function ($arg1, $arg2) {
    // body
};

$closureWithArgsAndVars = function ($arg1, $arg2) use ($var1, $var2) {
    // body
};
```

[MAY] 인수 목록과 변수 목록은 여러 행에 걸쳐 나눠질 수 있습니다. (각 행은 한번 들여 쓰기가 들어가야 합니다.) 그렇게 할때, [MUST] 목록의 첫 번째 항목은 다음 줄에 있어야 하며, [MUST] 한 줄에 하나의 인수나 변수만 있어야 합니다.

> Argument lists and variable lists MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one argument or variable per line.

[MUST] (인수이거나 변수일때) 마지막 리스트가 여러 줄로 나눠질 경우, 닫는 괄호와 여는 중괄호는 같은 줄에 공백으로 나눠져 있어야 합니다.

> When the ending list (whether of arguments or variables) is split across multiple lines, the closing parenthesis and opening brace MUST be placed together on their own line with one space between them.

다음은 인수 목록이 있거나 없는 클로저의 예와 여러 줄로 표현된 변수 목록에 대한 예제입니다.

> The following are examples of closures with and without argument lists and variable lists split across multiple lines.

```php
<?php
$longArgs_noVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) {
    // body
};

$noArgs_longVars = function () use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
    // body
};

$longArgs_longVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
    // body
};

$longArgs_shortVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use ($var1) {
    // body
};

$shortArgs_longVars = function ($arg) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
    // body
};
```

형식 지정 규칙은 함수 또는 메서드 호출에서 클로저가 직접 인수로 사용될 때에도 적용됩니다.

> Note that the formatting rules also apply when the closure is used directly in a function or method call as an argument.

```php
<?php
$foo->bar(
    $arg1,
    function ($arg2) use ($var1) {
        // body
    },
    $arg3
);
```

# 7. Conclusion

이 가이드에서 의도적으로 생략한 스타일과 연습해야 될 많은 요소들이 있습니다. 다음 내용들이 포함되지만 이 내용에 국한되지 않습니다:

> There are many elements of style and practice intentionally omitted by this guide. These include but are not limited to:

- 전역 변수, 전역 상수 선언

    > Declaration of global variables and global constants

- 함수 선언

    > Declaration of functions

- 연산자와 할당자

    > Operators and assignment

- 라인간 정렬

    > Inter-line alignment

- 주석과 문서 블록

    > Comments and documentation blocks

- 클래스 이름 접두사와 접미사

    > Class name prefixes and suffixes

- 모범 사례

    > Best practices

[MAY] 향후 권장 사항은 스타일이나 연습해야 될 많은 요소들을 다루기 위해 이 가이드를 수정하고 확장할 수 있습니다.

> Future recommendations MAY revise and extend this guide to address those or other elements of style and practice.
