from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CertificateForm
from app.models import Certificate
from datetime import date

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CertificateForm()
    if form.validate_on_submit():
        # Save to DB
        cert = Certificate(student_name=form.student_name.data, course=form.course.data)
        db.session.add(cert)
        db.session.commit()
        
        flash(f'Certificate requested for student {form.student_name.data}, course {form.course.data}')
        # Redirect to the certificate page
        return redirect(url_for('certificate', id=cert.id))
    return render_template('index.html', title='Home', form=form)

@app.route('/certificate/<int:id>')
def certificate(id):
    cert = Certificate.query.get_or_404(id)
    return render_template('certificate.html', certificate=cert, date=date.today())