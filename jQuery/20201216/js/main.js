$(function(){
  $('#box1').on('mouseover',function(){
    $(this).css({
      width : '150px',
      height : '150px'
    });
  })
  .on('mouseout',function(){
    $(this).css({
      width:'',
      height:''
    });
  });
});
const added1 = add(3,5);
const added2 = add(4, 10);
function add(n1,n2){
  return n1 + n2;
}
document.getElementById('num2').textContent = added1;
console.log(added1);
$(function(){
  $('#box3')
  .on('mouseover',function(){
    document.getElementById('num3').textContent = added2;
  })
  .on('mouseout',function(){
    $(this).css('display','none');
  });
});
const a=100;
const b=200;
const c=300;
switch(200){
  case a:
    document.getElementById('num4').textContent = a;
    break;
  case b:
    document.getElementById('num4').textContent = b;
    break;
  case c:
    document.getElementById('num4').textContent = c;
    break;
}
let array = [1,2,3,4,5,6,7,8,9,10];
let array_a = 0;
// for (let i = 0, len=array.length; i < len; i++){
//   array_a += array[i];
// }
// console.log(array_a);
for (let i = 0, len=array.length; i < len; i ++){
  let number = array[i];
  if (number % 5 === 0){
    break;
  }else if(number % 2 === 1){
    console.log(number);
    continue;
  }
  array_a += number;
}