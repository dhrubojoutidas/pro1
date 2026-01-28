/* LoadData.sql file contains the data for the tables in a csv formet.

here we have  7 types of csv file that contains the details of the tables like

1.loading data for_COACH Table
2.loading data for_ATHLETE Table
3.loading data for_TEAM Table
4.loading data for_TOTAL_MEDALS Table
5.loading data for_TABLE EVENT
6 Loading data for_MEDALISTIST TABLE
7 Loading data for_TABLE SCHEDULE 

*/


-- 1.loading data for_COACH Table

LOAD DATA LOCAL
    
   INFILE 'coach.csv'
   INTO TABLE COACH
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;


-- 2.loading data for_ATHLETE Table

LOAD DATA LOCAL
    
   INFILE 'athelete.csv'
   INTO TABLE  ATHLETE 
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;
   


-- 3.loading data for_TEAM Table

LOAD DATA LOCAL
    
   INFILE 'team.csv'
   INTO TABLE TEAM 
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;    



-- 4.loading data for_TOTAL_MEDALS Table

LOAD DATA LOCAL
    
   INFILE 'medals_total.csv'
   INTO TABLE TOTAL_MEDAL
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;



-- 5.loading data for_TABLE EVENT

LOAD DATA LOCAL
    
   INFILE 'events.csv'
   INTO TABLE EVENT 
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;
   
   
   
-- 6 Loading data for_MEDALISTIST TABLE

LOAD DATA LOCAL
    
   INFILE 'medallists.csv'
   INTO TABLE MEDALLIST
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;
   
   
-- 7 Loading data for_TABLE SCHEDULE 
     
LOAD DATA LOCAL
    
   INFILE 'schedule.csv'
   INTO TABLE SCHEDULE
   FIELDS TERMINATED BY ',' ENCLOSED BY '"'
   LINES TERMINATED BY '\n' 
   IGNORE 1 ROWS;
 
  

  
  
  
