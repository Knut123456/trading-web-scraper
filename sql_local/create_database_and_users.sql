
CREATE DATABASE trading_web_scraper_usefull_info;
CREATE DATABASE trading_web_scraper;

CREATE USER 'trading_web_scraper_user_admin'@'%' IDENTIFIED BY '1234';
CREATE USER 'trading_web_scraper_user_normal_user'@'%' IDENTIFIED BY '4321';

GRANT ALL PRIVILEGES ON trading_web_scraper.* TO 'trading_web_scraper_user_admin'@'%';
GRANT ALL PRIVILEGES ON trading_web_scraper_usefull_info.* TO 'trading_web_scraper_user_admin'@'%';


GRANT SELECT, INSERT, UPDATE, ALTER, DROP ON trading_web_scraper.* TO 'trading_web_scraper_user_normal_user'@'%';



GRANT SELECT, INSERT, UPDATE, ALTER, DROP ON trading_web_scraper_usefull_info.* TO 'trading_web_scraper_user_normal_user'@'%';
FLUSH PRIVILEGES;

