from django.db import models

# Create your models here.
class Event(models.Model):
    """This is the event data structure
        Blank/empty input is allowed and will be converted to null"""
    ##Fields##
    event_datetime = models.DateTimeField(help_text='Enter datetime of event')
    title = models.CharField(max_length=100, help_text='Enter title of event', null=True, blank=True)
    location = models.CharField(max_length=60, help_text='Enter the city location', null=True, blank=True)
    #note: availability is currently a string. consider splitting into start and end date
    availability = models.CharField(max_length=100, help_text='Enter the range of available dates', null=True, blank=True)
    speaker = models.CharField(max_length=60, help_text='Enter speaker name', null=True, blank=True)
    discount_policy = models.CharField(max_length=100, help_text='Enter discount policy', null=True, blank=True)
    ##[CHANGE] change into a file upload (image upload)
    description_picture = models.CharField(max_length=60, help_text='Enter image description', null=True, blank=True)
    price_final = models.IntegerField(help_text='Enter final price', null=True, blank=True)
    """[CHANGE] have other price fields uploaded (ex: original price), convert to 
    a price object later"""

    ##Metadata
    class Meta:
        #order by most recent event to least recent
        ordering = ['-event_datetime']
    
    ##Methods
    def __str__(self):
        return self.title

    

