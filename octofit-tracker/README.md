# OctoFit Tracker

## Overview

The OctoFit Tracker is a fitness application designed for Mergington High School, aimed at promoting physical activity among students. The application allows users to log their workouts, track their progress, and engage in friendly competitions with peers. It is built using a modern web stack, including Django for the backend and React for the frontend.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built with Django and includes the following components:

- **venv/**: Contains the Python virtual environment for isolating dependencies.
- **requirements.txt**: Lists the required Python packages for the backend.
- **octofit_tracker/**: The main Django application directory containing:
  - **__init__.py**: Marks the directory as a Python package.
  - **models.py**: Defines the data models for the application.
  - **serializers.py**: Contains serializers for converting data types.
  - **settings.py**: Configuration settings for the Django application.
  - **urls.py**: URL routing for the application.
  - **views.py**: View functions or classes that handle requests.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.
  - **asgi.py**: Entry point for ASGI-compatible web servers.

### Frontend

The frontend is built with React and includes:

- **public/**: Contains static files such as the HTML file and images.
- **src/**: Contains the source code for the React application, including components and styles.
- **package.json**: Lists the dependencies for the frontend application.
- **README.md**: Documentation specific to the frontend application.

## Setup Instructions

To set up the OctoFit Tracker application, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Set up the backend**:
   - Navigate to the backend directory:
     ```
     cd backend
     ```
   - Create a virtual environment:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```
     - On Windows:
       ```
       venv\Scripts\activate
       ```
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```

3. **Run the backend server**:
   ```
   python manage.py runserver
   ```

4. **Set up the frontend**:
   - Navigate to the frontend directory:
     ```
     cd ../frontend
     ```
   - Install the frontend dependencies:
     ```
     npm install
     ```

5. **Run the frontend application**:
   ```
   npm start
   ```

## Features

- User profiles for tracking individual progress.
- Activity logging for various workouts.
- Team creation and management for competitions.
- A competitive leaderboard to encourage engagement.
- Personalized workout suggestions based on user activity.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.