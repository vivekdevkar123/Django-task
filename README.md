
# Task Management App with Google Authentication

This project is a simple **Task Management Web Application** built using **Django**. It enables users to manage personal tasks after logging in with their Google accounts via **OAuth 2.0**. The application also provides an admin interface to manage invitations and send registration links via email.

---

## Features

### User Authentication
- Login using Google OAuth 2.0 via **Django Allauth**.
- Secure and seamless authentication.

### Task Management
- **Create Tasks**: Add tasks with a title and description.
- **View Tasks**: Display all tasks with a clean UI.
- **Edit Tasks**: Update task details.
- **Delete Tasks**: Remove tasks no longer needed.

### Admin Panel Features
- **Invitation Management**:
  - Add invitations and manage them.
  - Send registration links via email.

### Responsive Design
- Fully responsive using **Bootstrap** for styling.

---

## Tech Stack

**Backend**: Django, Django Allauth  
**Frontend**: HTML, CSS, Bootstrap  
**Database**: SQLite (default) – can be replaced with PostgreSQL or other databases.

---

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scriptsctivate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory with the following:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password

# Google OAuth
SOCIAL_AUTH_GOOGLE_CLIENT_ID=your_google_client_id
SOCIAL_AUTH_GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### Step 5: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 7: Run the Server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the application.

---

## Admin Panel

### Create a Superuser
```bash
python manage.py createsuperuser
```

### Access the Admin Panel
Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in using the superuser credentials.

### Manage Invitations
1. Go to the **Invitations** section.
2. Add a new invitation with an email address.
3. Use the "Send Invitation" button to send the registration link.

---

## Folder Structure

```plaintext
project/
├── mainapp/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── mainapp/
│   │   │   ├── index.html
│   │   │   ├── task_form.html
│   │   │   ├── register.html
│   │   │   └── task_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project_name/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .env
```

---

## Key Files

### `models.py`
Defines the models:
- **Task**: Represents tasks with fields for `title`, `description`, and a foreign key to the user.
- **Invitation**: Stores invitation data, including `email` and `token`.

### `views.py`
Implements the following:
- `home`: Displays the task list.
- `create_task`: Handles task creation.
- `edit_task`: Updates task details.
- `delete_task`: Deletes tasks.
- `register_with_token`: Registers a user with an invitation token.

### `urls.py`
Defines routes for:
- Task management.
- Registration with an invitation token.
- Admin-specific actions.

---

## How to Use

### User Workflow
1. Log in using your Google account.
2. View, create, edit, or delete tasks on the task dashboard.

### Admin Workflow
1. Access the admin panel at `/admin`.
2. Manage invitations and send registration links.

---

## Customizations

### Change Database
Modify the `DATABASES` setting in `settings.py` to use a different database like PostgreSQL, MySQL, etc.

### Deploy to Production
1. Set `DEBUG = False` in `settings.py`.
2. Deploy to a hosting platform like **Heroku**, **AWS**, or **DigitalOcean**.
3. Configure environment variables securely using the platform's tools.

---

## Known Issues

1. **Invitation Link 404 Error**  
   Ensure the `register/<token>/` route is defined and working as expected.

2. **Email Sending Failure**  
   - Verify SMTP credentials in `.env`.
   - Ensure the email service supports less secure apps or use an app password if using Gmail.

---

## Future Enhancements

1. **Task Deadlines**: Add due dates and notifications.
2. **Collaborative Features**: Enable task sharing with other users.
3. **API Integration**: Build a REST API using **Django REST Framework** for task management.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
