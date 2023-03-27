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
    professorRating = models.CharField('Will you take this course with this professor again?',max_length=100)
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
    

class Applicant(models.Model):
    courseList = Course.objects.all()
    courses = []
    for courseReq in courseList:
        courses.append((courseReq.courseName[0:3],courseReq.courseName))

    CHOICES = tuple(courses)
    for courseReq in courseList:
        courseReq.courseName.lower()

    appFName = models.CharField('First Name', max_length=100,default="")
    appLName = models.CharField('Last Name', max_length=100,default="")
    appUCID = models.CharField('UCID',max_length=100,default="")
    course = models.CharField('course',max_length=100,default="", choices=CHOICES)
    major = models.CharField('major',max_length=100,default="")
    year = models.CharField('year',max_length=100,default="")
    ques1 = models.TextField('ques1', default="")
    ques2 = models.TextField('ques2', default="")

    def __str__(self):
        appName = self.appFName + " " + self.appLName
        return appName
    