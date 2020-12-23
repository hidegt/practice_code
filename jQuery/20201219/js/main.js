$(function(){
  let duration = 400;
  $('header').typoShadow();

  $('#button button:nth-child(-n+3)')
    .on('mouseover',function(){
      $(this).stop(true).animate({
        backgroundColor: '#aa5e9b'
      },duration)
    })
    .on('mouseout',function(){
      $(this).stop(true).animate({
        backgroundColor:''
      },duration)
    });
});