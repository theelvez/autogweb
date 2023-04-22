from flask import render_template, redirect, url_for, flash, request, make_response
from app import app, db
from app.models import User, Car
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import qrcode
from io import BytesIO

# ... (your views functions go here)
