$(function(){
  $('#main').on('click',function(){
    $('.main-title').css('color','red');
  })
  .on('mouseover',function(){
    $('#main').stop(true).animate({
      backgroundColor : '#ebc000'
    },
    1500,
    'swing'
    );
    $('header, footer').stop(true).animate({
      backgroundColor: ''
    },
    1500,
    'easeOutCirc'
    );
  })
  .on('mouseout',function(){
    $('#main').stop(true).animate({
      backgroundColor: ''
    },
    1500
    );
    $('header, footer').css({
      backgroundColor: 'aquamarine'
    });
  });
});