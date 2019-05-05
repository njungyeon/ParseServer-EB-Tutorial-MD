
# PostgreSQL 환경 구성하기

## PostgreSQL


 PostgreSQL은 객체관계형 데이터베이스 관리 시스템(ORDBMS)이다. 이것은 미국 캘리포니아에 있는 버클리 대학 컴퓨터 과학부에서 개발한 POSTGRES, Version 4.2를 기반으로 개발되었다. POSTGRES는 훗날 몇몇 상용 데이터베이스에 영향을 준 많은 개념들을 개척했다.

PostgreSQL은 이 원래의 버클리 소스를 기반으로 확장된 오픈 소스이다. 이것은 표준 SQL 기능을 대부분 지원하며, 다음과 같은 진보된 많은 기능도 함께 지원한다:

    복합 쿼리
    참조키
    트리거
    업데이트 가능한 뷰
    트랜잭션
    다중 버전 병행 제어

또한, PostgreSQL에서는 다양한 방법으로 기능을 확장 할 수 있다. 예로, 다음과 같은 것들을 사용자가 직접 새로 만들 수 있다.

    자료형
    함수
    연산자
    집계 함수
    인덱스 방법
    프로시져 언어

그리고, PostgreSQL의 라이센스는 개인적이든, 상업적이든, 교육용이든 어떠한 목적으로도 누구나가, 소스를 수정하고, 재배포할 수 있다.

출처: http://postgresql.kr/docs/11/intro-whatis.html

## PostgreSQL 설치

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Window Tutorial: http://www.postgresqltutorial.com/install-postgresql/
Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

윈도우에서는 PostgreSQL 설치 시 SQL Shell 설치 후 그것을 통해 접속하는 것을 추천합니다.

### Ubuntu에 설치하기

#### 1. 설치

apt를 사용해 PostgreSQL을 설치하고 관련 유틸리티 또한 설치합니다.

```sh
sudo apt update
sudo apt install postgresql postgresql-contrib
```

#### 2. 설정

Postgres는 "roles"라는 권한 관리 방식을 사용합니다. 이것은 유닉스의 그것과 유사한 스타일이지만 더 유연합니다. Postgre 설치 후에는 Unix/Linux 시스템 계정과 매칭되는 postgres라는 계정이 생성되고 그 계정은 postgres의 관리자 계정으로 사용됩니다.

일반적으로 따로 권한을 주지 않는 이상 특정 유저로 postgres에 접속 시 해당 데이터베이스로 접속하게 됩니다.
postgres 유저의 경우 postgres 데이터베이스로, tutorial 유저의 경우 tutorial 데이터베이스로 접속하는 식입니다.

1. 설치된 버전 확인

```sh
postgres -V
```

2. PostgreSQL 프롬프트로 진입 및 유용한 명령어

postgres 유저로 변경 후 진입
```
sudo -i -u postgres
psql
```

혹은,
postgres 유저를 사용하여 바로 진입

```sh
sudo -u postgres psql
```



데이터 베이스 리스트 확인
```
postgres> \list
```

접속 정보 확인
```
postgres> \conninfo
```

유저 Role 리스트 확인
```
postgres> \du
```

테이블 리스트 보기
```
postgres> \d
or
postgres> \d TABLE_NAME
```

종료는

```
postgres> \q
```

3. 새로운 Role 생성하기

```
postgres> \du
```

현재 `postgres` 롤과 데이터베이스를 가지고 있습니다. . postgres 프롬프트에서 `createrole`을 통해 직접 유저를 생성하는 방법도 있지만  저희는 postgres의 `createuser` 커맨드를 이용하여 새로운 유저를 생성하여 사용하도록 하겠습니다.
`--pwprompt`를 추가하면 패스워드 설정도 가능하지만 여기서는 사용하지 않겠습니다.

postgres 유저를 통해 새로운 유저를 생성합니다. 비번은 적용하지 않습니다.

```
sudo -u postgres createuser --interactive
```

여기서는 superuser 권한을 주도록 하겠습니다.

```
Output
Enter name of role to add: tutorial
Shall the new role be a superuser? (y/n) y
```

이것은 psql 프롬프트에서 다음 명령어로도 대체 가능합니다.

```
postgres> CREATE USER tutorial WITH ENCRYPTED PASSWORD 'password';
```

3. tutorial 데이터베이스 생성

```sh
sudo -u postgres createdb tutorial
```

```sh
postgres> CREATE DATABASE tutorial;
```

4. DB 접속 후 테이블 만들어보기

tutorial 유저로 방금 만든 tutorial db에 접속해 보겠습니다.

```
psql -U tutorial -d tutorial -h localhost  -W
```

유저와 데이터베이스 이름이 동일할경우 생략 가능합니다.

```
psql -U tutorial
```

이제 psql 프롬프트에서 테이블을 생성하고 확인해보겠습니다.

```
tutorial> create table aa (column1 Int);
tutorial> \d
```

output
```
List of relations
 Schema | Name | Type  |  Owner
--------+------+-------+----------
 public | aa   | table | tutorial
(1 row)
```

잘 생성되는걸 확인하셨으면 테이블을 지우겠습니다.

```
tutorial> drop table aa;
tutorial> \d
```

#### 3. 유저 추가하기

현재 postgres에 'role'로 등록한 tutorial 유저는 리눅스상에서는 존재하지 않는 유저입니다.
유저를 추가한 후 해당 유저를 통해 psql 프롬프트 접근이 가능합니다.

유저 추가

```
sudo adduser tutorial
```

해당 유저로 psql 접속

```
sudo -i -u tutorial
psql
```

이것은 위의

```
psql -U tutorial
```

과 동일한 효과를 같습니다.