/* Beginning of index file */
const http = require('http');
const express = require('express');
const controller = require("./backend/controllers/controller.js");
const jsReport = require("./frontend/js/report.js");
// const pythonService = require("./backend/services/python.service");
const session = require('express-session');
let port = 5000;
// const bodyParser = require('body-parser');
// const bcrypt = require('bcrypt');
//const { Pool } = require("pg");
const app = express();
// const saltRounds = 10;

// const connectionString = process.env.DATABASE_URL;
// const pool = Pool({connectionString: connectionString});

// pythonService.run("hello", "what", "Yes");

app.use(session({
  name: 'server-session-cookie-id',
  secret: 'my express secret',
  saveUninitialized: true,
  resave: false,
}))

app.set('port', (/*process.env.PORT || */port));
app.use(express.static("frontend/views"));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.get("/", controller.home);
app.get("/getTxnUI", controller.txnUI);
app.get("/getReport", controller.getReport);
app.get("/getTxns", controller.getTxns);
//app.get("/js/report.js", jsReport.plotReport);


app.listen(app.get('port'), function(){
	console.log(`  Finance-Analyst running on port: ${port}`);
});