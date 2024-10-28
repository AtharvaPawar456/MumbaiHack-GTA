from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'trailers.db'

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Database Initialization
def init_db():
    with app.app_context():
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create tables if they do not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS UserData (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            preference TEXT,
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS TrailerData (
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            moviename TEXT NOT NULL,
            genre TEXT,
            description TEXT,
            actors TEXT,
            thumbnail TEXT,
            path TEXT,
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS ActionData (
            aid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            clickedon INTEGER NOT NULL,
            FOREIGN KEY (clickedon) REFERENCES TrailerData(tid) ON DELETE CASCADE
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS GenTrailerData (
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            moviename TEXT NOT NULL,
            prompt TEXT,
            preference TEXT,
            path TEXT,
            thumbnail TEXT,
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        conn.commit()
        conn.close()

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"404 Error: {e}")
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f"500 Error: {e}")
    return render_template("500.html"), 500

# Routes
@app.route("/")
def welcome():
    try:
        return render_template("welcome.html")
    except Exception as e:
        app.logger.error(f"Error | Rendering Welcome Page: {e}")
        flash("An error occurred while loading the welcome page.", "danger")
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM UserData WHERE username = ?', (username,)).fetchone()
            conn.close()

            if user and user['password'] == password:
                session["user_id"] = user['uid']
                session["username"] = user['username']
                session["preference"] = user['preference']
                return redirect(url_for("home"))

            flash("Invalid login credentials", "danger")
        return render_template("login.html")
    except Exception as e:
        app.logger.error(f"Error | Login Attempt: {e}")
        flash("An error occurred during login.", "danger")
        return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            preference = request.form.get("preference")
            conn = get_db_connection()
            try:
                conn.execute('INSERT INTO UserData (username, password, preference) VALUES (?, ?, ?)', (username, password, preference))
                conn.commit()
                flash("Registration successful", "success")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                flash("Username already exists", "danger")
            finally:
                conn.close()
        return render_template("register.html")
    except Exception as e:
        app.logger.error(f"Error | Registration: {e}")
        flash("An error occurred during registration.", "danger")
        return redirect(url_for("register"))

@app.route("/logout")
def logout():
    """Log out the user and clear session data."""
    try:
        session.clear()
        flash("You have been logged out.", "info")
        return redirect(url_for("login"))
    except Exception as e:
        app.logger.error(f"Error | Logout Attempt: {e}")
        flash("An error occurred during logout.", "danger")
        return redirect(url_for("home"))

@app.route("/home")
def home():
    try:
        if "user_id" not in session:
            return redirect(url_for("login"))
        
        username = session.get("username")
        preference = session.get("preference")

        conn = get_db_connection()
        # trailers = conn.execute('SELECT * FROM TrailerData WHERE genre LIKE ?', ('%' + preference + '%',)).fetchall()
        trailers = conn.execute('SELECT * FROM TrailerData').fetchall()
        conn.close()
        return render_template("home.html", username=username, preference=preference, trailers=trailers)
    except Exception as e:
        app.logger.error(f"Error | Loading Home: {e}")
        flash("An error occurred while loading the homepage.", "danger")
        return redirect(url_for("login"))

@app.route("/view")
def view_trailer():
    try:
        play = request.args.get("play")
        if play:
            conn = get_db_connection()
            trailer = conn.execute('SELECT * FROM TrailerData WHERE tid = ?', (play,)).fetchone()
            if trailer:
                # similar_trailers = conn.execute('SELECT * FROM TrailerData WHERE genre = ?', (trailer['genre'],)).fetchall()
                similar_trailers = conn.execute('SELECT * FROM TrailerData').fetchall()
                conn.close()
                return render_template("playvideo.html", trailer=trailer, similar_trailers=similar_trailers)
            flash("Invalid trailer ID", "danger")
            conn.close()
            return redirect(url_for("home"))
    except Exception as e:
        app.logger.error(f"Error | Viewing Trailer: {e}")
        flash("An error occurred while viewing the trailer.", "danger")
        return redirect(url_for("home"))

@app.route("/addmovie", methods=["GET", "POST"])
def addmovie():
    try:
        if request.method == "POST":
            moviename = request.form.get("moviename")
            description = request.form.get("description")
            thumbnail = request.form.get("thumbnail")
            actor = request.form.get("actor")
            genre = request.form.get("genre")
            path = request.form.get("path")  # New input for the file path

            conn = get_db_connection()
            conn.execute('INSERT INTO TrailerData (moviename, genre, description, actors, thumbnail, path) VALUES (?, ?, ?, ?, ?, ?)', 
                         (moviename, genre, description, actor, thumbnail, path))
            conn.commit()
            conn.close()
            flash("Trailer generated successfully", "success")
            return redirect(url_for("home"))
        return render_template("generate.html")
    except Exception as e:
        app.logger.error(f"Error | Generating Trailer: {e}")
        flash("An error occurred while generating the trailer. Please try again.", "danger")
        return redirect(url_for("home"))
    


# http://127.0.0.1:5000/generatetrailer?moviename=Avanger&preference=comedy_tech
@app.route("/generatetrailer", methods=["GET"])
def generatetrailer():
    # Retrieve parameters from the URL query string
    moviename = request.args.get("moviename")
    preference = request.args.get("preference")

    # Validate inputs
    if moviename != "" and preference != "":
        # Logic to generate the trailer should go here
        print(f"Trailer generation process initiated: moviename={moviename}, preference={preference}")
        # Here you would normally call your trailer generation logic
        flash("Trailer generation process initiated successfully!", "success")
        return redirect(url_for("home"))

    else:
        # If parameters are missing, return an error response
        flash("Please provide both movie name and preference.", "error")
        return redirect(url_for("home"))




@app.route("/account")
def account():
    """Retrieve user data from the database and render the account page."""
    try:
        if "user_id" not in session:
            flash("You need to log in to access your account.", "warning")
            return redirect(url_for("login"))

        user_id = session.get("user_id")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM UserData WHERE uid = ?", (user_id,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data is None:
            flash("User not found.", "danger")
            return redirect(url_for("login"))

        return render_template("account.html", user=user_data)

    except Exception as e:
        app.logger.error(f"Error | Loading Account: {e}")
        flash("An error occurred while loading your account information.", "danger")
        return redirect(url_for("login"))

# Initialization
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # Set up logging
    init_db()
    app.run(debug=True, host="0.0.0.0")
