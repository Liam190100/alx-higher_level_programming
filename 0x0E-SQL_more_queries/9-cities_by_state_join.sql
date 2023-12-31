--- Lists all cities contained in the database hbtn_0d_usa.
--- display: cities.id - cities.name - states.name.

SELECT cities.id, cities.name,
  (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
