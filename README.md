# Project Title:Nginx Web Application

## Description
This project is a simple web application that demonstrates the use of HTML, CSS, and JavaScript. It is containerized using Docker, allowing for easy deployment and management.

## Project Structure
```
web-app
├── src
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd web-app
   ```

2. **Build the Docker Image**
   ```
   docker-compose build
   ```

3. **Run the Application**
   ```
   docker-compose up
   ```

4. **Access the Application**
   Open your web browser and navigate to `http://localhost:8080` to view the application.

## Usage
- The application serves a simple webpage that includes interactive elements powered by JavaScript.
- Modify the `src/styles.css` file to change the appearance of the webpage.
- Update the `src/app.js` file to add or modify functionality.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.