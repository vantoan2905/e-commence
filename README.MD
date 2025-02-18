

# Author
```
    Code by: Nguyen Van Toan
             Duc Thanh
    GitHub: https://github.com/vantoan2905
            https://github.com/duc-thanh-2303
    Email: toanvippk115@gmail.com
           tika303103@gmail.com
```

# Django Project README
![Image](image.png)

## Project Overview
**Task:**
- Build an e-commerce website.
- Design and develop the back-end and front-end of an e-commerce website using Django.
- Simulate customer data such as search history, clicks, ratings, and time spent on product pages.
- Pre-process product and user data.
- Develop a model for task classification (image, text) using TensorFlow (MobileNetV2), and deploy the model for an image-based product search function. 
- Apply Large Language Models (LLM) to develop a chatbot system. (update)

## Directory Structure
```
(django_e-commence_system) /e-commence/
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
├── static
│   ├── models
│   └── shop
├── templates
└── 
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
   git clone https://github.com/vantoan2905/e-commence.git
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
   python manage.py render_User
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
For inquiries or support, contact Backend Nguyen Van Toan at [toanvippk115@gmail.com].

For inquiries or support, contact Fontend Duc Thanh at [tika303103@gmail.com].

