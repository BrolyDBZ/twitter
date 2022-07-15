
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField,DateField,SubmitField
from wtforms.validators import DataRequired, Email, Length
from datetime import date

class registrationForm(FlaskForm):
    class Meta:
        csrf=False
    firstName=StringField('firstName',validators=[DataRequired(),Length(max=64)])
    lastName=StringField('lastName',validators=[DataRequired(),Length(max=64)])
    userName=StringField('username',validators=[DataRequired(),Length(max=32)])
    email=StringField('email',validators=[DataRequired(),Length(max=100),Email()])
    dateOfBirth=DateField('Date of Birth',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    rePassword=PasswordField('re-enter password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validatePassword(self,password,rePassword):
        if password==rePassword:
            return True
        return False


