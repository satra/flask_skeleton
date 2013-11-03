from app import app

from flask import render_template

from uuid import uuid1

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/submit', methods=['POST'])
def submit_job():
    """Submit a job to the queue."""
    id = uuid1().hex
    app.jobs.append(id)
    print app.jobs
    return "Submitting job[%s]" % id

@app.route('/destroy/<id>')
def destroy_job(id):
    """Remove a job from the queue."""
    try:
        app.jobs.remove(id)
        return 'Removing job[%s] from queue' % id
    except Exception, e:
        return 'Could not remove job[%s] because %s' % (id, e)

@app.route('/status/<id>')
def job_status(id):
    """Return current status of job from queue."""
    return 'job: %s status: unknown ' % id

@app.route('/file/<location>')
def get_file(location):
    """Return current status of job from queue."""
    return 'location: %s ' % location
