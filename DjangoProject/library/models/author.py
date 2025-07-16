from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    olid = models.CharField(max_length=50, unique=True, null=True)

    def get_open_library_key(self) -> str | None:
        """Return the Open Library key for the author."""
        return f'/authors/{self.olid}' if self.olid else None

    def is_alive(self) -> bool:
        return self.death_date is None

    def how_old(self) -> int | bool:
        """Calculate the age of the author based on birth date."""
        from django.utils import timezone

        if self.birth_date:
            return timezone.now().year - self.birth_date.year
        return False

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Author({self.name}, {self.birth_date}, {self.death_date}, {self.country})"
