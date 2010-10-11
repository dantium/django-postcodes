""" Geo aware Postcode App using Data from Code-point """


from django.contrib.gis.db import models





class Postcode(models.Model):
    code = models.CharField(max_length=8, db_index=True)
    location = models.PointField(srid=27700)  
    
    objects = models.GeoManager()
    
    def _get_area(self):
        """ Try to return the postcodes area from google maps API """
        pass
    
    def __unicode__(self):
        return "%s" % (self.code)
    