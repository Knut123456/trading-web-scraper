Du må fulle ut user og passord, 

vis du vil ha en annen navn til DATABASE så fjern trading_web_scraper og skriv hva du vil ha.

CREATE DATABASE trading_web_scraper;
CREATE USER ' '@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON trading_web_scraper.* TO ''@'%';


CREATE USER ' '@'%' IDENTIFIED BY '';
GRANT SELECT, INSERT, UPDATE, ALTER, DROP ON trading_web_scraper.* TO ''@'%';
FLUSH PRIVILEGES;

CREATE DATABASE trading_web_scraper_usefull_info;
CREATE USER ' '@'%' IDENTIFIED BY '';
GRANT SELECT, INSERT, UPDATE, ALTER, DROP ON trading_web_scraper_usefull_info.* TO ''@'%';
FLUSH PRIVILEGES;

