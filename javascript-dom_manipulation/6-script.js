const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(function (response) {
    // Check if the response is successful
    return response.json();
  })
  .then(function (data) {
    // Select the element with id 'character'
    const characterDiv = document.querySelector('#character');
    // Update the text content with the character's name
    characterDiv.textContent = data.name;
  });