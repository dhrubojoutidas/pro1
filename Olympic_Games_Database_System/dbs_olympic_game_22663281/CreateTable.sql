/* CreateTable.sql  is the file for creating tables for Olympic Games 2024 database details.
HERE, 7 types of Tables are created .

1.COACH TABLE     -- this table contains the deatils of coches .
2. ATHLETE TABLE  -- details of atheltes of the game
3. TEAM  TABLE    -- details of team  game details
4. TOTAL_MEDAL    --details of total medal of the game
5. EVENT TABLE    -- contains details of event of the game
6.MEDALLIST TABLE -- contains the details of all medallist 
7. SCHEDULE TABLE -- contains the details of event schedule of all game
*/



-- 1. Creating COACH TABLE

DROP TABLE IF EXISTS COACH;

CREATE TABLE COACH (
    coach_code VARCHAR (100),   -- code of coach in COACH TABLE         
    coach_name CHAR(70) NOT NULL,   -- name of coach       
    gender CHAR(3) NOT NULL,      -- coch gender         
    coach_function VARCHAR(50) NOT NULL,   -- coach fucntion (eg : head, assistant )             
    country_code CHAR(3) NOT NULL,      -- country of the code
    country_long VARCHAR(100),      -- full country name         
    disciplines VARCHAR(200) NOT NULL,    -- name of games/ discipline
    events VARCHAR(100),                -- all the events name    
    PRIMARY KEY (coach_code)             -- primary key of COACH TABLE
);



-- 2. Creating ATHLETE  TABLE

DROP TABLE IF EXISTS ATHLETE;

CREATE TABLE ATHLETE (
    athlete_code VARCHAR (100),             
    name CHAR(70) NOT NULL,                -- Full name of athlete
    name_short VARCHAR(100) NOT NULL,      -- atheltes name short form
    name_tv VARCHAR(90) NOT NULL,          -- name of athelete display like TV
    gender CHAR(1) NOT NULL,               -- gender of ATHELETE TABLE  (G/F)
    country_code CHAR(3) NOT NULL,      -- country code
    country_long VARCHAR(100) NOT NULL,    -- full country name
    disciplines VARCHAR(200) NOT NULL,     -- name of games/ discipline
    events VARCHAR(100) NOT NULL,          -- details of events
    

    PRIMARY KEY (athlete_code)         -- primary key OF ATHELTE TABLE
    
   
);

-- 3. Creating team TABLE


DROP TABLE IF EXISTS TEAM;

CREATE TABLE TEAM (
    code VARCHAR(100) PRIMARY KEY,        -- Primary key  TEAM TABLE
    team_gender CHAR(1) NOT NULL,         -- Gender of team (M/F/X)
    country_code CHAR(3) NOT NULL,     -- country code 
    country VARCHAR(50) NOT NULL,         -- country name 
    country_long VARCHAR(100) NOT NULL,   -- full country name
    discipline VARCHAR(200) NOT NULL,     -- games/ discipline  name
    disciplines_code VARCHAR(6) NOT NULL, -- discipline /game code(short way)
    events VARCHAR(100) ,                 -- events of team
    num_athletes INT                    -- number of athelets 
    
);



-- 4  Create total_medals TABLE 
DROP TABLE IF EXISTS TOTAL_MEDAL;

CREATE TABLE TOTAL_MEDAL (
   
    country_code  CHAR(3) NOT NULL,          -- Country code
    country_long VARCHAR(100) NOT NULL,         -- fullcountry name
    Gold_Medal  INT(4),                         -- counts gold medal
    Silver_Medal  INT(4),                       -- count silver medal 
    Bronze_Medal  INT(4),                       -- counts bronze medal
    Total INT(4) ,                               -- total medal
    medal_id INT AUTO_INCREMENT PRIMARY KEY   -- primary key  auto_increment
);



-- 5 creating EVENT TABLE

DROP TABLE IF EXISTS EVENT;
CREATE TABLE EVENT(

    
    event VARCHAR(100) NOT NULL, -- events name in EVENT table
    sport  VARCHAR(200) NOT NULL, -- sport/game/ discipline name
    sport_code VARCHAR(10) NOT NULL, -- sport/game/ discipline code
    event_id INT PRIMARY KEY AUTO_INCREMENT   -- primary key of EVENT table auto_increment
   
);

   
 -- 6  CREATE MEDALISTIST TABLE

DROP TABLE IF EXISTS MEDALLIST;

CREATE TABLE MEDALLIST (
    medal_date DATE,   -- date of  getting medal 
    medal_type VARCHAR(20), -- TYPE of medal
    medal_code INT,       -- code of  medal
    name VARCHAR(70),  -- name of medallist
    gender CHAR(1),    -- gender of medallist
    country_code CHAR(3) NOT NULL,  -- country code of medallist
    country_long VARCHAR(100) NOT NULL, -- full country name of medallist
    team_gender CHAR(1),  --  gender of the medallist (M/F)
    discipline VARCHAR(200),  -- discipline/ sports/game name of the medalist
    events VARCHAR(100),  -- event name of the medallist
    event_type VARCHAR(20),  -- event TYPE of medallist
    birth_date DATE ,    --  birth date of mdallist
    code_athlete VARCHAR(100),   -- athelete code  of medalllist
    code_team VARCHAR(100),   -- team code of medalllist
    is_medallist BOOL,    -- checking  winner medallist is or not using true/false
    medalist_id INT PRIMARY KEY AUTO_INCREMENT,   -- using primary key as auto_increment
    FOREIGN KEY (code_athlete) REFERENCES ATHLETE (athlete_code) ON DELETE CASCADE,  -- using ATHELET table pk(athlete_code) as fk(code_athlete)
    FOREIGN KEY (code_team) REFERENCES TEAM (code) ON DELETE CASCADE  -- using TEAM table pk(code) as fk(code_team)
); 
   
   -- 7 Create TABLE SCHEDULE
   
DROP TABLE IF EXISTS SCHEDULE;

CREATE TABLE SCHEDULE (
    start_date TIMESTAMP ,  -- start date of event schedule using timestamp formet to hold UTC timezone
    end_date TIMESTAMP,  -- end date of event schedule using timestamp formet to hold UTC timezone
    status VARCHAR(20) NOT NULL,  -- shows the event finished/ cancelled
    discipline VARCHAR(200) NOT NULL,   -- name of discipline/ sports/ games
    discipline_code VARCHAR(60) NOT NULL,	-- short version of discipline/ sports code 
    event VARCHAR(100),	 -- events name
    event_medal	 INT,   -- medal of  the event
    phase VARCHAR(100),   -- 
    gender CHAR(1),	   -- gender   (G/F)
    event_type	VARCHAR(20),  -- details of event TYPE
    venue  VARCHAR(100),	  -- venue name  that discipline occured
    venue_code VARCHAR(60),  -- short  version of venue code
    schedule_id INT PRIMARY KEY AUTO_INCREMENT     -- using primary key as auto_increment SCHEDULE TABLE
    
);
    
 

  
  
  
   
