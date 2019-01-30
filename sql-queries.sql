/******
Basic SQL operations

Preparing environment. You may skip them if you have access to any SQL
1. Please download required version from https://www.sqlite.org/download.html
2. Next, install SQLLiteStudio from here https://sqlitestudio.pl/index.rvt?act=download

You can refer http://www.sqlitetutorial.net/download-install-sqlite/ to get more help!

Congratulations! You have an environment to play
*********/

/* Create Books table */
CREATE TABLE books(
    id integer PRIMARY KEY,
    name text,
    rating integer
    );

/* Insert sample data */
insert into books values(1, 'Harry Potter', 5);
insert into books values(2, 'Chronicles of Narnia', 4);
insert into books values(3, 'The Martian', null);

/* Select all books */
select * from books;

/**************
1	Harry Potter	5
2	Chronicles of Narnia	4
3	The Martian	NULL
*********/
/* Create bikes table */
create table bikes(
    id integer primary key,
    name text,
    quantity integer,
    price numeric,
    category text
);

/* insert sample data */
insert into bikes values (1, 'Nimbus 2000', 10, 500.00, 'Mountain');
insert into bikes values (2, 'Firebolt', 5, 599.99, 'Racing');
insert into bikes values (3, 'RoadRacer', 1, 445.50, 'Racing');
insert into bikes values (4, 'MountainClimber', 6, 330.00, 'Mountain');
insert into bikes values (5, 'Beach Cruiser', 12, 220, 'Cruiser');

/* Ensure data is inserted */
select * from bikes;

/**********
1	Nimbus 2000	10	500	Mountain
2	Firebolt	5	599.99	Racing
3	RoadRacer	1	445.5	Racing
4	MountainClimber	6	330	Mountain
5	Beach Cruiser	12	220	Cruiser
************/

/* Select each category based on quantities */
select category, sum(quantity) as total_quantity from bikes group by category order by total_quantity desc;

/*********
Mountain	16
Cruiser	12
Racing	6
*********/

select * from bikes where category = 'Mountain' order by price desc;
/*********
1	Nimbus 2000	10	500	Mountain
4	MountainClimber	6	330	Mountain
********/

/* Find total number of bikes*/
select sum(quantity) from bikes;
/*********
34
*********/

/* Create tables */
create table exercise_logs (
	id integer primary key autoincrement, 
	type, text, minutes integer, 
	calories integer, 
	heart_rate integer
);
create table drs_favorites (
	id integer primary key, 
	type text, 
	reason text
);

/* Insert data */
insert into exercise_logs(type, minutes, calories, heart_rate) values ('biking', 30, 100, 110);
insert into drs_favorites(type, reason) values ('biking', 'improves endurance and flexibility.');

/* subquery - selects all activities that the user did that are recommended by doctor for cardio health */
select * from exercise_logs where type in (select type from drs_favorites where reason like "%cardiovascular%");

/*****
No output - zero rows found
*****/

/* table of all types of activity and the total amount of calories burned by doing that activity */
select type, sum(calories) as total_calories from exercise_logs group by type; 

/*****
biking	100
****/

/* Insert more sample data */
insert into exercise_logs(type, minutes, calories, heart_rate) values ('biking', 30, 100, 110);
insert into exercise_logs(type, minutes, calories, heart_rate) values ('running', 30, 70, 110);
insert into exercise_logs(type, minutes, calories, heart_rate) values ('hiking', 30, 200, 110);
insert into exercise_logs(type, minutes, calories, heart_rate) values ('biking', 10, 30, 110);

select type, sum(calories) as total_calories
    from exercise_logs
    group by type
    having total_calories > 150;
    
/**********
biking	230
hiking	200
******/

/* 50-90% of max heart rate for activity */
select count(*) from exercise_logs 
where heart_rate >= round(.5 * (220 -30))
and heart_rate <= round(.9 * (220 - 30));
/*******
5
*******/
                              
/* Insert more sample data */
insert into exercise_logs(type, minutes, calories, heart_rate) values ('biking', 30, 100, 150);
insert into exercise_logs(type, minutes, calories, heart_rate) values ('running', 30, 70, 190);

/* add column for activity's target heart rate status */
select type, heart_rate,
    case 
        when heart_rate > 220 - 30 then 'above max'
        when heart_rate > round(.9 * (220 - 30)) then 'above target'
        when heart_rate > round(.5 * (220 - 30)) then 'within target'
        else 'below target'
    end as 'heart_rate_zone'
from exercise_logs;
    
/******
biking	110	within target
biking	110	within target
running	110	within target
hiking	110	within target
biking	110	within target
biking	150	within target
running	190	above target
********/
                                      
/* Group the count of exercises by each heart rate zone */
select count(*),
    case 
        when heart_rate > 220 - 30 then 'above max'
        when heart_rate > round(.9 * (220 - 30)) then 'above target'
        when heart_rate > round(.5 * (220 - 30)) then 'within target'
        else 'below target'
    end as 'heart_rate_zone'
from exercise_logs
group by heart_rate_zone;
                                      
/*******
1	above target
6	within target
*******/

                                      
/* Gradebook */

