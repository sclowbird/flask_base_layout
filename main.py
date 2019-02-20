import os
from webapp import create_app

#Sets environment variable e.g. export WEBAPP_ENV = development
env = os.environ.get('WEBAPP_ENV', 'dev')

#Basically same syntax as. 'config.{}Config'.format(env.capitalize())
app = create_app('config.%sConfig' % env.capitalize())
    
if __name__ == '__main__':
    app.run()