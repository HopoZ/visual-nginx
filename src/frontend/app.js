// filepath: /web-app/web-app/src/app.js
document.addEventListener('DOMContentLoaded', () => {
    const appElement = document.getElementById('app');
    appElement.innerHTML = '<h1>Welcome to the Web Application</h1>';
    
    const button = document.createElement('button');
    button.textContent = 'Click Me';
    button.addEventListener('click', () => {
        alert('Button was clicked!');
    });
    
    appElement.appendChild(button);
});