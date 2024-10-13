function generate() {
    const inputWord = document.getElementById('inputWord').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: inputWord })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.output;
    })
    .catch(error => console.error('Error:', error));
}
