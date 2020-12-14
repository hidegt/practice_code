$(function(){
  $('.main-title').on('click',function(){
    $('.main-title').css('color','red');
  })
  .on('mouseover',function(){
    $('#main').animate({
      backgroundColor : '#ebc000'
    },
    1500
    );
  });
});

// $(function(){
//   $('#main').on('click',function(){
//     $('#main').animate({
//       backgroundColor : '#ebc000'
//     },
//     1500
//     );
//   });
// });