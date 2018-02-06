DB_HOST = ""
DB_PORT = 3306
DB_USERNAME = ""
DB_PASSWORD = ""
DB_DATABASE = ""

SELECT_ONE_DATA = "select id, temperature, birth from data order by id desc limit 1"
SELECT_LAST_TEN_DATA = "SELECT id, temperature, birth FROM data ORDER BY id DESC limit {count}"
