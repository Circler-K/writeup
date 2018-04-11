/*
(function ck()
{
lv5frm.cmt.value=1;
lv5frm.id.value=1;
lv5frm.hack.value=lv5frm.attackme.value;

lv5frm.submit();

})()
*/
var fs = require('fs');
console.log(2); // 실행순서 1
fs.readFile('data.txt', 'utf8', function(err, data){
  console.log(3); // 실행순서 3
  console.log(data); // 실행순서 4
})
console.log(4); // 실행순서 2