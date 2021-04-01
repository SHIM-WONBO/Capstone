var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '2222',
  database : 'ddb'
});
 
connection.connect();
 
connection.query('SELECT * FROM test_num', function (error, results, fields) {
  if(error) {
      console.log(error);
  }
  console.log(results);
});
 
connection.end();