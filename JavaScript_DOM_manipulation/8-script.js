document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hello').textContent = data.hello;
        })
        .catch(error => console.error('Error:', error));
});

// const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// document.addEventListener('DOMContentLoaded', () => {
//   fetch(url)
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then((data) => {
//       const helloElement = document.getElementById('hello');
//       helloElement.textContent = data.hello;
//     })
//     .catch((error) => {
//       console.error('Error fetching hello:', error);
//     });
// });
