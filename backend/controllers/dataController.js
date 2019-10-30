const pythonService = require("../services/python.service");
const jsonService = require("../services/json.service");

function getReport(req, res) {
    let startDate = req.query.startDate;
    let endDate = req.query.endDate;
    console.log(startDate + ', ' + endDate);
    pythonService.get_report(startDate, endDate).then(function(results) {
        console.log(`Service: ${results}`);
        res.status(200).json(results);
    });
};

function getExpenses(req, res) {
    jsonService.get_expenses().then(function(expenses) {
        res.status(200).json(expenses);
    });
};

function getIncomes(req, res) {
    jsonService.get_incomes().then(function(incomes) {
        res.status(200).json(incomes);
    });
};

function addExpense(req, res) {
    //TODO
    //   I might not be able to use jsonService like this
    let date = Date.parse(req.body.date);
    let entry = `\n${date},${req.body.payment_to},${req.body.method},${req.body.category},${req.body.description},${req.body.amount}`;
    console.log(`${req.body.date}, ${req.body.payment_to}, ${req.body.method}, ${req.body.description}, ${req.body.amount}`);
    jsonService.add_expense(entry).then(function(response) {
        res.redirect(200, '/expense_form');
    });
};

function addIncome(req, res) {
    //TODO
    let date = Date.parse(req.body.date);
    let entry = `\n${date},${req.body.from},${req.body.type},${req.body.amount}`;
    jsonService.add_income(entry).then(function(incomes) {
        res.redirect(200, '/income_form');
    });
};

module.exports = {
    getExpenses: getExpenses,
    getIncomes: getIncomes,
    getReport: getReport,
    addIncome: addIncome,
    addExpense: addExpense
};