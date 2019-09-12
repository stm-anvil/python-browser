def greet():
    alert("Hello " + document.getElementById("name-box").value + "!")

document.getElementById("greet-button").addEventListener('click', greet)
