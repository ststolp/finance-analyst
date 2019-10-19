/* controller  */
const pythonService = require("../services/python.service");

function runScript() {
    pythonService.run("I", "am", "blue");
};

function home(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('home.html');
};

function report(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('report.html');
}

function txnUI(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    //pythonService.run("hello", "what", "Yes");
    res.status(200).redirect('txnUI.html');
}

module.exports = {
    home: home,
    report: report,
    txnUI: txnUI,
    runScript: runScript
};