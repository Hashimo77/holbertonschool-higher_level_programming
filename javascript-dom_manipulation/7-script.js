const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(function (response) {
    // Parse the response as JSON
    return response.json();
  })
  .then(function (data) {
    // Select the UL element with id 'list_movies'
    const listMovies = document.querySelector('#list_movies');

    // Iterate through the results array provided by the API
    data.results.forEach(function (movie) {
      // Create a new list item for each movie
      const listItem = document.createElement('li');
      // Set the text of the list item to the movie title
      listItem.textContent = movie.title;
      // Append the list item to the UL
      listMovies.appendChild(listItem);
    });
  });