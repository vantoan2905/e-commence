# Django Project README

## Project Overview
This project is a Django-based application designed for managing and recommending products on an e-commerce website. It includes functionality for storing and processing search and product selection history, managing media files, and utilizing a recommendation model.

## Directory Structure
```
(django_recommend_system) D:\recommend_product\recommend_product\shop>
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── __init__.py
├── media
│   ├── tag
│   └── image
├── migrations
├── recommend_model
├── static
├── templates
└── __pycache__
```

### Key Directories and Files
- **`media/tag`**: Contains JSON files with information about images.
- **`media/image`**: Contains image files.
- **`recommend_model`**: Includes the recommendation model implementation.
- **`static`**: Holds static assets such as CSS, JavaScript, and images.
- **`templates`**: Contains HTML templates for rendering views.
- **`migrations`**: Stores migration files for database schema changes.

## Prerequisites
- Python 3.x
- Django (latest compatible version)
- SQLite (or another configured database backend)
- Required Python packages (listed in `requirements.txt`)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd recommend_product
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**
   ```bash
   python manage.py makemigrations shop
   python manage.py migrate
   ```

4. **Load Initial Data**
   Ensure the `load_data` command is implemented under `shop/management/commands/load_data.py`.
   ```bash
   python manage.py load_data
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Media Management
- **Tag Files**: JSON files in the `media/tag` directory store metadata for corresponding images in the `media/image` directory.
- Ensure proper permissions for reading and writing to the `media` directory.

## Custom Commands
### `load_data`
Loads initial data into the database. Implemented as a custom management command under `shop/management/commands`.

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch.
   ```bash
   git checkout -b feature/<feature-name>
   ```
3. Commit your changes and push to your fork.
   ```bash
   git commit -m "Add <feature-description>"
   git push origin feature/<feature-name>
   ```
4. Open a pull request for review.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For inquiries or support, contact Nguyen Van Toan at [toanvippk115@gmail.com].

