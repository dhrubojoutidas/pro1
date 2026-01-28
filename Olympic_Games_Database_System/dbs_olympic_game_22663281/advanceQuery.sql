/* advanceQuery.sql -- this is the file of advance query like PROCEDURE, VIEWS using for olympic games 2024.*/
-- cappture tresult for this file
tee advanceQueryAnswerOlympic.out   


/*
DROP PROCEDURE IF EXISTS CAL_TOTAL_MEDALS;    -- delete  specific  procedure
DROP PROCEDURE IF EXISTS Counting_Medal_By_discipline;  -- delete specific procedure
DROP PROCEDURE IF EXISTS Count_Discipline;                           -- delete specific procedure

DROP VIEW MEDALLIST_TEAM;               -- delete view MEDALLIST_TEAM   */





-- 1.PROCEDURE

/* 
 PRODECURE_task1:  using store procedure  to calculate the total medals on a given game and gender .
also using out parameter to hold the totalmedals. moreover, add code for erorr handilng
*/

DROP PROCEDURE IF EXISTS CAL_TOTAL_MEDALS;
DELIMITER //

CREATE PROCEDURE CAL_TOTAL_MEDALS(
    IN PRO_discipline VARCHAR(200),
    IN PRO_gender CHAR(1),
    OUT TotalMedals INT   -- this will return the total medal number

)
COMMENT 'calucaltion of total medla fro a dicipline and gender'
BEGIN
    -- declaring variable (Existsdiscipline,TotalCount  )
    DECLARE Existsdiscipline INT DEFAULT 0;  -- checks if discipline exits or not
    DECLARE TotalCount INT DEFAULT 0;   -- this var hold the total count

    
    SET TotalMedals = 0;

    -- checkings the discilines exixtence
    SELECT COUNT(*) INTO Existsdiscipline
    FROM MEDALLIST
    WHERE discipline = PRO_discipline;

 
    -- discipline does not exit, so display msg
    IF Existsdiscipline = 0 THEN
          -- SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Discipline does not exist.';
         SELECT CONCAT('SOrry!!! Discipline you have  entered :', PRO_discipline, ' does not exist.') AS Total_Medal_CALCUALTION ;
    ELSE
      
   
       -- calculates total medal number
        SELECT COUNT(*) INTO TotalCount
        FROM MEDALLIST
        WHERE discipline = PRO_discipline AND gender = PRO_gender;

       
    -- now, the result(TotalCount) are assigning to out parameter which is  TotalMedals
        SET TotalMedals = TotalCount;
        
        
    END IF;
END //

DELIMITER ;




-- calling procedure 
CALL CAL_TOTAL_MEDALS('Football', 'M', @total);

-- display the result
SELECT @total AS TOTAL_MEDALS;


-- calling procedure for    discipline  does not exists
CALL CAL_TOTAL_MEDALS('Ludo', 'M', @total);

-- display the result
SELECT @total AS TOTAL_MEDALS;



-- calling procedure
CALL CAL_TOTAL_MEDALS('Water Polo', 'M', @total);

-- display the result
SELECT @total AS Total_Medals;








/*

PROCEDURE_task2: using procedure user variable  that counting total  medals  that have been won in a disicline  */


DROP PROCEDURE IF EXISTS Counting_Medal_By_discipline;
DELIMITER //

CREATE PROCEDURE Counting_Medal_By_discipline(
    IN discipline_name VARCHAR(200),   -- input for discplne name
    OUT medal_count INT        -- out parameetr for coutnig medals
)

COMMENT ' COUNTING total medal won on a specific discipline .'
BEGIN
    SELECT COUNT(*) INTO medal_count
    FROM MEDALLIST
    WHERE discipline = discipline_name;
END //

DELIMITER ;



-- call procedure
CALL Counting_Medal_By_discipline('Handball', @totalMedals);

-- display result
SELECT @totalMedals AS Total_Medals;


-- call procedure
CALL Counting_Medal_By_discipline('Table Tennis', @totalMedals);

-- display result
SELECT @totalMedals AS Total_Medals;



/*
PROCEDURE_TASK3: store procedure using Cursor and LOOP to count medals ( gold medals, silzer emdals, bronze medals) on a disipline

*/

DROP PROCEDURE IF EXISTS Count_Discipline;
DELIMITER //

