from subprocess import call
from uuid import uuid4
from time import sleep

def create_filename():
    filename = str(uuid4()) + '.html'
    print('Filename assigned {}'.format(filename))
    return filename

# Create a file
def add_file(filename):
    call(['touch', filename])
    print('Created filename {}'.format(filename))

# Push
def push(filename):
    call(['git', 'add', '.'])
    call(['git', 'commit', '-m', 'Created {}'.format(filename)])
    call(['git', 'push', 'origin', 'master'])
    print('Pushed to remote repo...')

seconds = 3
for x in range(10):
    sleep(seconds)
    filename = create_filename()
    add_file(filename)
    push(filename)
