import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Poll(models.Model):
    # The poll question we are asking.
    question = models.CharField(max_length = 200)

    # The date it was published.
    pub_date = models.DateTimeField('date published')

    # Return a the question instead of the oject of the poll model.
    def __unicode__(self):
        return self.question

    # Chceks to see if this question was published in the last day.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    # Allows us to order by this field in the admin Poll view.
    was_published_recently.admin_order_field = 'pub_date'

    # Declares that this result is of a boolean type.
    was_published_recently.boolean = True

    # Change the way it is displayed in the views so it isn't the method name.
    was_published_recently.short_description = 'Published recently?'

# This is the database model for the Choices to a Poll.
class Choice(models.Model):
    # This relates database to Poll with a foreignkey on id.
    poll    = models.ForeignKey(Poll)

    # The name of the choice.
    choice  = models.CharField(max_length = 200)

    # The number of votes for the choice.
    votes   = models.IntegerField()

    # Allows us to return a string of the database object instead of an object.
    def __unicode__(self):
        return self.choice