CREATE TABLE student_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    number_grade INTEGER,
    fraction_completed REAL);
    
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Winston", 90, 0.805);
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Winnefer", 95, 0.901);
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Winsteen", 85, 0.906);
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Wincifer", 66, 0.7054);
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Winster", 76, 0.5013);
INSERT INTO student_grades (name, number_grade, fraction_completed)
    VALUES ("Winstonia", 82, 0.9045);

select name, number_grade, round(100.00 * fraction_completed) as percent_completed from student_grades;

/***********
Winston	90	81
Winnefer	95	90
Winsteen	85	91
Wincifer	66	71
Winster	76	50
Winstonia	82	90
********/

/*How many students have got which grade*/
select count(number_grade),
    case
        when number_grade > 90 then 'A'
        when number_grade > 80 then 'B'
        when number_grade > 70 then 'C'
        else 'F'
    end as 'letter_grade'
    from student_grades    
    group by letter_grade;

/********
1	A
3	B
1	C
1	F
********/

                                      
/* Marvel Heroes and Villains */

CREATE TABLE marvels (ID INTEGER PRIMARY KEY,
    name TEXT,
    popularity INTEGER,
    alignment TEXT,
    gender TEXT, 
    height_m NUMERIC,
    weight_kg NUMERIC,
    hometown TEXT,
    intelligence INTEGER,
    strength INTEGER,
    speed INTEGER,
    durability INTEGER,
    energy_Projection INTEGER,
    fighting_Skills INTEGER);
    
INSERT INTO marvels VALUES(1, "Spider Man", 1, "Good", "Male", 1.78, 75.75, "USA", 4, 4, 3, 3, 1, 4); 
INSERT INTO marvels VALUES(2, "Iron Man", 20, "Neutral", "Male", 1.98, 102.58, "USA", 6, 6, 5, 6, 6, 4); 
INSERT INTO marvels VALUES(3, "Hulk", 18, "Neutral", "Male", 2.44, 635.29, "USA", 6, 7, 3, 7, 5, 4); 
INSERT INTO marvels VALUES(4, "Wolverine", 3, "Good", "Male", 1.6, 88.46, "Canada", 2, 4, 2, 4, 1, 7);
INSERT INTO marvels VALUES(5, "Thor", 5, "Good", "Male", 1.98, 290.3, "Norway", 2, 7, 7, 6, 6, 4);
INSERT INTO marvels VALUES(6, "Green Goblin", 91, "Bad", "Male", 1.93, 174.63, "USA", 4, 4, 3, 4, 3, 3);
INSERT INTO marvels VALUES(7, "Magneto", 11, "Neutral", "Male", 1.88, 86.18, "Germany", 6, 3, 5, 4, 6, 4);
INSERT INTO marvels VALUES(8, "Thanos", 47, "Bad", "Male", 2.01, 446.79, "Titan", 6, 7, 7, 6, 6, 4);
INSERT INTO marvels VALUES(9, "Loki", 32, "Bad", "Male", 1.93, 238.14, "Jotunheim", 5, 5, 7, 6, 6, 3);
INSERT INTO marvels VALUES(10, "Doctor Doom", 19, "Bad", "Male", 2.01, 188.24, "Latveria", 6, 4, 5, 6, 6, 4);
INSERT INTO marvels VALUES(11, "Jean Greay", 8, "Good", "Female", 1.68, 52.16, "USA", 3, 2, 7, 7, 7, 4);
INSERT INTO marvels VALUES(12, "Rogue", 4, "Good", "Female", 1.73, 54.43, "USA", 7, 7, 7, 7, 7, 7);

select * from marvels;
                                      
/**************
1	Spider Man	1	Good	Male	1.78	75.75	USA	4	4	3	3	1	4
2	Iron Man	20	Neutral	Male	1.98	102.58	USA	6	6	5	6	6	4
3	Hulk	18	Neutral	Male	2.44	635.29	USA	6	7	3	7	5	4
4	Wolverine	3	Good	Male	1.6	88.46	Canada	2	4	2	4	1	7
5	Thor	5	Good	Male	1.98	290.3	Norway	2	7	7	6	6	4
6	Green Goblin	91	Bad	Male	1.93	174.63	USA	4	4	3	4	3	3
7	Magneto	11	Neutral	Male	1.88	86.18	Germany	6	3	5	4	6	4
8	Thanos	47	Bad	Male	2.01	446.79	Titan	6	7	7	6	6	4
9	Loki	32	Bad	Male	1.93	238.14	Jotunheim	5	5	7	6	6	3
10	Doctor Doom	19	Bad	Male	2.01	188.24	Latveria	6	4	5	6	6	4
11	Jean Greay	8	Good	Female	1.68	52.16	USA	3	2	7	7	7	4
12	Rogue	4	Good	Female	1.73	54.43	USA	7	7	7	7	7	7
***************/
                                      
                                      
/*Most and least popular*/
select name, min(popularity) least_popular from marvels;
/***********
Spider Man	1
***********/

select name, max(popularity) most_popular from marvels;
/***********
Green Goblin	91
*************/
