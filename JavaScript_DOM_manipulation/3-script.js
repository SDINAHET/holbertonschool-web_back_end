document.getElementById('toggle_header').addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
    } else {
        header.classList.replace('green', 'red');
    }
});

// document.getElementById("toggle_header").onclick = colorToggle;
// function colorToggle() {
//   document.querySelector("header").classList.toggle("green");
//   document.querySelector("header").classList.toggle("red");

// }
