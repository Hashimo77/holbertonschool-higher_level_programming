// Select the element with the id 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener
toggleHeader.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Check the current class and toggle between 'red' and 'green'
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});