$(function() {
$('.navbar-toggler').on('click', function() {
  if($('#navmenu1').hasClass('show')) {
      $('#navmenu1').removeClass('show');
  } else {
    $('#navmenu1').addClass('show');
  }
});
});
