from flask import Flask,url_for,Request,render_template,abort,json
app = Flask(__name__)

@app.route('/')
def helloworld():
	return "helloworld"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path
    return 'Subpath %s' % subpath

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/okay',methods=['POST'])
def okay():
	app.logger.debug('A value for debugging')
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.logger.error('An error occurred')
	return "woah"

@app.route('/hello/')
@app.route('/hello/<username>')
def templateMagic(username=None):
	return render_template('hello.html',kay=name)

@app.route('/chamberofsecrets')
def blocked():
	abort(401)
	return "congratulations, you are a slythrin"

@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'), 401

with app.test_request_context():
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))
