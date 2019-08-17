

$(document).ready(function(){

  $('.open-search-link').magnificPopup({
      type: 'inline',
      midClick: true,
      mainClass: 'mfp-fade'
  });
  $('.open-login-link').magnificPopup({
      type: 'inline',
      midClick: true,
      mainClass: 'mfp-fade'
  });


  $( "#login-popup .input" ).focusin(function() {
    $( this ).find( "span" ).animate({"opacity":"0"}, 200);
  });
  
  $( "#login-popup .input" ).focusout(function() {
    $( this ).find( "span" ).animate({"opacity":"1"}, 300);
  });
  
  $("#login-popup .login").submit(function(){
    $("#login-popup .loginButton").css({"background":"#2ecc71", "border-color":"#2ecc71"});
    $("#login-popup input").css({"border-color":"#2ecc71"});
    return false;
  });


  $('#loginButton').click(function(){
    let formData = new FormData();

    formData.append("username", $("#userName").val());
    formData.append("password", $("#password").val());

    $.ajax({
        url: $(this).data('url'),
        data: formData,
        processData: false,
        contentType: false,
        type: "POST",
        success: function (data) {
            console.log(data);
            window.location.href = data.url;
        },
        error: function (data) {
            $('.loginError').addClass('show');
        },
    });
  });

});



/*
var skillsDiv = $('#skills');

$(window).on('scroll', function(){
	var winT = $(window).scrollTop(),
  	winH = $(window).height(),
  	skillsT = skillsDiv.offset().top;
  if(winT + winH  > skillsT){
  	$('.skillbar').each(function(){
      $(this).find('.skillbar-bar').animate({
        width:$(this).attr('data-percent')
      },2000);
    });
  }
});*/