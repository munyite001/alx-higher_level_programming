$(document).ready(function () {
  const proxyUrl = 'https://crossorigin.me/';
  const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.getJSON(proxyUrl + apiUrl, function (data) {
    $('div#hello').text(data.hello);
  });
});
