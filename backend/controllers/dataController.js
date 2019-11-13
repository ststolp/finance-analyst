const pythonService = require("../services/python.service");
const jsonService = require("../services/json.service");

function getReport(req, res) {
    let start = new Date(req.query.startDate);
    let end = new Date(req.query.endDate);
    const now = new Date();      `${start.getMonth() + 1}/${start.getDate() + 1}/${start.getFullYear()}`
    startFormated = `${start.getMonth() + 1}/${start.getDate() + 1}/${start.getFullYear()}`;
    endFormated = `${end.getMonth() + 1}/${end.getDate() + 1}/${end.getFullYear()}`;
    nowFormated = `${now.getMonth() + 1}/${now.getDate() + 1}/${now.getFullYear()}`;
    console.log(`${startFormated}, ${endFormated}, ${nowFormated}`);
    pythonService.get_report(startFormated, endFormated, nowFormated).then(function(results) {
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
    let date = new Date(req.body.date);
    let dateFormated = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate() + 1}`;
    let entry = `\n${dateFormated},${req.body.payment_to},${req.body.method},${req.body.category},${req.body.description},${req.body.amount}`;
    jsonService.add_expense(entry).then(function(response) {
        res.redirect(200, '/expense_form');
    });
};

function addIncome(req, res) {
    let date = new Date(req.body.date);
    let dateFormated = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate() + 1}`;
    let entry = `\n${dateFormated},${req.body.from},${req.body.type},${req.body.amount}`;
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