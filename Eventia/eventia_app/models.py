from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("concerts", "Concerts"),
        ("festivals", "Festivals"),
        ("dj-parties", "DJ Parties"),
        ("standup-comedy", "Stand-up Comedy"),
        ("movie-premieres", "Movie Premieres"),
        ("theatre", "Theatre Performances"),
        ("opera-ballet", "Opera & Ballet"),
        ("matches", "Matches & Tournaments"),
        ("runs-cycling", "Runs & Cycling"),
        ("yoga-wellness", "Yoga & Wellness"),
        ("educational-courses", "Educational Courses"),
        ("seminars", "Seminars & Lectures"),
        ("masterclasses", "Masterclasses"),
        ("business-workshops", "Business Workshops"),
        ("exhibitions-art", "Exhibitions & Art"),
        ("food-gastronomy", "Food & Gastronomy"),
        ("online-events", "Online Events"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="event_images/")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='concerts'
    )

    def __str__(self):
        return self.title

    def display_price(self):
        if self.price == 0:
            return "Free"
        return f"{self.price} ֏"
