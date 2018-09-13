var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rl.question("What are you hours and wages? ", function(hours, wages){
    var salary = hours*wages;
    console.log(salary);

    rl.close();
});
