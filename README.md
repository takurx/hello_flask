# hello_flask

### 0. environment
- Ubuntu 20.04
- python3, pip3 update
```
pip3 install -U pip
```

### 1. prepare
```
pip3 install flask
```

### 2. add RDBMS, Relational DataBase Management System
```
pip3 install PyMySQL
```

```
sudo apt update
sudo apt install mysql-server
```

```
$ mysql --version
mysql  Ver 8.0.21-0ubuntu0.20.04.4 for Linux on x86_64 ((Ubuntu))
```

```
sudo mysql -u root -p
```
- default password: ""(one), user access denied, you have to make user

```
mysql> members;
mysql> show databases;
mysql> use members;
mysql> show tables;
mysql> create table members (
    -> id int not null primary key auto_increment,
    -> name varchar(64) not null,
    -> email varchar(256) not null unique);
mysql> show tables;
mysql> desc members;
mysql> alter table members
    -> rename to member;
mysql> create user dbtest@'localhost' identified by 'root';
mysql> select user, host from mysql.user;
mysql> show grants for 'root'@'localhost';
mysql> show grants for 'dbtest'@'localhost';
mysql> grant all on *.* to 'dbtest'@'localhost' with grant option;
mysql> flush privileges;
mysql> INSERT testdb.members SET name='エラ・フィッツジェラルド',email='ella@exsample.jp';
mysql> INSERT testdb.members SET name='トミー・ゲレロ',email='tommy@exsample.jp';
mysql> INSERT testdb.members SET name='マディ・ウォーターズ',email='muddy@exsample.jp';
mysql> select * from testdb.members;
```

### Reference
1. https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
2. https://rfs.jp/sb/sql/s03/03-15.html

test
test2
