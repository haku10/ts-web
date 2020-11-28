jQuery(function($) {

  // ajaxの前に実行される処理
  $.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
});
  /**
   *　csvファイルアップロード処理
   *  // TODO ajaxの処理は共通化する
   * 
   */ 
$('#upload_btn').on('click', function(){
  var formData = new FormData();
  var csvfile = $('#csvtext')[0].files[0];
  formData.append('csvfile', csvfile);
  // Ajax通信を開始
  $.ajax({
    url: "texttospeech/upload",
    type: 'POST',
    data: formData,
    processData: false,
    contentType: false,
    enctype:  'multipart/form-data',
    timeout: 10000,
  }).done(function(data) {
      // 通信成功時の処理を記述
      $('#resultGET').text('POST処理成功：' + data);
  }).fail(function() {
      // 通信失敗時の処理を記述
      $('#resultGET').text('POST処理失敗.');
  });
  })
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
