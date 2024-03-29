# Our database models.
from polls.models import Poll, Choice

# Django shortcuts
#
# render_to_response = Renders a given template with a given context dictionary and
#   renders an HttpResponse object with that rendered text.
#
# get_object_or_404 = Render a 404 error page if object doesn't exist.
from django.shortcuts import render_to_response, get_object_or_404

# Allow us to send HTTP response and HTTP redirects.
from django.http import HttpResponseRedirect

# Add Cross Site Request Forgery proection
from django.template import RequestContext

# This allows us to not have to reconstruct each url in code but just replace args in the url given.
from django.core.urlresolvers import reverse

# Handle the POST request for submitting a users vote.
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)

    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You did not select a choice.",
        }, context_instance = RequestContext(request))

    else:
        # Update the vote count for the choice made and save it to the database.
        selected_choice.votes += 1
        selected_choice.save()

        # Always reutnr an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a user hits
        # the Back button.
        return HttpResponseRedirect(reverse('poll_results', args = (p.id, )))
