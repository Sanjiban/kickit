import os
from .utils import get_files, get_branches
from flask import Flask
from flask import render_template

app = Flask(__name__)

PATH = '/home/kdas/code/git/'

@app.route('/<reponame>')
def index(reponame):
    repopath = os.path.join(PATH, reponame)
    if not os.path.exists(repopath):
        return "Sorry"
    dirs, files = get_files(repopath, 'master')
    branches = get_branches(repopath)
    return render_template('index.html', dirs=dirs, files=files, projectname=reponame, branches=branches)


@app.route('/<reponame>/tree/<branchname>', defaults={'path': ''})
@app.route('/<reponame>/tree/<branchname>/<path:path>')
def index_branch(reponame, branchname, path):
    print path
    repopath = os.path.join(PATH, reponame)
    if not os.path.exists(repopath):
        return "Sorry"
    dirs, files = get_files(repopath, branchname, param=path)
    branches = get_branches(repopath)
    return render_template('index.html', dirs=dirs, files=files, projectname=reponame, branches=branches, param=path,
                           branch=branchname)