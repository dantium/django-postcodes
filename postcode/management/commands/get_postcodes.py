""" Setup file to get postcode and location data into the database """
import re
import csv
import urllib

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from postcode.models import Postcode


postcode_dir = "http://seagrass.goatchurch.org.uk/~julian/postcodes/data/CSV/"


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Postcode.objects.all().delete()
        count = 0
        
        d = urllib.urlopen(postcode_dir).read()
        postcodefiles = re.findall('<a href="(.*?\.csv)">', d)
        nprog = 0
        
        for n in range(nprog, len(postcodefiles)):
            fl = postcodefiles[n]
            print 'Processing %d %s ...' % (n, fl)
            s = urllib.urlopen(postcode_dir + fl)
            c = csv.reader(s.readlines())
            for row in c:
                postcode = row[0]
                lat = float(row[2])
                lng = float(row[3])
                location = Point(lng, lat)
                Postcode.objects.create(code=postcode, location=location)
                count += 1
                if count % 10000 == 0:
                    print "Imported %d" % count
            nprog = n+1