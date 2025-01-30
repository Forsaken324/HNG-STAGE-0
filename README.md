# HNG12 Stage 0 - Public API to Retrieve Basic Information

## Project Description
This is a simple public API developed using Python and Django REST Framework (DRF) for HNG12 Stage 0. The API returns basic information in JSON format, including:
- Your registered email address.
- The current datetime in ISO 8601 format (UTC).
- The GitHub repository URL for this project.

The API is publicly accessible and follows best practices, including CORS handling and structured documentation.

---

## Technologies Used
- **Programming Language:** Python
- **Framework:** Django REST Framework (DRF)
- **Database:** Not required for this project
- **Deployment:** [Specify your hosting provider, e.g., Render, Railway, Vercel, or AWS]
- **Version Control:** GitHub

---

## How to Set Up the Project Locally

### Prerequisites
Ensure you have the following installed:
- Python (≥3.8)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Installation Steps
1. **Clone the Repository**  
   ```sh
   https://github.com/Forsaken324/HNG-STAGE-0.git
   cd your-repo
   ```

2. **Create and Activate Virtual Environment**  
   ```sh
   python -m venv env  
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations (If Needed)**  
   ```sh
   python manage.py migrate
   ```

5. **Run the Server**  
   ```sh
   python manage.py runserver
   ```

The API should now be accessible at `http://127.0.0.1:8000/`.

---

## API Documentation

### Endpoint
- **URL:** `GET /`
- **Response Format:** JSON  

### Response Example (200 OK)
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

---

## Deployment
This API is deployed and publicly accessible at:  
➡️ **[https://your-deployment-url.com](https://your-deployment-url.com)**  

### Deployment Steps:
1. Choose a hosting provider (e.g., Render, Railway, Vercel, or AWS).
2. Configure environment variables (if necessary).
3. Deploy the project using GitHub integration or manually push to the server.

---

## CORS Handling
To ensure Cross-Origin Resource Sharing (CORS) is handled correctly:
- Install Django CORS Headers:
  ```sh
  pip install django-cors-headers
  ```
- Add `'corsheaders'` to `INSTALLED_APPS` in `settings.py`.
- Add the following middleware:
  ```python
  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
      # Other middlewares...
  ]
  ```
- Allow all origins or specify allowed domains:
  ```python
  CORS_ALLOW_ALL_ORIGINS = True
  ```

---

## Contributing
If you'd like to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make changes and commit: `git commit -m "Added a new feature"`
4. Push to your branch: `git push origin feature-branch`
5. Open a pull request.

---

## Useful Links
- Official Python Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
- Django REST Framework Docs: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- **HNG12 Backend Hiring Link (Python Developers)**  
  [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

## License
This project is open-source and available under the MIT License.
