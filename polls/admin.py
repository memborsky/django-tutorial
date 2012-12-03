from django.contrib import admin

from polls.models import Poll
from polls.models import Choice

# This is being used to allow us to move our choice selections
# into the poll add/change area so we have a more effecient
# workflow.
#
# admin.StackedInline = Stacks choice field per row.
# admin.TabularInline = Stacks choice per row.
class ChoiceInline(admin.TabularInline):

    # The database model is obviously Choice.
    model = Choice

    # Show 3 empty chocie setups off the line.
    extra = 3

# The controll of how information is being displayed in the admin
# section of the website relating to polls.
class PollAdmin(admin.ModelAdmin):

    # This adjusts the way the Polls listing is displayed on the
    # /admin/polls/poll/ page.
    list_display = ('question', 'pub_date', 'was_published_recently')

    # Change the way Poll fields are displayed on the
    # individual Add/Change poll admin pages.
    fieldsets = [
        (None,                  {'fields': ['question']}),
        ('Date infomration',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # The below line is a basic method of adding fields to Poll
    # admin page.
    # fields = ['pub_date', 'question']

    # Add choices to poll creation.
    inlines = [ChoiceInline]

    # Add a single filter by the date published.
    list_filter = ['pub_date']

    # Search our polls question field. (This uses a LIKE search method)
    search_fields = ['question']

    # Add hierarchial navigation by date to the top of the change list page.
    date_hierarchy = 'pub_date'

# This registeres polls to be modified in the admin section.
# The controller for how the information is displayed is PollAdmin.
admin.site.register(Poll, PollAdmin)
