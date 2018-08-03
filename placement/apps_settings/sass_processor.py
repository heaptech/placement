import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATIC_ROOT = '/tmp/statics/'

SASS_PROCESSOR_ROOT = STATIC_ROOT

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_PATH, 'webapp/static'),
]

SASS_PRECISION = 8

# If inside of your SASS/SCSS files, you also want to import (using @import "path/to/scssfile";)
# files which do not start with an underscore,
# then you can configure another Regex pattern in your settings,
# for instance:
# SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
