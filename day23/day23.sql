show databases;

create database python5 charset='utf8';

show create database python5;

drop database python5;

show tables;

-- 每一句sql记得加分号
create table classes(
	id int UNSIGNED auto_increment PRIMARY KEY NOT NULL,
	`name` varchar(20));

-- 枚举类型第一个位置值是1
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','人妖','保密'),
    cls_id int unsigned default 0
);

-- 给表添加一个字段
ALTER TABLE students ADD birthday DATE;
ALTER TABLE students ADD test int;
-- 改变表中某个列的列名
ALTER TABLE students change birthday birth DATE;
-- 改变字段的类型
ALTER TABLE students MODIFY birth DATE not null;
-- 删除一列
ALTER TABLE students drop test;
-- 删除表
drop table students;
-- 查看创建表语句
show create table students;
-- 插入，0 就是自动增长的含义
insert into students values(0,'郭靖',20,181,1,1,'2016-1-2');
insert into students(`name`,birthday) values('黄蓉','2016-3-2');
insert into students(height,birthday) values(160,'2013-3-2');

select * from students;

insert into classes values(0,'python1'),(0,'python2');
-- 修改
update students set name='熊大' where id=3;
update students set height=161,gender=2 where name='黄蓉';

-- 删除
delete from students where gender is NULL;