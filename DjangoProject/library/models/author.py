from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    nationality = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Author({self.name}, {self.birth_date})"

    def __repr__(self):
        return f"Author({self.name}, {self.birth_date})"