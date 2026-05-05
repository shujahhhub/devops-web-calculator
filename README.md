# 🚀 DevOps Web Calculator

A containerized, web-based calculator microservice built to demonstrate core DevOps principles, including Continuous Integration/Continuous Deployment (CI/CD) and Docker containerization.

## 🛠️ Tech Stack
* **Application Code:** Python 3.12, Flask 3.0.3
* **Testing Framework:** Pytest 8.2.2
* **Containerization:** Docker
* **CI/CD Pipeline:** GitHub Actions

## 🏗️ Architecture & Pipeline
This project utilizes a fully automated CI/CD pipeline defined in `.github/workflows/ci-pipeline.yml`. 
Every push to the `main` branch triggers the following automated workflow:
1. **Code Checkout:** GitHub Actions provisions an Ubuntu runner and fetches the latest code.
2. **Environment Setup:** Initializes Python 3.12 and installs dependencies from `requirements.txt`.
3. **Automated QA Testing:** Executes `pytest test_app.py` to ensure core mathematical logic and web routing function correctly.
4. **Container Build:** If all tests pass, the pipeline builds a fresh Docker image from the `Dockerfile`.

🧑‍💻 How to Run Locally (Without Docker)
If you want to run the raw Python code directly:

Bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 app.py
