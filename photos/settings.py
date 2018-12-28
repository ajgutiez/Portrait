# -*- coding: utf-8 -*-
from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative_commons')
)

#nos permite definirlas en el setting de portrait
LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)

BADWORDS = getattr(settings, 'PROJECT_BADWORDS', [])