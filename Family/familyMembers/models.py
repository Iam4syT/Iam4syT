from django.db import models
from django.contrib.auth.models import User
# models.py in familyMembers app

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')

class Photo(models.Model):
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    oriki = models.CharField(max_length=50, blank=True, null=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('PNTS', 'Prefer not to say'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=5, choices=gender_choices)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    place_of_death = models.CharField(max_length=100, blank=True, null=True)
    living_status = models.BooleanField(default=True)  # True for alive, False for deceased

    # Contact Information
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Family Relationships (self-referencing fields)
    parents = models.ManyToManyField('self', symmetrical=False, related_name='children', blank=True)
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='spouses')
    siblings = models.ManyToManyField('self', symmetrical=True, blank=True)
    grandparents = models.ManyToManyField('self', symmetrical=False, related_name='grandchildren', blank=True)

    # Biographical Details
    occupation = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    hobbies_and_interests = models.TextField(blank=True, null=True)
    notable_achievements = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    # Health Information
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    genetic_information = models.TextField(blank=True, null=True)

    # Profile and Media
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    photos = models.ManyToManyField('Photo', blank=True) 
    videos = models.ManyToManyField('Video', blank=True)
    documents = models.ManyToManyField('Document', blank=True)


    # Ancestry Details
    ethnicity = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    family_origin = models.CharField(max_length=100, blank=True, null=True)
    notable_ancestry_events = models.TextField(blank=True, null=True)

    # Other Details
    nickname = models.CharField(max_length=50, blank=True, null=True)
    family_role = models.CharField(max_length=50, blank=True, null=True)
    special_notes = models.TextField(blank=True, null=True)
    favorite_family_traditions = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('date_of_birth',)
        verbose_name_plural = 'Members'
    
    def __str__(self):
        return self.first_name
        
