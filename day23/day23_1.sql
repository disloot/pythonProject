create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0 
);

-- classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);

SHOW create table students
-- 向students表中插入数据
INSERT INTO students(name,age,height,gender,cls_id,is_delete)
VALUES
	( '小明', 18, 180.00, 2, 1, 0 ),
	( '小月月', 18, 180.00, 2, 2, 1 ),
	( '彭于晏', 29, 185.00, 1, 1, 0 ),
	( '刘德华', 59, 175.00, 1, 2, 1 ),
	( '黄蓉', 38, 160.00, 2, 1, 0 ),
	( '凤姐', 28, 150.00, 4, 2, 1 ),
	( '王祖贤', 18, 172.00, 2, 1, 1 ),
	( '周杰伦', 36, NULL, 1, 1, 0 ),
	( '程坤', 27, 181.00, 1, 2, 0 ),
	( '刘亦菲', 25, 166.00, 2, 2, 0 ),
	( '金星', 33, 162.00, 3, 3, 1 ),
	( '静香', 12, 180.00, 2, 4, 0 ),
	( '郭靖', 12, 170.00, 1, 4, 0 ),
	( '周杰', 34, 176.00, 2, 5, 0 );

-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期");


-- 可以通过 as 给表起别名 
select s.id,s.name,s.gender from students as s;

select DISTINCT gender from students;

-- 例1：查询编号大于3的学生
select * from students where id > 3;
-- 例2：查询编号不大于4的学生
select * from students where id <= 4;
-- 例3：查询姓名不是“黄蓉”的学生
select * from students where name != '黄蓉';
-- 例4：查询没被删除的学生,is_delete为零代表没有删除，为1代表删除
select * from students where is_delete=0;

-- 例5：查询编号大于3的女同学
select * from students where id > 3 and gender=2;
-- 例6：查询编号小于4或没被删除的学生
select * from students where id < 4 or is_delete=0;

-- 例7：查询姓小的学生
select * from students where name like '小%';
-- 例8：查询姓小并且“名”是一个字的学生
select * from students where name like '小_';
-- 例9：查询姓黄或叫靖的学生
select * from students where name like '黄%' or name like '%靖';


-- 例10：查询编号是1或3或8的学生
select * from students where id in(1,3,8);
-- •between ... and ...表示在一个连续的范围内，闭区间
-- 例11：查询编号为3至8的学生
select * from students where id between 3 and 8;
-- 例1  2：查询编号是3至8的男生
select * from students where gender=1 and id between 3 and 8;

-- --------------------------------------------------------
-- 排序
-- 例1：查询未删除男生信息，按学号降序
select * from students where gender=1 and is_delete=0 order by name;
-- 显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时 按照身高从高-->矮排序
select * from students  order by age desc,height desc;

-- 聚合

-- 例1：查询学生总数
select count(*) from students;
-- 最大值
-- •max(列)表示求此列的最大值
-- 例2：查询女生的年龄最大值
select max(age) from students where gender=2;


-- 例3：查询未删除的学生最小编号
select min(id) from students where is_delete=0;

-- 查询男生的总年龄
select sum(age) from students where gender=1;

-- 查询未删除女生的编号平均值
select avg(age) from students where is_delete=0 and gender=2;


-- 分组,聚合
select gender from students group by gender;

-- null不参与分组里的聚合
select avg(height),gender,max(age) from students group by gender;

-- group_concat对字符串进行聚合
select gender,group_concat(name) from students group by gender;

-- having用于分组后的聚合结果的过滤，这时用where会报错
select gender,count(*) from students group by gender HAVING count(*)>2;


select gender,count(*) from students where gender<=2 group by gender with rollup ;


select *,rank() over (partition by cls_id order by age desc) as rank1,
								 dense_rank() over (partition by cls_id order by age desc) as dese_rank,
									row_number() over (partition by cls_id order by age desc) as row_num  from students;
									
									
select *,rank() over (order by age desc) as rank1,
								 dense_rank() over (order by age desc) as dese_rank,
									row_number() over (order by age desc) as row_num  from students;
									
									
select * from students where gender=1 order by age desc limit 1,3;

select gender,count(*) from students group BY gender with rollup HAVING count(*)>3  ;

