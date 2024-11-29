fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('list_movies');
        data.results.forEach(movie => {
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            list.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));


// const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// fetch(url)
//     .then((response) => {
//     if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//     }
//     return response.json();
//     })
//     .then((data) => {
//     const movies = data.results;
//     const listMoviesElement = document.getElementById('list_movies');

//     movies.forEach((movie) => {
//         const listItem = document.createElement('li');
//         listItem.textContent = movie.title;
//         listMoviesElement.appendChild(listItem);
//     });
//     })
//     .catch((error) => {
//     console.error('Error fetching movies:', error);
//     });


// const request = new Request("https://swapi-api.hbtn.io/api/films/?format=json");
// fetch(request)
//   .then((response) => {
//     if (response.status === 200){
//       return response.json();
//     } else {
//       throw new Error("Something went wrong on API server!")
//     }
//   })
//   .then((data) => {
//     const movieTitles = data.results;
//     const movieList = document.getElementById("list_movies");

//     movieTitles.forEach(element => {
//       const newElement = document.createElement("li");
//       newElement.textContent = element.title;
//       movieList.appendChild(newElement);
//     });
//   })
//   .catch(error => {
//     console.error('Erreur:', error);
//   })
