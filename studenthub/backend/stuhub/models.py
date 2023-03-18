from django.db import models

class Tutor(models.Model):
    tutorID = models.CharField('Tutors ID',max_length=100)
    tutorName = models.CharField('Tutors Name',max_length=100)
    tutorEmailAddress = models.EmailField('Email Address')
    tutorPhoneNumber = models.TextField('PhoneNumber')
    tutorAbout = models.TextField('About')

    def __str__(self):
        return self.tutorName

class Professor(models.Model):
    profID = models.CharField('Professors ID',max_length=100)
    profName = models.CharField('Professors Name',max_length=100)
    profEmailAddress = models.EmailField('Email Address')
    profPhoneNumber = models.TextField('PhoneNumber')
    profAbout = models.TextField('About')

    def __str__(self):
        return self.profName


class Comment(models.Model):
    courseName = models.CharField('Course Name',max_length=100)
    professorRating = models.CharField('Prof Rating 1-10',max_length=100)
    professorN = models.CharField('Professors Name',max_length=100)
    courseComment = models.TextField('Comment')
    commenterName =models.CharField('Commenters Name',max_length=100)

    def __str__(self):
        return self.courseName
      


class Course(models.Model):
    courseName = models.CharField('Course Name', max_length=100)
    courseProfessors = models.ManyToManyField(Professor, blank=True)
    courseSummary = models.TextField(blank=True)
    courseTutors = models.ManyToManyField(Tutor, blank=True)
    
    def __str__(self):
        return self.courseName