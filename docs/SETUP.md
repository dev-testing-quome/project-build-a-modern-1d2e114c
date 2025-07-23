# Developer Setup Guide - project-build-a-modern

## Prerequisites

This guide assumes basic familiarity with command-line interfaces, Git, and at least one programming language (preferably Python and JavaScript).

**Required Software Versions:**

* **Docker:** 20.10.0+ (Recommended for Option 1)
* **Docker Compose:** 1.29.0+ (Recommended for Option 1)
* **Node.js:** 16+ (Required for both options)
* **npm (or yarn):** Latest version (Required for both options)
* **Python:** 3.9+ (Required for Option 2)
* **PostgreSQL:** 14+ (Recommended, adjust if using a different database)


**Development Tools:**

* **Git:** For version control.
* **Text Editor/IDE:** VS Code, Sublime Text, Atom, or PyCharm (see IDE recommendations below).


**IDE Recommendations and Configurations:**

* **VS Code:** Highly recommended for both frontend and backend development.  Install the following extensions:
    * Python extension (for Python development)
    * Prettier (for code formatting)
    * ESLint (for linting JavaScript)
    * Docker extension (for easier Docker management)
* **PyCharm (Professional):** Excellent for Python backend development, but may require a license.
* **WebStorm:** Good for frontend development with JavaScript.


## Local Development Setup

### Option 1: Docker Development (Recommended)

This option simplifies setup by containerizing the entire application.

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-build-a-modern
   ```

2. **Docker Setup:** Ensure Docker and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  (Example - adapt to your actual `docker-compose.yml`)

   ```yaml
   version: "3.9"
   services:
     web:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - api
     api:
       build: ./backend
       ports:
         - "8000:8000"
       environment:
         - DATABASE_URL=postgres://user:password@db:5432/database_name
         - STRIPE_SECRET_KEY=your_stripe_secret_key  # Replace with your key
         # ... other environment variables
     db:
       image: postgres:14
       ports:
         - "5432:5432"
       environment:
         - POSTGRES_USER=user
         - POSTGRES_PASSWORD=password
         - POSTGRES_DB=database_name
   ```

4. **Hot Reload Setup:**  The `docker-compose.yml` file should be configured to use a development server with hot reloading capabilities (e.g., using `nodemon` for the backend and a similar tool for the frontend).  This will automatically restart the application when you make code changes.


### Option 2: Native Development

This option requires installing dependencies directly on your system.

1. **Backend Setup:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt 
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:** Install PostgreSQL and create a database.  Configure the database connection details in your application's configuration files.  (Example using `psql`):

   ```bash
   psql -U postgres -c "CREATE DATABASE database_name;"
   psql -U postgres -d database_name -c "CREATE USER user WITH PASSWORD 'password';"
   psql -U user -d database_name -f schema.sql  # Assuming you have a schema file
   ```


## Environment Configuration

**Required Environment Variables:**

* `DATABASE_URL`:  Database connection string (e.g., `postgres://user:password@localhost:5432/database_name`).
* `STRIPE_SECRET_KEY`: Your Stripe secret key for payment processing.
* `SECRET_KEY`: A secret key for your application's security (generate a strong random key).
* `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`:  Settings for your email provider (e.g., SendGrid, Mailgun).  (Optional, but recommended for order updates)
* `FRONTEND_URL`: URL of your frontend application (for redirecting after login/checkout).


**Local Development `.env` File Setup:** Create a `.env` file in the root directory of your project and add your environment variables:

```
DATABASE_URL=postgres://user:password@localhost:5432/database_name
STRIPE_SECRET_KEY=your_stripe_secret_key
SECRET_KEY=your_secret_key
EMAIL_HOST=your_email_host
EMAIL_PORT=your_email_port
EMAIL_HOST_USER=your_email_user
EMAIL_HOST_PASSWORD=your_email_password
FRONTEND_URL=http://localhost:3000
```

**Configuration for Different Environments:** Use environment variables to manage configurations for development, staging, and production.  Consider using a tool like `python-dotenv` for loading environment variables in your backend.


## Running the Application

**Start Commands for Development:**

* **Docker:** `docker-compose up -d --build`
* **Native:**  Start the backend server (e.g., `python manage.py runserver` if using Django) and the frontend development server (e.g., `npm start` or `yarn start`).


**How to Access Frontend and Backend:**

* **Frontend:** Access the frontend application at `http://localhost:3000` (or the port specified in your `docker-compose.yml` or `package.json`).
* **Backend:** Access the backend API at `http://localhost:8000` (or the port specified).  You might need to use tools like Postman or curl to test the API endpoints directly.


**API Documentation Access:**  Ideally, generate API documentation using tools like Swagger or OpenAPI.


## Development Workflow

**Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., `main` branch for production, feature branches for new features, pull requests for code review).


**Code Formatting and Linting Setup:** Use Prettier (for frontend) and a linter like Pylint (for backend) to enforce consistent code style.  Configure your IDE to automatically format code on save.


**Testing Procedures:**  Write unit tests for individual components and integration tests for interactions between components.  Use a testing framework like pytest (for backend) and Jest (for frontend).


**Debugging Setup:** Use your IDE's debugger or tools like `pdb` (Python debugger) or the browser's developer tools for debugging.


## Database Management

**Running Migrations:** Use database migration tools (e.g., Alembic for SQLAlchemy in Python) to manage database schema changes.


**Seeding Development Data:** Create scripts to populate the database with sample data for development purposes.


**Database Reset Procedures:**  Include scripts to easily reset the database to a clean state.


## Testing

**Running Unit Tests:**  `pytest` (backend), `jest` (frontend)

**Running Integration Tests:**  Use a testing framework that supports integration testing (e.g., pytest with fixtures).

**Test Coverage Reports:** Generate test coverage reports using tools like `pytest-cov` to track test completeness.


## Common Development Tasks

**Adding New API Endpoints:**  Follow the existing API design and implement new endpoints with proper validation and error handling.

**Adding New Frontend Components:** Create new React components (or components in your chosen framework) and integrate them into the existing application.

**Database Schema Changes:** Use migrations to manage schema changes safely.

**Adding Dependencies:** Use `pip` (backend) and `npm` (frontend) to add new dependencies, ensuring version compatibility.


## Troubleshooting

**Common Setup Issues:**  Check Docker and database configurations, ensure ports are not already in use, and verify environment variables.

**Port Conflicts Resolution:**  Change ports in your configuration files if there are conflicts.

**Dependency Issues:**  Resolve dependency conflicts using tools like `pip-tools` (backend) or `npm-check-updates` (frontend).

**Environment Variable Problems:** Double-check that environment variables are set correctly and that your application is loading them properly.


## Contributing

**Code Style Guidelines:**  Follow a consistent code style (e.g., PEP 8 for Python, Airbnb style guide for JavaScript).

**Pull Request Process:** Create feature branches, write clear commit messages, and submit pull requests for code review.

**Issue Reporting:**  Use the project's issue tracker to report bugs and suggest features.  Provide clear descriptions and steps to reproduce issues.


This guide provides a foundation for developers working on `project-build-a-modern`. Remember to adapt these instructions to your specific project structure and technologies.  Always consult the documentation for your chosen frameworks and libraries for more detailed information.
