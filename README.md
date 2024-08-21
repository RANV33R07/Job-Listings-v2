# Job Listing Website

This project is a Flask-based web application that serves as a platform for job listings and applications. It provides a user-friendly interface for both job seekers and employers.

## Features

* **Job Listings:**
    * Display job listings from a PostgreSQL database.
    * Allow users to search, filter, and sort job listings based on various criteria (location, keywords, salary, etc.).
    * Provide detailed job descriptions with responsibilities, requirements, and company information.
* **Application Submission:**
    * Enable users to create accounts and apply for jobs with a streamlined application process.
    * Collect user information (name, email, LinkedIn, education, experience, resume).
    * Track application status and provide feedback to candidates.
* **User Interface:**
    * Designed a user-friendly interface using HTML and CSS, ensuring a smooth and intuitive user experience for both job seekers and employers.
    * Implemented a responsive design to ensure optimal viewing across different devices.

## Technologies Used

* **Python:**  Used as the primary programming language for backend development.
* **Flask:**  A lightweight web framework for building the application.
* **HTML:**  Used for structuring the web pages.
* **CSS:**  Used for styling the web pages.
* **PostgreSQL:**  A relational database system for storing job listings and user data.

## Getting Started

1. **Prerequisites:**
    * Python 3.x installed
    * Flask installed (`pip install Flask`)
    * PostgreSQL installed and configured

2. **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```

3. **Set up Database:**
    * Create a PostgreSQL database and a user.
    * Update the database connection details in the `database.py` file.

4. **Run the Application:**
    ```bash
    python app.py
    ```

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
