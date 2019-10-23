let {PythonShell} = require('python-shell');

module.exports.execute = function(arg1, arg2, arg3) {
  return new Promise((resolve, reject) => {
    let options = {
      mode: 'text',
    // pythonPath: 'path/to/python',
      pythonOptions: ['-u'], // get print results in real-time
      scriptPath: 'C:/Users/scsto/finance-analyst/backend/pythonScripts',
      args: [arg1, arg2, arg3]
    };

    /* TODO have this function return a promise */

    PythonShell.run('python.py3', options, function (err, results) {
      
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
        if (err) reject(err);
        resolve(results);
    });
  });
}

// PythonShell.run = new Promise('python.py3', options, function (err, results) {
//   if (err) throw err;
//   // results is an array consisting of messages collected during execution
//   console.log('results: %j', results);
  
//   return results;
// });
// }