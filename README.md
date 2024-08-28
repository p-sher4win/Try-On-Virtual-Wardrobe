
# Try On (Virtual Wardrobe)

An e-commerce platform for purchasing clothes, featuring a real-time virtual try-on functionality.

### Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

### Overview

This project is a web-based application that allows users to try on clothes virtually in real-time using VR technology. The frontend is developed using HTML, CSS, and JavaScript, while the backend services are powered by Python. The application connects to a database to store user information.

### Features

- Virtual Try-On: Users can select clothing items and try them on virtually in real-time using VR technology.
- User Authentication: Secure login and registration system for users.
- Product Catalog: Browse and search through a variety of clothing items.
- Responsive Design: The website is fully responsive and works on all devices.
- Database Connectivity: The backend connects to a database to manage users.

### Technologies

#### Frontend
- HTML5: Structure of the web pages.
- CSS3: Styling of the web pages for a clean and modern look.
- JavaScript: Dynamic and interactive features, including form validation, event handling, and VR integration.

#### Backend
- Python: Backend logic, including user authentication, handling requests, and VR data processing.
- Flask: Web framework used to create the API endpoints and manage the server-side logic.
- Database: MongoDB for storing user data.
### Setup and Installation

#### Prerequisites
- Python 3.x
- Virtual Environment (recommended)
- MongoDB
- Postman API

#### Installation Steps
1. Clone the Repository:
```bash
git clone https://github.com/p-sher4win/Try-On-Virtual-Wardrobe.git
```

2. Navigate to the project directory:
```bash
cd Try-On-Virtual-Wardrobe
```

3. Install Backend Dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Database:
- Set up your database and update the database connection settings in the app.py file.

5. Run the Backend Server:
```bash
python app.py
```

6. Access the Application:
- Open your web browser and go to http://127.0.0.1:8085 (or the appropriate URL depending on your setup).

### Usage

1. Login/Signup: Users can create an account or log in to their existing account.

2. Browse Catalog: Browse through the clothing catalog and select items to try on.

3. Virtual Try-On: Use the VR feature to see how selected clothes look in real-time.

4. Purchase: Buy items and proceed to checkout.

### Contributing

While contributions to this repository are not accepted, you are welcome to fork the repository and make modifications in your own fork. If you have suggestions or feedback, feel free to open an issue or contact [sher4winpereira@gmail.com]. Thank you for your understanding!

### License

This project is currently not licensed. All rights reserved. You are not permitted to modify this code without explicit permission from the author.
