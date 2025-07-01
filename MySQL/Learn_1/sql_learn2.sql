CREATE TABLE `employee`(
    `emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);
 
CREATE TABLE `branch`(
    `branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`)ON DELETE SET NULL
);


ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`)
REFERENCES `branch`(`branch_id`)
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY(`sup_id`)
REFERENCES `employee`(`emp_id`)
ON DELETE SET NULL;

CREATE TABLE `client`(
    `client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);

CREATE TABLE `workS_with`(
    `emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY(`emp_id`, `client_id`),
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
);

INSERT INTO `branch` VALUES(1, 'YANFA', NULL);
INSERT INTO `branch` VALUES(2, 'XINGZHENG', NULL);
INSERT INTO `branch` VALUES(3, 'ZIXUN', NULL);

INSERT INTO `employee` VALUES(206, 'XIAOHUANG', '1998-10-08', 'F', 50000, 1, NULL);
INSERT INTO `employee` VALUES(207, 'XIAOLV', '1985-09-16', 'M', 29000, 2, NULL);
INSERT INTO `employee` VALUES(208, 'XIAOHEI', '2000-12-19', 'M', 35000, 3, NULL);
INSERT INTO `employee` VALUES(209, 'XIAOBAI', '1997-01-22', 'F', 39000, 3, NULL);
INSERT INTO `employee` VALUES(210, 'XIAOLAN', '1925-11-10', 'F', 84000, 1, NULL);

UPDATE `employee`
SET `sup_id` = 207
WHERE `name` = 'XIAOBAI' OR `name` = 'XIAOLAN';

UPDATE `branch`
SET `manager_id` = 208
WHERE `branch_id` = 3;

SELECT * FROM `branch`;

INSERT INTO `client` VALUES(400, 'AGOU', '123');
INSERT INTO `client` VALUES(401, 'AMAO', '123');
INSERT INTO `client` VALUES(402, 'WANGLAI', '123');
INSERT INTO `client` VALUES(403, 'LUCY', '123');
INSERT INTO `client` VALUES(404, 'ERIC', '123');

SELECT * FROM `client`;

INSERT INTO `workS_with` VALUES(206, 400, 70000);
INSERT INTO `workS_with` VALUES(207, 401, 24000);
INSERT INTO `workS_with` VALUES(208, 400, 9800);
INSERT INTO `workS_with` VALUES(208, 403, 24000);
INSERT INTO `workS_with` VALUES(210, 404, 87940);

SELECT * FROM `workS_with`;

SELECT * FROM `employee`;

SELECT * FROM `client`;

SELECT *
FROM `employee`
ORDER BY `salary` DESC
LIMIT 3;

SELECT `name`
FROM `employee`;

SELECT DISTINCT `sex`
FROM `employee`;


SELECT COUNT(`sup_id`) FROM `employee`;

SELECT COUNT(`birth_date`)
FROM `employee`
WHERE `birth_date` >'1970-01-01' AND `sex` = 'F'; 

SELECT AVG(`employee`.`salary`) FROM `employee`;
SELECT SUM(`salary`) FROM `employee`;
SELECT MAX(`salary`) FROM `employee`;
SELECT MIN(`salary`) FROM `employee`;


SELECT * FROM `client` WHERE `phone` LIKE '%23';
SELECT * FROM `client` WHERE `client_name` LIKE 'A%';

SELECT *
FROM `employee`
WHERE `birth_date` LIKE '_____12___';

SELECT `name`
FROM `employee`
UNION
SELECT `client_name`
FROM `client`;

INSERT `branch` VALUES(4, 'TOULAN', NULL);

SELECT * 
FROM `employee`
LEFT JOIN `branch`
ON `emp_id` = `manager_id`;

SELECT `name`
FROM `employee`
WHERE `emp_id` = (
    SELECT `branch`.manager_id
    FROM `branch`
    WHERE `branch_name` = 'YANFA'
);

SELECT `name`
FROM `employee`
WHERE `emp_id` IN (
    SELECT `emp_id`
    FROM `workS_with`
    WHERE `total_sales` > 50000
);
