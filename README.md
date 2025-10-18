# Smart Health Check – CI/CD Demo

[![CI/CD](https://github.com/Parthiv19M/Smart-health-check-CI-CD/actions/workflows/ci.yml/badge.svg)](https://github.com/Parthiv19M/Smart-health-check-CI-CD/actions)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern Python Flask application demonstrating industry-standard CI/CD practices with GitHub Actions, automated testing, and deployment.

## 🚀 Key Features

- **Automated Testing**: Robust test suite with Pytest and Coverage
- **Code Quality**: Pre-commit hooks for consistent code style
- **Security**: Automated vulnerability scanning with Bandit and Safety
- **CI/CD**: GitHub Actions workflow with automated testing and deployment
- **Containerization**: Ready for Docker deployment
- **API Documentation**: Well-documented endpoints with docstrings

## 📦 Prerequisites

- Python 3.9+
- Git
- pip (Python package manager)
- (Optional) Docker for containerization

## 🛠️ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Parthiv19M/Smart-health-check-CI-CD.git
   cd Smart-health-check-CI-CD
   ```

2. **Set up a virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   # python -m venv venv
   # venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Run the application locally**
   ```bash
   python app.py
   ```
   Visit http://localhost:5001 in your browser

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=.

# Generate HTML coverage report
coverage html
# Open htmlcov/index.html in your browser
```

## 🛠 Development Setup

### Pre-commit Hooks
This project uses pre-commit hooks to ensure code quality. They will run automatically before each commit.

```bash
# Install pre-commit hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

## 🌐 API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint

## 🚀 Deployment

The application is configured for deployment to Heroku. The CI/CD pipeline will automatically deploy the application when changes are pushed to the `main` branch.

### Required Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

[Parthiv](https://github.com/Parthiv19M)

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=.

# Generate HTML coverage report
coverage html
```

## 🏗️ CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) includes:

1. **Test Job** (runs on every push and PR):
   - Python 3.9 setup
   - Dependency installation
   - Code formatting with Black
   - Linting with Flake8
   - Import sorting with isort
   - Security checks with Bandit
   - Dependency vulnerability scanning with Safety
   - Static type checking with mypy
   - Documentation checks with pydocstyle
   - Test execution with Pytest and coverage
   - Application health check

2. **Deploy Job** (runs on push to main after tests pass):
   - Automated deployment to Heroku
   - Container-based deployment for consistency

## 🔒 Environment Variables

For local development, create a `.env` file:

```env
FLASK_APP=app.py
FLASK_ENV=development
```

## 🚀 Deployment

The application is automatically deployed to Heroku when changes are pushed to the main branch. The deployment requires the following secrets to be set in GitHub:

- `HEROKU_API_KEY`: Your Heroku API key
- `HEROKU_APP_NAME`: Your Heroku application name

## 📝 API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

[Parthiv](https://github.com/Parthiv19M)
