from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


@app.route("/save_student", methods=["POST"])
def save_student():

    name = request.form["name"]
    usn = request.form["usn"]
    branch = request.form["branch"]
    cgpa = request.form["cgpa"]

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, usn, branch, cgpa) VALUES (?, ?, ?, ?)",
        (name, usn, branch, cgpa)
    )

    conn.commit()
    conn.close()

    return """
    <h1>Student Added Successfully!</h1>
    <a href="/">Go Home</a>
    """


@app.route("/view_students")
def view_students():

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "view_students.html",
        students=students
    )


@app.route("/search_student", methods=["GET", "POST"])
def search_student():

    if request.method == "POST":

        usn = request.form["usn"]

        conn = sqlite3.connect("placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE usn=?",
            (usn,)
        )

        student = cursor.fetchone()

        conn.close()

        if student:

            return f"""
            <h1>Student Found</h1>
            <p>Name: {student[1]}</p>
            <p>USN: {student[2]}</p>
            <p>Branch: {student[3]}</p>
            <p>CGPA: {student[4]}</p>
            <a href="/">Go Home</a>
            """

        return """
        <h1>Student Not Found</h1>
        <a href="/">Go Home</a>
        """

    return render_template("search_student.html")


@app.route("/delete_student", methods=["GET", "POST"])
def delete_student():

    if request.method == "POST":

        usn = request.form["usn"]

        conn = sqlite3.connect("placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE usn=?",
            (usn,)
        )

        conn.commit()
        conn.close()

        return """
        <h1>Student Deleted Successfully!</h1>
        <a href="/">Go Home</a>
        """

    return render_template("delete_student.html")


@app.route("/add_company", methods=["GET", "POST"])
def add_company():

    if request.method == "POST":

        company = request.form["company"]
        cgpa = request.form["cgpa"]

        conn = sqlite3.connect("placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO companies (company, cgpa) VALUES (?, ?)",
            (company, cgpa)
        )

        conn.commit()
        conn.close()

        return """
        <h1>Company Added Successfully!</h1>
        <a href="/">Go Home</a>
        """

    return render_template("add_company.html")


@app.route("/view_companies")
def view_companies():

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM companies")

    companies = cursor.fetchall()

    conn.close()

    return render_template(
        "view_companies.html",
        companies=companies
    )


@app.route("/eligibility", methods=["GET", "POST"])
def eligibility():

    if request.method == "POST":

        usn = request.form["usn"]
        company = request.form["company"]

        conn = sqlite3.connect("placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT cgpa FROM students WHERE usn=?",
            (usn,)
        )

        student = cursor.fetchone()

        cursor.execute(
            "SELECT cgpa FROM companies WHERE company=?",
            (company,)
        )

        company_data = cursor.fetchone()

        conn.close()

        if student and company_data:

            if student[0] >= company_data[0]:
                return "<h1>Eligible</h1><a href='/'>Go Home</a>"
            else:
                return "<h1>Not Eligible</h1><a href='/'>Go Home</a>"

        return "<h1>Data Not Found</h1><a href='/'>Go Home</a>"

    return render_template("eligibility.html")


if __name__ == "__main__":
    app.run(debug=True)