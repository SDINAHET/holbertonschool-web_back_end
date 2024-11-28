fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('character').textContent = data.name;
    })
    .catch(error => console.error('Error:', error));

// const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// fetch(url)
//     .then((response) => {
//     if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//     }
//     return response.json();
//     })
//     .then((data) => {
//     const characterElement = document.getElementById('character');
//     characterElement.textContent = data.name;
//     })
//     .catch((error) => {
//     console.error('Error fetching character:', error);
//     });

