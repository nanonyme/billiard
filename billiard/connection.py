from __future__ import absolute_import

import sys

if sys.version_info[0] == 3:
    import multiprocessing.connection
    sys.modules['billiard.connection'] = multiprocessing.connection
else:
    import billiard._connection
    sys.modules['billiard.connection'] = billiard._connection
