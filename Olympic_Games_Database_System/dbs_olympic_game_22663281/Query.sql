/* Quer.sql -- file stores the qureies like simple, join , subquery, agrrregation fucntion */
-- Capturing all the output in a file
tee  SimpleQueryAnswerOlympic.out


-- show available databses---
show databases;

-- use dswork databases


-- display the structure of all tables using DESC
DESC ATHLETE ;
DESC COACH;
DESC TEAM;
DESC MEDALLIST;
DESC EVENT;
DESC SCHEDULE;
DESC TOTAL_MEDAL; 


-- Display all retrieve data using SELECT * from EACH table
SELECT * FROM ATHLETE;
SELECT * FROM TEAM;
SELECT * FROM COACH;
SELECT * FROM MEDALLIST; 
SELECT * FROM EVENT;
SELECT * FROM SCHEDULE;
SELECT * FROM TOTAL_MEDAL; 



    
-- LIST OF ALL QUERIES HERE 


/* query1 : using  SCHEDULE TABLE Rretrive all unique  discipline data   which was occured  venue  name called Champ-de-Mars Arena 
*/ 

SELECT 
    DISTINCT discipline  
FROM 
   SCHEDULE
WHERE 
    venue = 'Champ-de-Mars Arena';



/* query2:  Get the total number of Athelets using aggregation  function and rename the tbale as TOTAL_ATHELETES FROM TEAM */  
   
SELECT  SUM(num_athletes) AS TOTAL_ATHLETES  FROM TEAM;
 
 

 
/* query3 :find out the  code of team  from TEAM table discipline which name is  Archery  and renamed the tanble as  TEAM_code */

SELECT code AS TEAM_code  FROM TEAM where discipline like '%Archery%' ;  
 
 
 
/* query4 :using aggregation function find out the maximum events list from TEAM Table  */


Select MAX(events) AS EVENT_MAX from TEAM;



/* query_5: counting participants accross countries using ATHELETE TABLE.

group them country_long , Order them Alphabetically of  total_participant
*/


SELECT 
    country_long AS Name_of_Country,                   
    COUNT(athlete_code) AS Total_Participants     
FROM 
    ATHLETE
GROUP BY 
    country_long                                 
ORDER BY 
   Total_Participants ASC ;



/*
Query_6: List of total  coach number issued  by each country.

Group the results by country_long and order them alphabetically by the country_long.

*/

SELECT 
    country_long, 
    COUNT(coach_name) AS Total_Coaches_NUM_BY_Country
FROM 
    COACH
GROUP BY 
    country_long
ORDER BY             
    country_long;



/* Query_7 : List  of Coaches vs Player Ratio */


SELECT 
    c.country_code, 
    COUNT(DISTINCT a.athlete_code) AS Total_athletes,         
    COUNT(DISTINCT c.coach_code) AS Total_Coaches,       
    ROUND(COUNT(DISTINCT a.athlete_code) / COUNT(DISTINCT c.coach_code), 2) AS player_vs_coach_Ratio
FROM 
    COACH c
JOIN 
    ATHLETE a ON c.country_code = a.country_code           -- joinning based on country_code
GROUP BY 
    c.country_code 
ORDER BY 
    Total_athletes DESC;                               -- ordering them by total_ num of altheltes by large to small
    
    
    
/* query8:  List All Coaches Who Have Coached Athletes in More Than 30 Discipline*/
    
SELECT 
    c.coach_name, 
    COUNT(DISTINCT a.disciplines) AS DisciplineCount   -- Count distinct disciplines for each coach
FROM 
    COACH c
JOIN 
    ATHLETE a ON c.country_code = a.country_code       
GROUP BY 
    c.coach_name                                      -- Group by coach_name
HAVING 
    COUNT(DISTINCT a.disciplines) > 30                 -- display coches involed  more than 30 discipline
ORDER BY 
    c.coach_name ASC;                        -- ordering them based on coches name aphabetaclly
    

    
/* query 9: get the most medals won by each counrty, using limit get the top 10 */
    

select country_long as Country_Won_Most_medals, Total
from TOTAL_MEDAL 
order by 
     Total DESC 
limit 10;     
    






/* query10: using event table, athelets table,and   event_id from events table, countycode, atheltes_code from atheltes 
and medal_type from total_medals table remaed as total_medals,


get toatl_events, total_atheltes,  total_country  and total medals select queries.
*/



SELECT
    (SELECT COUNT(DISTINCT event_id) FROM EVENT) AS Total_Events,          
    (SELECT COUNT(DISTINCT country_code) FROM ATHLETE) AS Total_Countries,
    (SELECT COUNT(DISTINCT athlete_code) FROM ATHLETE) AS Total_Athletes,  
    (SELECT SUM(Gold_Medal + Silver_Medal + Bronze_Medal) FROM TOTAL_MEDAL) AS Total_Medals;
    
 
    
/* query11: calculates the male participlants percentages  in each discipline  Using athelets  table

get male participlants  percentages   ((sum of   male number) divided by (total male participlants number))
and mutiplying by 100 to get a percentage nd palceing it for 2 decimal 


*/   
    
    
SELECT 
    a.disciplines AS Games_participated_by_male,                              
    SUM(a.gender = 'M') AS Male,                           -- counts male participnast using Sum aggrigation fucntion
    COUNT(a.athlete_code) AS Total_athlete_num,                            -- Total number of participants
    ROUND((SUM(a.gender = 'M') / COUNT(a.athlete_code)) * 100, 2) AS Male_Participation  -- Male participation percentage
