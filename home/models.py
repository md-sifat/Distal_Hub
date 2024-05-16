from django.db import models

# database model for patient data 

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=1)
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    firstname = models.CharField(max_length=100 , default='Firstname')
    lastname = models.CharField(max_length=100 , default='Lastname')
    aboutme = models.TextField(max_length= 1000 , default='I am a passionate individual with a keen interest in technology and innovation. With a background in computer science, I am driven by curiosity and a desire to learn and grow. I enjoy tackling complex problems and finding creative solutions. In my free time, I love exploring the outdoors, reading science fiction novels, and experimenting with new recipes in the kitchen. I believe in continuous self-improvement and strive to make a positive impact in both my personal and professional life.')
    img = models.ImageField(upload_to='user_image/' ,  default='user_image/img2.jpg')
    
    def __str__(self):
        return self.username


# database model for doctor profile 

class DoctorProfile(models.Model):
    serialno = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100 , default='No data')
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    firstname = models.CharField(max_length=100 , default='Firstname')
    lastname = models.CharField(max_length=100 , default='Lastname')
    aboutme = models.TextField(max_length= 200 , default='I am a dedicated and compassionate medical professional committed to providing excellent care to my patients. With years of experience in [specialty], I have honed my skills and expertise to deliver the highest standard of medical treatment. I believe in taking a holistic approach to patient care, considering not only the physical aspects but also the emotional and psychological well-being of my patients. My goal is to empower individuals to take control of their health and lead fulfilling lives. Outside of work, I enjoy staying active through hiking and yoga, as well as spending quality time with my family.')
    img = models.ImageField(upload_to='user_image/' ,  default='doctor.png')
    
    def __str__(self):
        return self.serialno