CREATE PROCEDURE Count_Discipline(
    IN discipline_name VARCHAR(200),   
    OUT count_gold INT,                    -- out parameter for  gold medal  counting
    OUT count_silver INT,                -- out parameter for silver medal  counting
    OUT count_bronze INT               
)
BEGIN
     -- declarign var (var_medal_type, done)
    DECLARE var_medal_type VARCHAR(20);
    DECLARE done INT DEFAULT 0;  -- To control loop exit
    
    -- declarign the cursor
    DECLARE cursor_medal CURSOR FOR
    SELECT medal_type
    FROM MEDALLIST
    WHERE discipline = discipline_name;



    -- declar not found handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

 
-- initializing counts
    SET count_gold = 0;
    SET count_silver = 0;
    SET count_bronze = 0;

 
    -- open cursor(cursor_medal) 
    OPEN cursor_medal;



    -- start loop
    StartLoop: LOOP

        -- fetch the  cursor(cursor_medal) into variable( var_medal_type)
       
        FETCH cursor_medal INTO var_medal_type;

       
        -- checks cursor is done
        IF done = 1 THEN
            LEAVE StartLoop;  
        END IF;

      

        -- checks the medal type by using if else
        IF var_medal_type = 'Gold Medal' THEN
            SET count_gold = count_gold + 1;
        ELSEIF var_medal_type = 'Silver Medal' THEN
            SET count_silver = count_silver + 1;
        ELSEIF var_medal_type = 'Bronze Medal' THEN
            SET count_bronze = count_bronze + 1;
        END IF;
    END LOOP;

    -- closing cursor
    CLOSE cursor_medal;
END //

DELIMITER ;




-- calling procedure
CALL Count_Discipline ('Water Polo', @count_gold, @count_silver, @count_bronze);



-- display result
SELECT @count_gold AS Gold_Medals, @count_silver AS Silver_Medals, @count_bronze AS Bronze_Medals;







-- 2.EXAMPLE OF VIEW


/*
 VIEW_TASK1 :

Create VIEW  name  "MEDALLIST_TEAM " by joining MEDALLIST and TEAM table  
where MEDALLIST medal_date medal_type, medalist_id, code_athlete , birth_date, name and 
FROM team discipline and events attribute will be included.

*/
    
    
CREATE VIEW MEDALLIST_TEAM AS
SELECT  
    m.medal_date AS DATE_OF_MEDAL,       
    m.medal_type AS TYPE_OF_MEDAL,
    m.medalist_id AS MEDALLIST_ID,
    m.code_athlete ATHELTE_CODE_M,
    m.birth_date  AS BIRTHDATE,
    m.name AS NAME,
    e.code   AS TEAM_CODE,
    e.discipline AS GAMES,
    e.events AS EVENT_LIST
    
FROM 
   MEDALLIST  m
JOIN 
    TEAM e
ON
   m.code_team = e.code;  
   

SELECT * FROM MEDALLIST_TEAM;

-- DROP VIEW MEDALLIST_TEAM; 

/*

VIEW_task2 :
update name in  MEDALLIST TABLE  and checked on VIEW  MEDALLIST_TEAM  if the update was succesfull or not  by calling procedure 

let's say medallist_id 1159 changed the name and checked
*/


SELECT  NAME FROM MEDALLIST_TEAM where   MEDALLIST_ID = '1159';  -- checking VIEW the name before updating
SELECT  name FROM MEDALLIST  where medalist_id = '1159';  -- checking mEDALLIST table before updating


-- updating  MEDALLIST TABLE 
UPDATE MEDALLIST
SET name = 'dhrubo das'
WHERE medalist_id = '1159' ;



SELECT  NAME FROM MEDALLIST_TEAM where   MEDALLIST_ID = '1159';  -- updated in VIEW
SELECT  name FROM MEDALLIST  where medalist_id = '1159';  -- Updated MEDALLISt TABLE





/*

SHOW PROCEDURE STATUS WHERE Db='Olympic_Game_2024_22663281';  -- display all procedure in a specific database
-- SHOW CREATE PROCEDURE Count_Discipline;                     -- display specific procedure



SHOW FULL TABLES IN Olympic_Game_2024_22663281 WHERE TABLE_TYPE = 'VIEW';     -- display all views in  a specific database
 
SELECT * FROM MEDALLIST_TEAM;             -- select all from MEDALLIST_TEAm VIEW

SHOW CREATE VIEW MEDALLIST_TEAM ;             -- display specific VIEW 


*/

