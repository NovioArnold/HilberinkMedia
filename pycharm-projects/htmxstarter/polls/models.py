from django.db import models

#database models

#Questions model
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

#Choises model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

#Content model
class Content(models.Model):
    name_task = models.CharField(max_length=128)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name_task

#media model
class Media(models.Model):
    name_file = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f'the name of the file is {self.name_file}'

#Card model
class Card(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateField()
    Start_date = models.DateField(null=True)
    End_date = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    set_alert = models.BooleanField(default=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