FROM 
    ATHLETE a
GROUP BY 
    a.disciplines                                              
ORDER BY 
    Male_Participation DESC;                                  -- ordering by  descending of male participlanst




/* query 12: calculates the Female participlants percentages  in each discipline  Using athelets  table
*/


SELECT 
    a.disciplines AS Games_participated_by_female,                             
    SUM(a.gender = 'F') AS Female,                            
    COUNT(a.athlete_code) AS Total_athlete_num,                          
    ROUND((SUM(a.gender = 'F') / COUNT(a.athlete_code)) * 100, 2) AS Female_Participation  
FROM 
    ATHLETE a
GROUP BY 
    a.disciplines                                              
ORDER BY 
    Female_Participation DESC; 
    
    
        
    
             
/*query13: get the coch name  ASSOCIATED WITH COUNRTY AND won  least 10 gold medals , used join and sub-queryy

*/           
             
SELECT 
    c.coach_name,                                   
    c.country_code AS COUNTRY,                          
    c.disciplines AS GAMES                   
FROM 
    COACH c                                         
INNER JOIN (
    SELECT 
        country_code,                               
        SUM(Gold_Medal) AS GOLD_TOTAL                
    FROM 
        TOTAL_MEDAL                                  
    GROUP BY 
        country_code                                 
    HAVING 
        SUM(Gold_Medal) >= 10                        
) AS WINNER_OF_MEDAL

ON c.country_code = WINNER_OF_MEDAL.country_code;                                  
   
 






/*  query 14: retrive the current age of the  athlete  using DATEDIFF formet  and 
renamed the table CURRENT_AGE_ATHELETS,name, gender, medal_type and discipline from MEDALLIST TABLE 
*/  

SELECT 
    name,
    birth_date,
    FLOOR(DATEDIFF(CURDATE(), birth_date) / 365.25) AS CURRENT_AGE_ATHLETS,
    gender,
    medal_type,
    discipline
FROM 
    MEDALLIST;




/*query 15: Compare medals beteen Feamale & Male */

SELECT
  
    gender,
    discipline,
    COUNT(*) AS total_medals,
    SUM(CASE WHEN medal_type = 'Gold Medal' THEN 1 ELSE 0 END) AS Gold_Medals,
    SUM(CASE WHEN medal_type = 'Silver Medal' THEN 1 ELSE 0 END) AS Silver_Medals,
    SUM(CASE WHEN medal_type = 'Bronze Medal' THEN 1 ELSE 0 END) AS Bronze_Medals
FROM 
    MEDALLIST
GROUP BY 
    discipline, gender
ORDER BY 
    discipline;
    


/* query16: find out the Medals by discipline  */
    
SELECT discipline, COUNT(*) AS total_medals
FROM MEDALLIST
GROUP BY discipline
ORDER BY total_medals DESC;
 



/* query 17:list down the athletes age group and compare  how many medals( medal_type) they have win  based on age group 
*/     

  
  
SELECT 
   CASE 
      WHEN YEAR(CURDATE()) - YEAR(birth_date) < 20 THEN 'UNDER 20'
      WHEN YEAR(CURDATE()) - YEAR(birth_date) BETWEEN 20 AND 29 THEN 'AGE between 20 to 29'
      WHEN YEAR(CURDATE()) - YEAR(birth_date) BETWEEN 30 AND 39 THEN 'AGE between 30 to 39'
      ELSE ' AGE OVER 40'
   END AS ATHLETES_AGE_GROUP,
   gender,
   COUNT(*) AS MEDAL_TOTAL,
   SUM(CASE WHEN medal_type = 'Gold Medal' THEN 1 ELSE 0 END) AS Gold_Medals,
   SUM(CASE WHEN medal_type = 'Silver Medal' THEN 1 ELSE 0 END) AS Silver_Medals,
   SUM(CASE WHEN medal_type = 'Bronze Medal' THEN 1 ELSE 0 END) AS Bronze_Medals
FROM
   MEDALLIST
GROUP BY
   ATHLETES_AGE_GROUP, gender
ORDER BY
  MEDAL_TOTAL DESC, ATHLETES_AGE_GROUP, gender;
  




/* query18: find out the youngest athlete  using birthdate  from MEDALLIST TABLE, also name, code of the althlete, gender, discipline,
 events, medal_type ,is_medallist 
*/


SELECT
   name ,
   code_athlete,
   gender,
   birth_date,
   discipline,
   events,
   medal_type,
   medal_date,
   is_medallist
FROM 
  MEDALLIST
WHERE birth_date = (SELECT MIN(birth_date) FROM MEDALLIST);
   

 

    
/* query19: from MEDALLIST find out top Atheltes by counting medal , use limit to get only top 10 */


SELECT name, country_code, COUNT(*) AS medal_count
FROM MEDALLIST
GROUP BY name, country_code
ORDER BY medal_count DESC
LIMIT 10;
 
 
/* query20: from SCGEDULE TABLE  get the start_date  and then  */


 
SET time_zone = '+00:00' ;
SELECT @@session.time_zone;
select start_date from SCHEDULE;
   
 
/* query21: from SCGEDULE TABLE  get the start_date, end_date , vanue_code when status is cancelled   */   
SELECT start_date, end_date, venue_code  FROM SCHEDULE WHERE status = 'CANCELLED';
 
