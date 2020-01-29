const mysql = require('mysql');

module.exports = () => {
  return mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Dacc9524',
    database: 'movie_db'
  });
}