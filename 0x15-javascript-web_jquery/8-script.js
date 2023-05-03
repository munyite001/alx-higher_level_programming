$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    for (const item of data.results) {
      $('ul#list_movies').append(`<li>${item.title}</li>`);
    }
  });
});
