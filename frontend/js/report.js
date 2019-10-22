let plotReport = function() {
    let Plotly = require("../../node_modules/plotly")('', '');
    let income = {
        x: [2015, 2016, 2017, 2018],
        y: [20000, 10000, 500, 300],
        type: 'scatter'
    };

    let home = {
        x: [2015, 2016, 2017, 2018],
        y: [200, 100, 500, 1000],
        type: 'scatter'
    };

    let auto = {
        x: [2015, 2016, 2017, 2018],
        y: [600, 500, 450, 800],
        type: 'scatter'
    };

    let data = [income, home, auto];
    var initGraphOptions = {fileopt : "extend", filename : "nodenodenode"};
    Plotly.plot(data, initGraphOptions, function(err, mess) {
        console.log(mess);
    });
};

module.exports = {
    plotReport: plotReport
}