document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/latest/')
        .then(response => response.json())
        .then(data => {
            const ul = document.getElementById('latest-list');
            ul.innerHTML = ''; // Clear existing items

            data.forEach(user => {
                const li = document.createElement('li');

                // Create an img element for profile picture
                const img = document.createElement('img');
                img.src = user.profile_pic; // or add domain if needed
                img.alt = user.username + "'s profile picture";
                img.style.width = '50px'; // optional styling
                img.style.height = '50px';
                img.style.borderRadius = '50%';
                img.style.marginRight = '10px';

                // Create a span for username
                const span = document.createElement('span');
                span.textContent = user.username;

                // Append img and username to li
                li.appendChild(img);
                li.appendChild(span);

                // Append li to ul
                ul.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
