/* controller to serve up pages  */

function home(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('home.html');
};

function expenseForm(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    //pythonService.run("hello", "what", "Yes");
    res.status(200).redirect('expense_form.html');
};

function incomeForm(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('income_form.html');
};

function reportPage(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('report.html');
};

module.exports = {
    home: home,
    expenseForm: expenseForm,
    incomeForm: incomeForm,
    reportPage: reportPage 
};