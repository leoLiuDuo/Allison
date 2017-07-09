from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from content_read import dir_read


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('Home.html')


@app.route('/Contact')
def contact():
    return render_template('Contact.html')


@app.route('/Project')
def project():
    content = dir_read('project')
    return render_template('Project.html', content=content)


@app.route('/Photography')
def photography():
    return render_template('Photography.html')


@app.route('/Illustration')
def illustration():
    return render_template('Illustration.html')


@app.route('/<dir>/<package>')
def package_detail(dir, package):
    return render_template('package_detail.html', dir=dir, package=package)

if __name__ == '__main__':
    app.run(debug=True)

