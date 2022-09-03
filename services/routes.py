from werkzeug.security import check_password_hash,generate_password_hash
from werkzeug.routing import Rule

from app import Base, db,app
import string,flask,random,datetime,jwt
from flask import jsonify,request
from functools import wraps

user=Base.classes.user

app.url_map.add(Rule('/api/register',methods=['GET','POST'], endpoint='register'))
app.url_map.add(Rule('/api/login',methods=['GET','POST'], endpoint='login'))

def token_required(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        else:
            return jsonify({'message':"Missing authentication token",'ok':False})
        try:
            data=jwt.decode(token,app.config['SECRET_KEY'])
            current_user=db.session.query(user).filter_by(userName=data['user_id']).first()
            if not current_user:
                return jsonify({"message":"User doesn't exit!!",'ok':False})
        except:
            return jsonify({'message':"Token is Invalid",'ok':False})
        return func(current_user,*args,**kwargs)
    return decorated





@app.endpoint('register')
def register():
    firstName=request.json['firstName']
    lastName=request.json["lastName"]
    userName=request.json["userName"]
    email=request.json['email']
    dateOfBirth=request.json['dateOfBirth']
    password=request.json["password"]
    rePassword=request.json["rePassword"]
    if validatePassword(password,rePassword):
        uniqueId=''.join(random.sample(string.ascii_uppercase +string.digits+string.ascii_lowercase, k = 10))
        user_count= db.session.query(user).filter_by(uniqueId=uniqueId).count()
        user_check= db.session.query(user).filter_by(userName=userName).count()
        user_check2= db.session.query(user).filter_by(email=email).count()
        print(user_check,user_check2)
        if user_check:
            return jsonify({'message':'username already existed','ok':False})
        if user_check2:
            return jsonify({'message':'email already existed','ok':False})
        while user_count:
            uniqueId=''.join(random.sample(string.ascii_uppercase +string.digits+string.ascii_lowercase, k = 10))
            user_count= db.session.query(user).filter_by(uniqueId=uniqueId).count()
        created_at=datetime.date.today()
        password_hash=generate_password_hash(password)
        new_user=user(uniqueId=uniqueId,userName=userName,password=password_hash,firstName=firstName,lastName=lastName,email=email,dateOfBirth=dateOfBirth,createdAt=created_at)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message':"Account succesfully created!!",'ok':True})
    return jsonify({'message':"passwords not matched, Try again?",'ok':False})

def validatePassword(password,rePassword):
    return password==rePassword


@app.endpoint('login')
def login():
    userName=request.json['userName']
    password=request.json['password']
    login_user=db.session.query(user).filter_by(userName=userName).first()
    if not login_user:
        return jsonify({'message':"User doesn't exit!!",'ok':False})
    if check_password_hash(login_user.password,password):
        token=jwt.encode({'user_id':login_user.userName,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8'),'message':'Login sucessful','ok':True})
    return jsonify({'message':"enter correct password",'ok':False})


