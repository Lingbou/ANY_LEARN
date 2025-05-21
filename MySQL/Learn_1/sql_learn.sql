#Show all the database in the databaseAPP.
SHOW DATABASES;


# create a database and detele it. 
CREATE DATABASE `test`;
DROP DATABASE `test`;


# use this database.
USE sql_learn;


# create a table named `*****`.
CREATE TABLE `student`(
    `student_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20)
);

DROP TABLE `student`;

CREATE TABLE `student`(
    `student_id` INT AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20) UNIQUE,
    `tset_default` VARCHAR(20) DEFAULT 'caonima',
    PRIMARY KEY(`student_id`)
);


#create a table and delete it.
CREATE TABLE `test_table`(
    `nimalegebi` INT
);
DROP TABLE `test_table`;


# show the table's struct;
DESCRIBE `student`;

ALTER TABLE `student` ADD `gpa` DECIMAL(3,2);
ALTER TABLE `student` DROP `gpa`;

SELECT * FROM `student`;

INSERT INTO `student` VALUES(1, '小红', '物理', '1');
INSERT INTO `student` VALUES(2, '小绿', NULL);
INSERT INTO `student` VALUES(3, '小蓝', '英语');
INSERT INTO `student` VALUES(4, '小黑', '英语');


INSERT INTO `student`(`student_id`, `name`, `major`) VALUES(1, '111', '3');


DROP TABLE `student`;


CREATE TABLE `student`(
    `student_id` INT AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20),
    `score` INT,
    PRIMARY KEY(`student_id`)
);

DESCRIBE TABLE `student`;

SELECT * FROM `student`;

INSERT INTO `student`(`name`, `major`, `score`) VALUES('小白', '英语', 50);
INSERT INTO `student`(`name`, `major`, `score`) VALUES('小黄', '生物', 90);
INSERT INTO `student`(`name`, `major`, `score`) VALUES('小绿', '历史', 70);
INSERT INTO `student`(`name`, `major`, `score`) VALUES('小蓝', '英语', 80);
INSERT INTO `student`(`name`, `major`, `score`) VALUES('小黑', '化学', 20);


DELETE FROM `student`;


UPDATE `student`
SET `major` = '英语文学系'
WHERE `major` = '英语';

SELECT * FROM `student`;

UPDATE `student`
SET `major` = '生化'
WHERE `major` = '化学' OR `major` = '生物';

UPDATE `student`
SET `major` = '物理';

DELETE FROM `student`
WHERE `student_id` = 4;


SELECT *
FROM `student`
ORDER BY score DESC;