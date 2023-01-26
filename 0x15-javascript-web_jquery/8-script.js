$(function () { 
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data, textStatus) {
			if (textStatus === 'success') {
				for (const key in data.results) {
					$('UL#list_movies').append('<li>'+ data.results[key].title + '</li>');
				}
			}
		});
});
