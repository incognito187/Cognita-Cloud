# Cognita-Cloud

🎉 Great! You want the **final full-featured Flask app** with:

✅ Email-based registration  
✅ Session timeout/logout on inactivity  
✅ Admin dashboard  
✅ PostgreSQL support  
✅ Bootstrap UI  
✅ Password hashing  
✅ Flash messages  
✅ Profile settings  
✅ Auto-generated folder structure  
✅ Downloadable ZIP  

You **don’t** want OAuth integration (Google/Facebook), so we’ll skip that.

---

## 📦 Final Project Structure

```
flask_auth_app/
│
├── app.py
├── requirements.txt
└── templates/
    ├── base.html
    ├── cloud_services.html
    ├── home.html
    ├── login.html
    ├── profile.html
    ├── register.html
    └── admin.html
```

I’ll now give you a **Python script** to auto-generate this project structure, and then I’ll provide the full downloadable ZIP-like content below.

---

## 🧪 Step 1: Python Script to Generate Folder Structure

Create a file called `generate_project.py`:

---

## 📦 How to Use It

1. Run the script:
   ```bash
   python generate_project.py
   ```

2. A folder named `flask_auth_app` will be created with all files.

3. Install dependencies:
   ```bash
   cd flask_auth_app
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   ```sql
   CREATE USER flaskuser WITH PASSWORD 'flaskpass';
   CREATE DATABASE flaskauthdb OWNER flaskuser;
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Access it at [http://localhost:5000](http://localhost:5000)

---

## ✅ Features Recap

| Feature | Status |
|--------|--------|
| Email-based Registration | ✅ Done |
| Session Timeout | ✅ Done |
| Admin Dashboard | ✅ Done |
| PostgreSQL Support | ✅ Done |
| Bootstrap UI | ✅ Done |
| Password Hashing | ✅ Done |
| Flash Messages | ✅ Done |
| Profile Settings | ✅ Done |

---

Would you like me to:
- Package this into a downloadable ZIP?
- Add REST API endpoints for mobile apps?
- Provide a Dockerfile for easy deployment?

Let me know how you'd like to proceed!

To log into PostgreSQL using the connection string:

```
postgresql://flaskuser:**********@localhost/flaskauthdb
```

you can use the `psql` command-line tool or a GUI tool. Below are **multiple ways** to connect using this URL-style connection string.

---

## ✅ Option 1: Use `psql` with a Connection String (Terminal)

PostgreSQL supports connecting via a full **libpq connection string**, which is what you've provided.

### 🔧 Command:

```bash
psql "postgresql://flaskuser:**********@localhost/flaskauthdb"
```

Just paste that into your terminal, and it will connect you directly to the database.

> ✅ This works in macOS, Linux, and modern Windows terminals with PostgreSQL installed.

---

## ✅ Option 2: Use Individual Flags with `psql`

If you prefer not to use the full URL format, you can break it down like this:

```bash
psql -h localhost -U flaskuser -d flaskauthdb
```

You’ll be prompted for the password (`**********`) unless you set up `.pgpass` (see below).

---

## ✅ Option 3: Set Up `.pgpass` File for Passwordless Login

To avoid entering the password every time in the terminal:

### 1. Create or edit the `.pgpass` file:

```bash
nano ~/.pgpass
```

### 2. Add this line:

```
localhost:5432:flaskauthdb:flaskuser:**********
```

### 3. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X` in nano)

### 4. Set correct permissions:

```bash
chmod 600 ~/.pgpass
```

Now you can connect without being prompted for a password:

```bash
psql -h localhost -U flaskuser -d flaskauthdb
```

---

## ✅ Option 4: Use a GUI Tool (e.g., Postico, DBeaver, TablePlus)

Most PostgreSQL GUIs allow you to paste the connection string or enter its components manually.

### Example (in Postico or TablePlus):

- **Host:** `localhost`
- **Port:** `5432`
- **User:** `flaskuser`
- **Password:** `**********`
- **Database:** `flaskauthdb`

Then click **Connect**.

---

## 🧪 Bonus: Test if the DB Exists

Once connected, try:

```sql
SELECT current_user;
SELECT current_database();
\dt
```

This confirms you're logged in correctly and shows any tables in the database.

---

## ❓ Troubleshooting Common Issues

| Problem | Solution |
|--------|----------|
| `FATAL: password authentication failed` | Check username/password or update `.pg_hba.conf` |
| `FATAL: database ... does not exist` | Create the DB first: `CREATE DATABASE flaskauthdb OWNER flaskuser;` |
| `could not connect to server` | Make sure PostgreSQL is running: `brew services start postgresql` |

flask run --port=8000
---


