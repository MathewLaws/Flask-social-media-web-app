from flask import render_template, Blueprint, request, flash
from flask_login import login_required, current_user
from .models import Post, User
from . import db
#from werkzeug.utils import secure_filename
import os

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        post = request.form.get("post")

        if post and "img" in request.files:
            new_post = Post(content=post, user_id=current_user.id)
            img = request.files["img"]
            #filename = secure_filename(img.filename)
            #print(os.path.relpath)
            db.session.add(new_post)
            db.session.commit()
            img.save(os.path.relpath(("website/static/images/" + str(new_post.id)).replace("\\", "/")))
            flash("New post made!", category="success")
        else:
            flash("You cannot post nothing!", category="error")


    posts = Post.query.order_by(Post.id.desc()).all()

    imgs_file_names = os.listdir("website/static/images")

    imgs_file_names = sorted(imgs_file_names, key = lambda x:x[0], reverse=True)

    for i, itm in enumerate(imgs_file_names):
        imgs_file_names[i] = f"images/{itm}"
    users = []
    dates = []
    for i, itm in enumerate(posts):
        userid = (User.query.get(itm.user_id))
        users.append(userid.username)
        dates.append(itm.date)

    #print(users)
    #print(posts)
    #print(dates)
    #print(imgs_file_names)

    user_data = list(zip(users, posts, dates, imgs_file_names))
    #print(user_data)
    return render_template("home.html", user=current_user, current=current_user.username, 
    data=user_data)