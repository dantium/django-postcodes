""" Setup file to get postcode and location data into the database """
from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from postcode.models import Postcode
import csv
import re
import urllib2

postcode_dir = getattr(settings, 'POSTCODE_DIR', 'http://codepoint.danatkinson.com/csv/')

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Postcode.objects.all().delete()
        count = 0
        
        d = urllib2.urlopen(postcode_dir).read()
        postcodefiles = re.findall('<a href="(.*?\.csv)">', d)
        nprog = 0
        
        for n in range(nprog, len(postcodefiles)):
            fl = postcodefiles[n]
            print 'Processing %d %s ...' % (n, fl)
            s = urllib2.urlopen(postcode_dir + fl)
            c = csv.reader(s.readlines())
            for row in c:
                postcode = row[0]
                location = Point(map(float, row[10:12]))
                Postcode.objects.create(code=postcode, location=location)
                count += 1
                if count % 10000 == 0:
                    print "Imported %d" % count
            s.close()
            nprog = n+1