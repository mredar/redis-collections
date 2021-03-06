

__title__ = 'redis-collections'
__version__ = '0.1.7'
__author__ = 'Honza Javorek'
__license__ = 'ISC'
__copyright__ = 'Copyright 2013 Honza Javorek'


import sys
from .base import RedisCollection  # NOQA

from .sets import Set  # NOQA
from .lists import List  # NOQA
from .dicts import Dict # NOQA
if sys.version_info[:2] > (2, 6):
    from .dicts import Counter
