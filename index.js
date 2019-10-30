/* Beginning of index file */
const http = require('http');
const express = require('express');
const viewsController = require("./backend/controllers/viewsController.js");
const dataController = require("./backend/controllers/dataController.js");
const jsReport = require("./frontend/js/report.js");
const session = require('express-session');
let port = 5000;
// const bodyParser = require('body-parser');
// const bcrypt = require('bcrypt');
//const { Pool } = require("pg");
const app = express();
// const saltRounds = 10;

// const connectionString = process.env.DATABASE_URL;
// const pool = Pool({connectionString: connectionString});

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

/* html page requests  */
app.get("/", viewsController.home);
app.get("/expense_form", viewsController.expenseForm);
app.get("/income_form", viewsController.incomeForm);
app.get("/report_page", viewsController.reportPage);

/*  AJAX request endpoints  */
app.get("/getExpenses", dataController.getExpenses);
app.get("/getIncomes", dataController.getIncomes);
app.get("/getReport", dataController.getReport);

app.post("/addIncome", dataController.addIncome);
app.post("/addExpense", dataController.addExpense);
//app.get("/js/report.js", jsReport.plotReport);

app.listen(app.get('port'), function() {
	console.log(`  Finance-Analyst running on port: ${port}`);
});