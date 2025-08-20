from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector 

app = Flask(__name__)
app.secret_key = '123abc'

def open_conn():
    """Connect toMySQL database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='task_db'
    )

@app.route('/')
def home():
    return redirect('/details')

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        # personal details
        session['first_name'] = request.form['first_name'].strip()
        session['last_name']  = request.form['last_name'].strip()
        session['email']      = request.form['email'].strip()
        session['dob']        = request.form['dob']
        session['gender']     = request.form['gender']
        session['phoneno']    = request.form['phoneno'].strip()
        session['city']       = request.form['city'].strip()
        session['state']      = request.form['state'].strip()
        return redirect('/edu')
    return render_template('details.html')

@app.route('/edu', methods=['GET', 'POST'])
def edu():
    if 'first_name' not in session:
        return redirect('/details')

    if request.method == 'POST':
        # edu details
        degree         = request.form['degree'].strip()
        institution    = request.form['institution'].strip()
        subject        = request.form['subject'].strip()
        cgpa           = float(request.form['cgpa'])
        year_started   = int(request.form['year_started'])
        year_graduated = int(request.form['year_graduated'])

        # personal details from session
        first_name = session['first_name']
        last_name  = session['last_name']
        email      = session['email']
        dob        = session['dob']
        gender     = session['gender']
        phoneno    = session['phoneno']
        city       = session['city']
        state      = session['state']

        # save to databse
        conn = open_conn()
        cur  = conn.cursor()
        sql  = """INSERT INTO users
                  (first_name, last_name, email, dob, gender, phoneno, city, state,
                   degree, institution, subject, cgpa, year_started, year_graduated)
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            cur.execute(sql, (first_name, last_name, email, dob, gender,
                              phoneno, city, state,
                              degree, institution, subject, cgpa,
                              year_started, year_graduated))
            conn.commit()
            session.clear()
            return redirect(url_for('success', name=first_name))
        except Exception as e:
            flash(str(e))
            return redirect('/details')
        finally:
            cur.close()
            conn.close()

    return render_template('edu.html')

@app.route('/success')
def success():
    name = request.args.get('name', 'User')
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)