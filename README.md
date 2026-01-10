# 📊 Django Expense Tracker

A streamlined and efficient **Personal Finance Management** application built with the Django framework. This project focuses on providing a clean user experience for tracking daily expenses while demonstrating core web development principles like CRUD operations and user authentication.

---

## 🔍 About the Project

**Django Expense Tracker** is designed for users who want a distraction-free way to log their spending. Instead of complex financial tools, this app provides a minimalist interface to answer three basic questions: **How much did I spend? When? and On what?**

The project serves as a robust foundation for anyone looking to understand how Django handles relational data and user-specific content.

---

## ✨ Features

### 🔐 Secure User Authentication
- **Personalized Data:** Each user has their own private workspace. You can only see and manage the expenses you have created.
- **Identity Management:** Built-in Sign-up and Login systems utilizing Django's secure `User` model and session management.

### 💰 Expense Management (CRUD)
- **Create:** Quickly log new expenses by entering the amount, date, description, and category.
- **Read:** View all your past transactions in a clean, chronological list.
- **Update:** Easily edit the details of an existing entry if you made a mistake.
- **Delete:** Remove unwanted or duplicate records with a single click.

### 📂 Categorization
- Organize your spending into predefined categories (e.g., Food, Transport, Rent, Entertainment) to keep your financial data structured.

---

## 🛠 Tech Stack

- **Backend:** Python & Django (MVT Architecture)
- **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive Design)
- **Database:** SQLite3 (Default development database)
- **Styling:** Modern and readable UI components powered by Bootstrap.

---

## ⚙️ Installation & Local Setup

Follow these steps to get the project running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/celiikerenn/django-expense-tracker.git](https://github.com/celiikerenn/django-expense-tracker.git)
    cd django-expense-tracker
    ```

2.  **Set Up Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000` in your web browser.

---

## 📁 Project Structure

- `config/`: Main project settings and URL configurations.
- `tracker/`: The core application folder containing models, views, and business logic.
- `templates/`: HTML user interface files.
- `static/`: Custom CSS styles and assets.

---

## 🚀 Future Roadmap

I plan to enhance the application with the following features:
- [ ] **Data Visualization:** Interactive charts to show spending distribution by category.
- [ ] **Advanced Filtering:** The ability to filter expenses by date range or specific categories.
- [ ] **Budgeting:** Monthly limit settings with automated alerts when nearing the limit.
- [ ] **Export Options:** Download expense reports in PDF or Excel format.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contact
**Eren Çelik** - [My GitHub Profile](https://github.com/celiikerenn)
