# Simple Access Control Log API
---

## Tech Stack

* **Python** 3.12
* **Django** 5.x
* **SQLite** (default, no external DB required)
* **Docker** (containerized setup)
* **GNU Make** (developer convenience commands)

---

## Project Structure

```
access_control_project/
├── access_control/        
├── logs/                  
├── manage.py
├── requirements.txt
├── Dockerfile
├── Makefile
├── .dockerignore
├── README.md
```

---

## Prerequisites

Make sure the following are installed on your system:

* Python >= 3.10
* Docker >= 24
* Git
* Make (usually preinstalled on Linux/macOS)

---

## Option 1: Run Locally (Without Docker)

### 1. Clone the repository

```bash
git clone https://github.com/niloy104/access_control_project.git
cd access_control_project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## Option 2: Run with Docker (Recommended)

This is the preferred and most reliable way to run the project.

### 1. Build the Docker image

```bash
make docker-build
```

If you encounter network issues during build, run:

```bash
docker build --network=host -t access_control_app .
```

### 2. Run the container

```bash
make docker-run
```

The API will be available at:

```
http://localhost:8000/
```

Migrations are automatically applied when the container starts.

---

## Environment Notes

* The project uses **SQLite** for simplicity.
* No environment variables are required for basic usage.
* Debug mode is enabled by default for development purposes.

---

## Common Make Commands

```bash
make docker-build   # Build Docker image
make docker-run     # Run Docker container
```

---

## Author

**Md.Manzurul Alam (Niloy)**
Aspiring Software Engineer | Golang • Python | Problem Solver • R&D Enthusiast

