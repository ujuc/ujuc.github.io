Title: Design of QL
Date: 2018-05-24 00:00:02
Modified: 2018-03-23 16:50:00
Category: 번역
Tags: go, database, translate
Slug: design_of_ql
Summary: Go 임베디드 데이터베이스 패키지인 QL에 대한 디자인 문서이다.

`QL` design 문서

이 문서는 [`cznic/ql`](https://github.com/cznic/ql) 프로젝트 설계 문서이다.
`QL` 은 Go로 만들어진 embedded SQL 데이터베이스이다.

**원문**

* code: [doc.go - v1.1.0](https://github.com/cznic/ql/blob/v1.1.0/design/doc.go)
* godoc: [package design](https://godoc.org/github.com/cznic/ql/design)

---

[TOC]

패키지 디자인은 QL에서 사용중인 일부 데이터 구조를 설명합니다.
> Package design describes some of the data structures used in QL.

## Handles

Handle은 DB에서 사용중인 블록에대한 7 바이트 “pointer” 입니다. [`lldb/hdr-Block_handles`][0]
> A handle is a 7 byte "pointer" to a block in the DB [0].

## Scalar encoding

[`lldb/EncodeScalars`][1]에서 제공하는 "scalars" 인코딩을 말합니다. 달리 명시하지 않는한 아래 설명된 모든 값은 scalars, 인코딩된 scalars, scalar 배열에 대한 인코딩 입니다.
> Encoding of so called "scalars" provided by [`lldb/EncodeScalars`][1]. Unless specified otherwise, all values discussed below are scalars, encoded scalars or encoding of scalar arrays.

## Database root

DB root는 고정된 핸들에서 발견되는 1-scalar 입니다 (#1).
> DB root is a 1-scalar found at a fixed handle (#1).

| # | Name |  Type  |     Description       |
| :-: | :-: | :---: | :-------------------: |
| 0 | head | handle | First table meta data |


Head는 메타 데이터 테이블에서 싱클 링크 목록의 제목 행입니다. `0`은 DB에 아무런 테이블이 없을 경우를 나타냅니다.
> Head is the head of a single linked list of table of meta data. It's zero if there are no tables in the DB.

## Table meta data

테이블 메타 데이터는 6-scalar 입니다.
> Table meta data are a 6-scalar.

| # | Name    | Type   |      Description         |
| :-: | :---- | :----- | :----------------------- |
| 0 | next    | handle | Next table meta data.    |
| 1 | scols   | string | Column defintitions      |
| 2 | hhead   | handle | -> head -> first record  |
| 3 | name    | string | Table name               |
| 4 | indices | string | Index definitions        |
| 5 | hxroots | handle | Index B+Trees roots list |

필드 #4와 #5는 기존 데이터베이스와 하위 호환성 (backward compatibility)을 위한 선택 사항입니다. 그러나 상위 호환성(forward compatibility)은 작동하지 않습니다. 최신 QL 버전에서 인덱스를 생성하면 메타 데이터에 4가지 필드만 있을 경우, 이 DB를 사용할 수 없습니다. 이전 버전 QL 인덱스를 업데이트 할 수 없기에 매번 `table-with-indeces` 변화가 될때마다 새로운 QL 버전 쿼리가 실행이 안될 수 있어 의도된 구현입니다.
> Fields #4 and #5 are optional for backward compatibility with existing databases. OTOH, forward compatibility will not work. Once any indices are created using a newer QL version the older versions of QL, expecting only 4 fields of meta data will not be able to use the DB. That's the intended behavior because the older versions of QL cannot update the indexes, which can break queries runned by the newer QL version which expect indices to be always actualized on any table-with-indices mutation.

다음 테이블 메타 데이터의 handle은 필드 #0 (`next`)에 있습니다. 만약 다음 테이블 메타 데이터가 없다면, 이 필드 값은 `0`입니다. 테이블 컬럼에대한 이름과 타입은 필드 #1 (`scols`)에 있습니다. 단일 필드는 타입 태그와 컬럼 이름을 연결하여 설명합니다. 타입 태그는 다음과 같습니다.
> The handle of the next table meta data is in the field #0 (next). If there is no next table meta data, the field is zero. Names and types of table columns are stored in field #1 (scols). A single field is described by concatenating a type tag and the column name. The type tags are

```
bool       'b'
complex64  'c'
complex128 'd'
float32    'f'
float64    'g', alias float
int8       'i'
int16      'j'
int32      'k'
int64      'l', alias int
string     's'
uint8      'u', alias byte
uint16     'v'
uint32     'w'
uint64     'x', alias uint
bigInt     'I'
bigRat     'R'
blob       'B'
duration   'D'
time       'T'
```

Scols 값은 위에서 설명한 인코딩된 필드를 `"|"`로 결합하여 사용합니다. 예를 들어
> The scols value is the above described encoded fields joined using "|". For example

```sql
CREATE TABLE t (Foo bool, Bar string, Baz float);
```

이 문구는 scols를 사용하여 테이블 메타 데이터를 추가합니다.
> This statement adds a table meta data with scols

```
"bFool|sBar|gBaz"
```

테이블에서 컬럼을 삭제할 수 있습니다.
> Columns can be dropped from a table

```sql
ALTER TABLE t DROP COLUMN Bar;
```

이렇게 하면 scols에서 필드 정보가 **지워**집니다. 값은 다음과 같이 보여집니다.
> This "erases" the field info in scols, so the value becomes

```
"bFool||gBaz"
```

테이블에 커럼을 추가할 수 있습니다.
Colums can be added to a table

```sql
ALTER TABLE t ADD Count uint;
```

새로운 필드는 scols 맨 끝에 항상 추가됩니다.
> New fields are always added to the end of scols

```
”bFool||gBaz|xCount"
```

`strings.Split(scols, "|")`에 있는 필드에 대한 인덱스는 테이블 레코드에 있는 필드에 대한 인덱스 입니다. 위에서 설명한 컬럼 삭제 및 추가 규칙은 기존 테이블 데이터를 다시 만들 필요없이 스키마를 변경시킬 수 있습니다. 삭제된 컬럼은 원래 위치에 그대로 두고 새로운 레코드는 해당 위치에 `nil`을 삽입합니다. 인코딩된 `nil` 값은 1 바이트입니다. 기존 레코드에 없는 경우, 추가된 열은  `nil` 값을 반환합니다. 삭제된 컬럼의 오버해드가 문제가되고 테이블 레코드를 이동할 충분한 시간/공간과 메모리가 있다면:
> Index of a field in `strings.Split(scols, "|")` is the index of the field in a table record. The above discussed rules for column dropping and column adding allow for schema evolution without a need to reshape any existing table data. Dropped columns are left where they are and new records insert `nil` in their place. The encoded `nil` is one byte. Added columns, when not present in preexisting records are returned as `nil` values. If the overhead of dropped columns becomes an issue and there's time/space and memory enough to move the records of a table around:

```sql
BEGIN TRANSACTION;
  CREATE TABLE new (column definitions);
  INSERT INTO new SELECT * FROM old;
  DROP TABLE old;
  CREATE TABLE old (column definitions);
  INSERT INTO old SELECT * FROM new;
  DROP TABLE new;
END TRANSACTION;
```

이것은 시간적/공간적으로 효과적이지 못하며, Big Data일 경우, 트랜젝션이 프로세스에서 사용 가능한 메모리 리소스에 의해 제한되기에 OOM 이 발생할 수 있습니다. 어쩌면 이것을 수행하는 메소드나 QL 구문을 추가해야합니다.(MySQL OPTIMIZE TABLE 구문 채택을 고려해야합니다)
> This is not very time/space effective and for Big Data it can cause an OOM because transactions are limited by memory resources available to the process. Perhaps a method and/or QL statement to do this in-place should be added (MAYBE consider adopting MySQL's OPTIMIZE TABLE syntax).

필드 #2(`hhead`)는 테이블 레코드의 해드에 대한 handle 입니다. 테이블 첫 번째 레코드에 대한 handle이 아닙니다. 따라서 레코드가 없는 테이블의 경우라도 항상 `0` 값을 가지고 있지 않습니다. 이 **이중 포인터(double pointer** 스키마를 사용하는 이유는 (`hhead` 포인트에 대한) head 단일 값을 업데이트하여 새 레코드를 추가 (연결) 할 수 있기 때문입니다.
> Field #2 (`hhead`) is a handle to a head of table records, i.e. not a handle to the first record in the table. It is thus always non zero even for a table having no records. The reason for this "double pointer" schema is to enable adding (linking) a new record by updating a single value of the (`hhead` pointing to) head.

```
tableMeta.hhead	-> head	-> firstTableRecord
```

테이블 이름은 필드 #3 (`name`)에 저장됩니다.
> The table name is stored in field #3 (name).

## Indices

인덱스 이름은 'N', 인덱스 컬럼 이름은 'C'으로 정합니다. 이 특정 인덱스 인코딩은 `<tag>N` 문자열입니다. `<tag>`는 고유하지 않은 인덱스는 `n`이고 고유한 인덱스는 `u` 입니다. 인덱스 `id()`와 scols의 다른 모든 컬럼을 인덱싱 할 수 있는 인덱스에 대한 정보기 이 인덱스에 있습니다. 컬럼에 인덱스되지 않은 경우, 인덱스 정보는 빈 문자열입니다. 모든 인덱스에 대한 정보는 `"|"` 으로 결합됩니다. 예를 들어:
> Consider an index named N, indexing column named C. The encoding of this particular index is a string "<tag>N". `<tag>` is a string "n" for non unique indices and "u" for unique indices. There is this index information for the index possibly indexing the record id() and for all other columns of scols. Where the column is not indexed, the index info is an empty string. Infos for all indexes are joined with "|". For example

```sql
BEGIN TRANSACTION;
  CREATE TABLE t (Foo int, Bar bool, Baz string);
  CREATE INDEX X ON t (Baz);
  CREATE UNIQUE INDEX Y ON t (Foo);
COMMIT;
```

위의 필드 #1과 #4는 다음과 같습니다:
> The values of fields #1 and #4 for the above are

```
scols: "lFoo|bBar|sBaz"
indices: "|uY||nX"
```

`"|"` 값을 나눠서 보자면:
> Aligning properly the "|" split parts

```
             id    col#0    col#1    col#2
+----------+----+--------+--------+--------+
|   scols: |    | "lFoo" | "bBar" | "sBaz" |
+----------+----+--------+--------+--------+
| indices: | "" | "uY"   | ""     | "nX"   |
+----------+----+--------+--------+--------+
```

`Foo`와 `Baz` 컬럼이 인덱스되는 동안 레코드 `id()`가 이테이블에 대해 인덱싱되지 않는 것을 보여줍니다.
> shows that the record id() is not indexed for this table while the columns Foo and Baz are.

주의: 동일한 컬럼에 두개의 다른 이름을 가진 인덱스가 있을 수 없으며, 이것은 의도한 것입니다. 인덱스는 [B+Trees][2]로 작성되었습니다. 그들의 루트에서 handle에 대한 목록은 인덱스가 없는 컬럼에 대해서 `0`과 `hxroots`에 의해 가리켜집니다. 이전 예제의 경우:
> Note that there cannot be two differently named indexes for the same column and it's intended. The indices are [B+Trees][2]. The list of handles to their roots is pointed to by `hxroots` with zeros for non indexed columns. For the previous example

```
tableMeta.hxroots -> {0, y, 0, x}
```

여기서 `x`는 `X` 인덱스의 B+Tree에 대한 루트이고, `y`는 `Y` 인덱스의 B+Tree에 대한 루트입니다. `id()`에 대한 인덱스가 있다면, 첫번째 `0`이 있는 곳에 B+Tree 루트가 있습니다. `hhead`와 마찬가지로 `hxroots`는 테이블에 대한 인덱스가 없는 경우라도 절대로 `0`이 아닙니다.
> where x is the root of the B+Tree for the X index and y is the root of the B+Tree for the Y index. If there would be an index for id(), its B+Tree root will be present where the first zero is. Similarly to `hhead`, `hxroots` is never zero, even when there are no indices for a table.

## Table record

테이블 레코드는 N-scalar 입니다.
> A table record is an N-scalar.

|  #  |    Name    |  Type  |      Description              |
| :-: | :--------- | :----- | :---------------------------- |
|  0  | next       | handle | Next record or zero.          |
|  1  | id         | int64  | Automatically assigned unique |
|     |            |        | value obtainable by id().     |
|  2  | field #0   | scalar | First field of the record.    |
|  3  | field #1   | scalar | Second field of the record.   |
| ... | ...        | ...    | ...                           |
| N-1 | field #N-2 | scalar | Last field of the record.     |

테이블 레코도에 링크된 **정렬**에는 의미가 없으므로 레코드가 테이블에 추가되는 순서와 상관이 없습니다. 실제로 효율적인 연결 방법은 **정렬**을 유도하며, 추가된 순서에 관해서는 실지로 역순이 됩니다.
> The linked "ordering" of table records has no semantics and it doesn't have to correlate to the order of how the records were added to the table. In fact, an efficient way of the linking leads to "ordering" which is actually reversed wrt the insertion order.

## Non unique index

B+Tree에 대한 [복합키](https://en.wikipedia.org/wiki/Compound_key)는 `{indexed valuse, record handle}` 입니다. B+Tree 값은 사용하지 않습니다.
> The composite key of the B+Tree is `{indexed values, record handle}`. The B+Tree value is not used.

```
            B+Tree key                    B+Tree value
+----------------+---------------+      +--------------+
| Indexed Values | Record Handle |  ->  |   not used   |
+----------------+---------------+      +--------------+
```

## Unique index

인덱스된 값이 모두 `NULL`이라면, 복합 B+Tree 키는 `{nil, record handle}`이고 B+Tree 값은 사용하지 않습니다.
> If the indexed values are all NULL then the composite B+Tree key is `{nil, record handle}` and the B+Tree value is not used.

```
        B+Tree key                B+Tree value
+------+-----------------+      +--------------+
| NULL |  Record Handle  |  ->  |   not used   |
+------+-----------------+      +--------------+
```

인덱스된 값이 모두 `NULL`이라면, B+Tree 키에 대한 키가 인덕싱된 값이고, B+Tree 값은 레코드 handle 입니다.
> If the indexed values are not all NULL then key of the B+Tree key are the indexed values and the B+Tree value is the record handle.

```
    B+Tree key                B+Tree value
+----------------+      +---------------+
| Indexed Values |  ->  | Record Handle |
+----------------+      +---------------+
```

## Non scalar types

[`lldb/EncodeScalars`][1]에 대한 scalar 타입은 `bool`, `complex*`, `float*`, `int*`, `uint*`, `string`, `[]byte` 타입입니다. 모든 다른 타입은 `blob-like` 입니다.
> Scalar types of [`lldb/EncodeScalars`][1] are `bool`, `complex*`, `float*`, `int*`, `uint*`, `string` and `[]byte` types. All other types are "blob-like".

```
QL type         Go type
-----------------------------
blob            []byte
bigint          big.Int
bigrat          big.Rat
time            time.Time
duration        time.Duration
```

메모리 백엔드는 Go 타입으로 직접 저장합니다. 파일 백엔드는 lldb가 기본적으로 지원하는 유형이 더 적기에 (태그가 붙은) `[]byte`를 이용하여 위 모든 내용을 인코딩 해야합니다. `Blob-like`한 타입의 `NULL` 값은 `nil` (`lldb/db.go`안의 `gbNull`)으로 인코딩 됩니다. 이미 존재하는 QL 타입과 완전히 동일합니다.
> Memory back-end stores the Go type directly. File back-end must resort to encode all of the above as (tagged) `[]byte` due to the lack of more types supported natively by lldb. NULL values of blob-like types are encoded as `nil` (`gbNull` in `lldb/gb.go`), exactly the same as the already existing QL types are.

## Blob encoding

`Blob-like`한 타입 값은 먼저 `[]byte` 슬라이스로 인코딩 됩니다:
> The values of the blob-like types are first encoded into a `[]byte` slice:

```
+-----------------------+-------------------+
| blob                  | raw               |
| bigint, bigrat, time	| gob encoded       |
| duration	          	| gob encoded int64 |
+-----------------------+-------------------+
```

`gob` 인코딩은 `blob-like`한 타입에 대한 모든 초기 인코딩과 관련하여 **차별됩니다**. 다른 말로, `gob` 인코딩이 반드시 써야되는 초기 타입 디스크립터는 제거되고 정직하게 디코딩될때 **재 공급**됩니다. (참조, [`blob.go`](https://github.com/cznic/ql/blob/v1.1.0/blob.go)). 결과로 나온 슬라이스 길이가 `<= shortBolob` 인 경우, 첫번째이자 유일한 청크는 다음과 같은 스칼라 인코딩입니다:
> The gob encoding is "differential" wrt an initial encoding of all of the blob-like type. IOW, the initial type descriptors which gob encoding must write out are stripped off and "resupplied" on decoding transparently. See also blob.go. If the length of the resulting slice is `<= shortBlob`, the first and only chunk is the scalar encoding of

```
[]interface{}{typeTag, slice}.                  // initial (and last) chunk
```

슬라이스 길이가 `0`일 수도 있습니다 (`blob("")`인 경우). 결과로 나온 슬라이스 길이가 길다면 (`> shortBlob`), 첫 번째 청크는 인코딩에서 옵니다:
> The length of slice can be zero (for blob("")). If the resulting slice is long (`> shortBlob`), the first chunk comes from encoding

```
[]interface{}{typeTag, nextHandle, firstPart}.  // initial, but not final chunk
```

이 경우 `len(firstPart) <= shortBlob`입니다. 두번째와 다른 청크입니다. 만약 마지막 청크면 `src`는 다음과 같습니다.
> In this case `len(firstPart) <= shortBlob`. Second and other chunks: If the chunk is the last one, src is

```
[]interface{lastPart}.                          // overflow chunk (last)
```

이 경우 `len(lastPart) <= 64kB`입니다. 마지막 청크가 아닌 경우, `src`는 다음과 같습니다.
> In this case `len(lastPart) <= 64kB`. If the chunk is not the last one, src is

```
[]interface{}{nextHandle, part}.                // overflow chunk (not last)
```

이 경우는 `len(part) == 64kB` 입니다.
> In this case `len(part) == 64kB`.

## Links

참조 사항:
> Referenced from above:

```
[0]: http://godoc.org/github.com/cznic/lldb#hdr-Block_handles
[1]: http://godoc.org/github.com/cznic/lldb#EncodeScalars
[2]: http://godoc.org/github.com/cznic/lldb#BTree
```

## Rationale

이 노트는 QL 소스를 보든 사람에게 유용 할 수 있지만, 특별히 의도된 독자는 미래의 나 자신입니다.
> While these notes might be useful to anyone looking at QL sources, the specifically intended reader is my future self.

[0]: http://godoc.org/github.com/cznic/lldb#hdr-Block_handles
[1]: http://godoc.org/github.com/cznic/lldb#EncodeScalars
[2]: http://godoc.org/github.com/cznic/lldb#BTree
