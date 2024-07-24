document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = document.getElementById('myForm');
    const formData = new FormData(form);

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect_url) {
            window.location.href = data.redirect_url;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});