let {PythonShell} = require('python-shell');

module.exports.run = function(arg1, arg2, arg3) {
  let options = {
    mode: 'text',
  // pythonPath: 'path/to/python',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: 'C:/Users/scsto/finance-analyst/backend/pythonScripts',
    args: [arg1, arg2, arg3]
  };

  PythonShell.run('python.py3', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
  });
}