Title: mysql 복제 오류
Date: 2016-01-28 01:10
Category: Operation
Tags: aws, rds, mysql, mariadb, replication
Slug: mysql-복제-오류
Summary: 오랜만에 RDS를 확인하러 들어갔더니... error 이벤트가... 딱!

오랜만에 설정할 일이 있어서 RDS로 접속했더니... RDS 인스턴스에서 error 이벤트가
발생하고 있었다. 복제 기능을 사용하면서 신경안 쓸려고 하고 있었는데... 여기서
문제가...

RDS를 제외하고 관련 내용을 찾았더니, `my.cnf` 파일에다가 뭘 넣고 수정하라고
한다. 이렇게 할려면 RDS는 안된다. 명령어를 입력하라는 말도 있었다. 그런데...
이넘의 RDS에서 사용자는 말그대로 사용자일 뿐이다. 어떠한 database에 대한 수정을
가할 수 있는 권한 자체가 없다. 그 사용자 이름을 `root`로 했다고 해도 말이다.

결국.. 찾다 돌아온 곳은.
[Amazon Relational Database Service - mysql_rds_skip_repl_error](http://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/mysql_rds_skip_repl_error.html)
부분. 그냥 접근해서 `CALL mysql.rds_skip_repl_error` 입력하면 된단다.

그런데 이건 mysql에서만 발생하는 오류인것같다. mariadb에서는 해당 오류가 없다.
mariadb를 사용하는게 정신 건강에 좋은...
