from django.db import models

# Create your models here.
class Entity(models.Model):
#   entity_id = models.IntegerField(primary_key=True,unique=True)
    entity_name = models.CharField(max_length=264)
    Tax_reg_no = models.IntegerField(unique=True)
    address = models.CharField(max_length = 264)
    reg_date = models.DateField()
    contact_no = models.IntegerField()

    def __str__(self):
            return self.entity_name

class Program(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    programe_name =  models.CharField(max_length = 264)
    no_of_people = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    place = models.CharField(max_length=294)
    description = models.CharField(max_length=294)

    def __str__(self):
            return self.prog_name

class Topic(models.Model):
    program =  models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length = 294)
    description = models.CharField(max_length = 294)

class Actor(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    actor_name = models.CharField(max_length = 294)

class Funtions(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    fun_name = models.CharField(max_length = 294, unique=True)

class Combination(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    Funct = models.ForeignKey(Funtions, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
