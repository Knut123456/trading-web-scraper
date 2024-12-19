

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

