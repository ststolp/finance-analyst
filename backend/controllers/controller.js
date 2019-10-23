/* controller  */
const pythonService = require("../services/python.service");

function runScript() {
    pythonService.execute("I", "am", "blue").then(function(results) {
        console.log(`Service: ${results}`);
    });
   // req.headers['if-none-match'] = 'no-match-for-this';
    // TODO: Set up an ajax request to handle the response from the script
    //res.status(200).redirect(`report.html&results=${results}`);
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