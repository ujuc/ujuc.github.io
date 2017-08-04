Title: Scala에서 val, var 차이
Date: 2017-08-04 11:07:25
Category: Develop
Tags: scala, value
Slug: scalae-seo_val,_var_ca-i
Summary: Scala에서 `var`, `val`의 차이가 궁금해졌다.

요세 Java를 공부하기는 싫고 JVM에서 도는 걸 찾다가. Scala쪽으로 어떤분이 약을 파셔서 약을먹었다.

초기 공부는 역시 홈페이지에 있는 문서를 기반으로... [Scala Tour](http://docs.scala-lang.org/tour/tour-of-scala.html) 를 보다 [Classes](http://docs.scala-lang.org/tour/classes.html)에 갔더니 예제로 다음 과 같은 내용이 있었다.

```scala
class Point(var x: Int, var y: Int) {
    def move(dx: Int, dy: Int): Unit = {
        x = x + dx
        y = y + dy
    }

    override def toString: String = 
        s"($x, $y)"
}

val point1 = new Point(2, 3)
point1.x    // 2
println(point1)     // prints (x, y)
```

변수를 초기화하는데 `var`랑 `val`이 같이 쓰였다. 느낌상으로는 `var`, `val`이나 동일할꺼같은데 같은걸 다른곳에서 다르게 사용할 필요가 없을꺼니 구글검색.

[Use of def, val, and var in scala](https://stackoverflow.com/questions/4437373/use-of-def-val-and-var-in-scala)

역시 나랑 같은 생각을 하는 사람이 있을 줄알았지. 그것도 영어잘하는 :). 그런데 여기는 `def`도 들어가있다. 메소드는 왜... 메소드를 할당할때에도 쓸수 있어서 그런건가..
암튼 답변 내용은 다음과 같다.

* `def`: 메소드, *immutable label*, **lazily evaluated**

```scala
scala> def something = 2 + 3 * 4
something: Int

scala> something
res2: Int = 14

scala> something = 10
<console>:12: error: value something_= is not a member of object $iw
       something = 10
       ^
```

* `val`: 상수, *immutable label*, **eagerly/immediately evaluated**

```scala
scala> val somethingelse = 2 + 3 * 5
somethingelse: Int = 17

scala> something = 4 * 10
<console>:12: error: value something_= is not a member of object $iw
       something = 4 * 10
       ^
```

* `var`: 변수, *mutable variable*

```scala
scala> var aVariable = 2 * 3
aVariable: Int = 6

scala> aVariable = 5
aVariable: Int = 5
```

개인적으로는 [두번째 답](https://stackoverflow.com/a/33066906/978762)이 마음에 든다. 
