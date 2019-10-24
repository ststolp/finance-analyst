const pythonService = require("../services/python.service");
const jsonService = require("../services/json.service");

function getReport(req, res) {
    pythonService.get_txns("read", "am", "blue").then(function(results) {
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
    jsonService.add_expense(req);
};

function addIncome(req, res) {
    //TODO
    //   I might not be able to use jsonService like this
    jsonService.add_income(req);
};

module.exports = {
    getExpenses: getExpenses,
    getIncomes: getIncomes,
    getReport: getReport,
    addIncome: addIncome,
    addExpense: addExpense
};