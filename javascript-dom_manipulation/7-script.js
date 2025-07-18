fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li')       // 1. Create <li>
      li.textContent = movie.title                   // 2. Set the movie title
      document.querySelector('#list_movies').appendChild(li)  // 3. Add to the list    
    });
  })