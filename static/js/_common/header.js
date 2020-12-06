$(function() {
$('.navbar-toggler').on('click', function() {
  if($('#navmenu1').hasClass('show')) {
      $('#navmenu1').removeClass('show');
  } else {
    $('#navmenu1').addClass('show');
  }
});
});

/**
 * 
 * Cookieから必要なパラメータを取得するために使用
 * ※ ajaxするためにCSRFトークンを設定するために使用している
 * // TODO 共通化する
 * 
 */
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
