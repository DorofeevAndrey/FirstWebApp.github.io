document.addEventListener('DOMContentLoaded', function () {
    const isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (isDarkMode) {
        document.body.style.backgroundImage = 'url("dark_background.jpg")';
    } else {
        document.body.style.backgroundImage = 'url("light_background.jpg")';
    }
});
