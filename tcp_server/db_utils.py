
import os
import sys

try:
    sys.path.append(os.environ['DJANGO_PROJECT_PATH'])
    # sys.path.append(os.environ['DJANGO_PROJECT_PATH'] + '/gpsserver')
except:
    pass

os.environ['DJANGO_SETTINGS_MODULE'] = 'gpsserver.settings'

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.contrib.gis.geos import Point

application = get_wsgi_application()


from gpsserver.models import Transport as DjTransport, TransportData as DjTransportData
from users.models import CustomUser as DjCustomUser


# --------------------------------------------------------------------------------------------------
class Transport(object):
    pass


# --------------------------------------------------------------------------------------------------
class TransportData(object):

    def save_data(self, user_id, dt, tm, lat, lon, course, speed, altitude, sats, flags1):
        if speed == "empty": speed = None
        if course == "empty": course = None
        if altitude == "empty": altitude = None
        if sats == "empty": sats = None
        if flags1 == "empty": flags1 = None

        try:
            ptn = Point(float(lon), float(lat))
            new_data = DjTransportData(
                user_id=user_id,
                point=ptn,
                altitude=altitude,
                speed=speed,
                satellites=sats,
                flags1=flags1,
            )
            new_data.save()
        except Exception as e:
            return False, str(e)

        return True, None

# --------------------------------------------------------------------------------------------------
class CustomUser(object):

    def check_login(self, _username, _password):
        try:
            user = DjCustomUser.objects.get(username__exact=_username, password__exact=_password)
            return user.id, None
        except Exception as e:
            return None, str(e)
