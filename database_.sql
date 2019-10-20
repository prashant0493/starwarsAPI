
/*Create database*/

CREATE DATABASE starwarsDB;
USE starwarsDB;

/*create tables */

CREATE TABLE `species`(
    `species_id` INT(11) NOT NULL,
    `average_height` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `average_lifespan` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `classification` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `designation` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `eye_colors` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `hair_colors` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `homeworld` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `name` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `skin_colors` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    PRIMARY KEY (`species_id`)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `characters` (
    `char_id` INT(11) NOT NULL,
    `name` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `height` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `mass` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `hair_color` VARCHAR(50) COLLATE 'utf8_unicode_ci',
    `skin_color` VARCHAR(50) COLLATE 'utf8_unicode_ci',
    `eye_color` VARCHAR(50) COLLATE 'utf8_unicode_ci',
    `birth_year` VARCHAR(50) COLLATE 'utf8_unicode_ci',
    `gender` VARCHAR(50) COLLATE 'utf8_unicode_ci',
    `homeworld` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    `films` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `species` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `vehicles` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `starships` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
     PRIMARY KEY (`char_id`)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `film` (

    `film_id` INT(11) NOT NULL,
    `title` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `episode_id` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `opening_crawl` VARCHAR(2000) COLLATE 'utf8_unicode_ci',
    `director` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `producer` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `release_date` DATE,
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    `characters` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `planets` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `starships` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `vehicles` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    `species` VARCHAR(1000) COLLATE 'utf8_unicode_ci',
    PRIMARY KEY (`film_id`)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `vehicle`(

    `vehicle_id` INT(11) NOT NULL,
    `cargo_capacity` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `consumables` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `cost_in_credits` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `crew` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `length` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `manufacturer` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `max_atmosphering_speed` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `model` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `name` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `passengers` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `vehicle_class` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    `film_id` INT(11),
    `char_id` INT(11),
    PRIMARY KEY (`vehicle_id`)
 ) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `starship`(

    `starship_id` INT(11) NOT NULL,
    `MGLT` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `cargo_capacity` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `consumables` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `cost_in_credits` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `crew` INT(11),
    `hyperdrive_rating` INT(11),
    `length` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `manufacturer` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `max_atmosphering_speed` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `model` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `name` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `starship_class` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `passengers` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    `film_id` INT(11),
    `char_id` INT(11),
    PRIMARY KEY (`starship_id`)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `planet`(

    `planet_id` INT(11) NOT NULL,
    `climate` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `diameter` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `gravity` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `name` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `orbital_period` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `population` INT(11),
    `rotation_period` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `surface_water` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `terrain` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `created` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `edited` VARCHAR(250) COLLATE 'utf8_unicode_ci',
    `url` VARCHAR(500) COLLATE 'utf8_unicode_ci',
    `film_id` INT(11),
    `char_id` INT(11),
    PRIMARY KEY (`planet_id`)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;

/* many-to-many relationships with ``characters`` table and other tables*/

CREATE TABLE `CharPlanetRelation`(
    `char_id` INT(11),
    `planet_id` INT(11) NOT NULL,
    FOREIGN KEY (char_id) REFERENCES characters(char_id),
    FOREIGN KEY (planet_id) REFERENCES planet(planet_id),
    UNIQUE (char_id, planet_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `CharStarshipRelation`(
    `starship_id` INT(11) NOT NULL,
    `char_id` INT(11) NOT NULL,
    FOREIGN KEY (starship_id) REFERENCES starship(starship_id),
    FOREIGN KEY (char_id) REFERENCES characters(char_id),
    UNIQUE (starship_id, char_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `CharVehicleRelation`(
    `char_id` INT(11),
    `vehicle_id` INT(11) NOT NULL,
    FOREIGN KEY (char_id) REFERENCES characters(char_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id),
    UNIQUE (char_id, vehicle_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `CharFilmRelation`(
    `char_id` INT(11),
    `film_id` INT(11) NOT NULL,
    FOREIGN KEY (char_id) REFERENCES characters(char_id),
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    UNIQUE (char_id, film_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `CharSpeciesRelation`(
    `char_id` INT(11),
    `species_id` INT(11) NOT NULL,
    FOREIGN KEY (char_id) REFERENCES characters(char_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    UNIQUE (char_id, species_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


/* many-to-many relationships with ``film`` table and other tables*/

CREATE TABLE `FilmPlanetRelation`(
    `film_id` INT(11),
    `planet_id` INT(11) NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    FOREIGN KEY (planet_id) REFERENCES planet(planet_id),
    UNIQUE (film_id, planet_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `FilmVehicleRelation`(
    `film_id` INT(11) ,
    `vehicle_id` INT(11) NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id),
    UNIQUE (film_id, vehicle_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `FilmStarshipRelation`(
    `film_id` INT(11),
    `starship_id` INT(11) NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    FOREIGN KEY (starship_id) REFERENCES starship(starship_id),
    UNIQUE (film_id, starship_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `FilmSpeciesRelation`(
    `film_id` INT(11),
    `species_id` INT(11) NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    UNIQUE (film_id, species_id)
) Engine=InnoDB DEFAULT CHARSET=utf8mb4;



/*.
DEFAULT CHARSET=utf8mb4 based on random recommendation found on the internet
https://www.eversql.com/mysql-utf8-vs-utf8mb4-whats-the-difference-between-utf8-and-utf8mb4/
*/
