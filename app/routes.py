from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import CertificateForm
from app.models import Certificate
from datetime import date
import qrcode
import io
import base64

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
    
    # Generate QR Code
    # In production, use _external=True for absolute URL
    url = url_for('certificate', id=id, _external=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to buffer
    buffered = io.BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return render_template('certificate.html', certificate=cert, date=date.today(), qr_code=img_str)

@app.route('/admin')
def admin():
    certificates = Certificate.query.all()
    return render_template('admin.html', certificates=certificates)

@app.route('/admin/delete/<int:id>', methods=['POST'])
def delete_certificate(id):
    cert = Certificate.query.get_or_404(id)
    db.session.delete(cert)
    db.session.commit()
    flash(f'Certificate for {cert.student_name} deleted.')
    return redirect(url_for('admin'))