from flask import render_template, Blueprint, request, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Post
from . import db
import base64

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        post = request.form.get("post")

        if post:
            image = request.files["img"]
            filename = secure_filename(image.filename)
            mimetype = image.mimetype
            read = base64.b64encode(image.read())
            read = read.decode("ascii")
            print(type(read))
            print(mimetype)
            new_post = Post(content=post, img=read,
                            name=filename, mimetype=mimetype, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash("New post made!", category="success")
        else:
            flash("Empty post!", category="error")

    data = Post.query.order_by(Post.id.desc()).all()

    return render_template("home.html", data=data, user=current_user)
