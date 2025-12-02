from app import db

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(64), index=True)
    course = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Certificate {self.student_name} - {self.course}>'
