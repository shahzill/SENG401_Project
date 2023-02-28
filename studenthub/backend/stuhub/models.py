from django.db import models

class Tutor(models.Model):
    tutorName = models.CharField('Tutors Name',max_length=100)
    tutorEmailAddress = models.EmailField('Email Address')
    tutorPhoneNumber = models.TextField('PhoneNumber')
    tutorAbout = models.TextField('About')

    def __str__(self):
        return self.tutorName


class Comment(models.Model):
    courseName = models.CharField('Course Name',max_length=100)
    professorRating = models.CharField('Prof Rating 1-10',max_length=100)
    courseComment = models.TextField('Comment')
    commenterName =models.CharField('Commenters Name',max_length=100)

    def __str__(self):
        return self.courseComment + " :  "+ self.commenterName
        
class Professor(models.Model):
    profName = models.CharField('Professors Name',max_length=100)
    profEmailAddress = models.EmailField('Email Address')
    profPhoneNumber = models.TextField('PhoneNumber')
    profAbout = models.TextField('About')

    def __str__(self):
        return self.profName + "      Email: " + self.profEmailAddress


class Course(models.Model):
    courseName = models.CharField('Course Name', max_length=100)
    courseProfessors = models.ManyToManyField(Professor, blank=True)
    courseSummary = models.TextField(blank=True)
    courseComments = models.ManyToManyField(Comment, blank=True)
    courseTutors = models.ManyToManyField(Tutor, blank=True)
    
    def __str__(self):
        return self.courseName