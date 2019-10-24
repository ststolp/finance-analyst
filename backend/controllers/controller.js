/* controller  */
const pythonService = require("../services/python.service");

function getTxns(req, res) {
    pythonService.get_txns("read", "am", "blue").then(function(results) {
        console.log(`Service: ${results}`);
        res.status(200).json(results);
    });
   // req.headers['if-none-match'] = 'no-match-for-this';
    // TODO: Set up an ajax request to handle the response from the script
    //res.status(200).redirect(`report.html&results=${results}`);
};

function getReport(req, res) {
    pythonService.get_report("I", "am", "blue").then(function(results) {
        console.log(`Service: ${results}`);
        //res.status(200).json(results);
       res.status(200).json(results);
    });
   // req.headers['if-none-match'] = 'no-match-for-this';
    // TODO: Set up an ajax request to handle the response from the script
    //res.status(200).redirect(`report.html&results=${results}`);
};


function home(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    res.status(200).redirect('home.html');
};

function txnUI(req, res) {
    req.headers['if-none-match'] = 'no-match-for-this';
    //pythonService.run("hello", "what", "Yes");
    res.status(200).redirect('txnUI.html');
}

module.exports = {
    home: home,
    txnUI: txnUI,
    getReport: getReport,
    getTxns: getTxns
};