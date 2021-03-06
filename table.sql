CREATE TABLE `weather` (
   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
   `dateutc` datetime NOT NULL,
   `tempinf` float NOT NULL,
   `humidityin` float NOT NULL,
   `baromrelin` float NOT NULL,
   `baromabsin` float NOT NULL,
   `tempf` float NOT NULL,
   `humidity` float NOT NULL,
   `winddir` float NOT NULL,
   `windspeedmph` float NOT NULL,
   `windgustmph` float NOT NULL,
   `maxdailygust` float NOT NULL,
   `hourlyrainin` float NOT NULL,
   `eventrainin` float NOT NULL,
   `dailyrainin` float NOT NULL,
   `weeklyrainin` float NOT NULL,
   `monthlyrainin` float NOT NULL,
   `totalrainin` float NOT NULL,
   `solarradiation` float NOT NULL,
   `uv` float NOT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;