document.getElementById('add_item').addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
});

// document.getElementById("add_item").onclick = addList;
// function addList(){
//   const newElement = document.createElement("li");
//   const textItem = document.createTextNode("Item");
//   newElement.appendChild(textItem);
//   document.querySelector(".my_list").appendChild(newElement);
// }
