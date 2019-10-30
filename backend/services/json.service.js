/* Beginning of json service -- the service appends data onto the expence and income json object files */
const fs = require('fs');

function add_income(entry) {
    return new Promise((resolve, reject) => {
        try {
            fs.appendFileSync("C:/Users/scsto/finance-analyst/backend/data/income.csv", entry);
            resolve();
        } catch (err) {
           console.log(` json.service: ${err}`);
           reject();
        }
    });
};

function add_expense(entry) {
    return new Promise((resolve, reject) => {
        try {
            // let data = fs.readFileSync("C:/Users/scsto/finance-analyst/backend/data/expense.csv", "utf-8");
            // console.log(`data: ${data}`);
            // let newFile = data.replace(/]}$/, '');
            // console.log(`newFile: ${newFile}`);
            // fs.writeFileSync("C:/Users/scsto/finance-analyst/backend/data/expense.csv", newFile);
            fs.appendFileSync("C:/Users/scsto/finance-analyst/backend/data/expense.csv", entry);
            resolve();
        } catch (err) {
        console.log(` json.service: ${err}`);
            reject();
        }
    });
};

function get_expenses() {

};

function get_incomes() {

};

module.exports = {
   add_income: add_income,
   add_expense: add_expense,
   get_expenses: get_expenses,
   get_incomes: get_incomes
};