// Function to determine if the background is dark or light
function isBackgroundDark(imageUrl, callback) {
    const img = new Image();
    img.src = imageUrl;
    img.crossOrigin = "Anonymous"; // Allow cross-origin images
    img.onload = function () {
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);

        // Get the average color of the image
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
        let brightness = 0;
        for (let i = 0; i < imageData.length; i += 4) {
            brightness += (imageData[i] + imageData[i + 1] + imageData[i + 2]) / 3;
        }
        brightness /= (imageData.length / 4);

        // If brightness is less than 128, the background is dark
        callback(brightness < 128);
    };
}

// Set the welcome text color based on the background
isBackgroundDark('background-image.jpg', function (isDark) {
    const welcomeText = document.querySelector('.welcome-message h1');
    if (isDark) {
        welcomeText.style.color = '#ffffff'; // White for dark backgrounds
    } else {
        welcomeText.style.color = '#000000'; // Black for light backgrounds
    }
});

// Dynamically set the college name, team name, and project link
document.getElementById('collegeName').innerText = "PRPCEM (AIDS)";
document.getElementById('teamName').innerText = "CodeMasters";
document.getElementById('projectLink').innerText = "View Our Project";
document.getElementById('projectLink').href = "chess.html ";