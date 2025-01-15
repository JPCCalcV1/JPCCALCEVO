# core/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

# Rate-Limiter: Standardmäßig kein globales Limit, wir vergeben Limits per Dekorator
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[]
)

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))