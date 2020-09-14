# hello_flask

### 0. environment
- Ubuntu 20.04
- python3

### 0.1. pip3 update
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
mysql> create database rabbit_house;
mysql> show databases;
mysql> use rabbit_house;
mysql> show tables;
mysql> create table members (
    -> id int not null primary key auto_increment,
    -> name varchar(64) not null,
    -> email varchar(256) not null unique);
mysql> show tables;
mysql> desc members;
mysql> create user 'tippy'@'localhost' identified by 'root';
mysql> select user, host from mysql.user;
mysql> show grants for 'root'@'localhost';
mysql> show grants for 'tippy'@'localhost';
mysql> grant all on *.* to 'tippy'@'localhost' with grant option;
mysql> flush privileges;
mysql> INSERT rabbit_house.members SET name='Chino Kafu',email='chino_kafu@is-your-order.rb';
mysql> INSERT rabbit_house.members SET name='Rize Tedeza',email='rize_tedeza@is-your-order.rb';
mysql> INSERT rabbit_house.members SET name='Cocoa Hoto',email='cocoa_hoto@is-your-order.rb';
mysql> select * from rabbit_house.members;
```

### Extra. delete database
- finish, exit database
```
mysql> exit;
```
- delete database
```
mysql> drop database rabbit_house
```
- rename table
```
mysql> alter table members rename to worker;
```

### Reference
1. https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
2. https://rfs.jp/sb/sql/s03/03-15.html

test
test2
