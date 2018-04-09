from flask import Flask, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import PostForm, CommentForm


app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG = True,
    SECRET_KEY='development key',
    WTF_CSRF_ENABLED = False,
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vadim:root@localhost/test'
db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    from models import Post
    posts = Post.query.order_by(Post.title).all()
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    from models import Post
    if request.method == 'POST':
        post_form = PostForm(request.form)
        if post_form.validate():
            post = Post(post_form.title.data, post_form.text.data)
            db.session.add(post)
            db.session.commit()
            flash('Form  saved')
            return redirect('/')
    else:
        post_form = PostForm()
    return render_template('create_post.html', post_form=post_form)


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    from models import Post

    post = Post.query.get_or_404(post_id)
    print(post)
    return render_template('post_detail.html', post = post)




if __name__ == '__main__':
    app.run(debug=True)
