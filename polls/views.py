# Our database model to the polls so we can render some dynamic content.
from polls.models import Poll

# Django shortcuts
#
# render_to_response = Renders a given template with a given context dictionary and
#   renders an HttpResponse object with that rendered text.
#
# get_object_or_404 = Render a 404 error page if object doesn't exist.
from django.shortcuts import render_to_response, get_object_or_404

# Raw HTTP response.
from django.http import HttpResponse

# The /polls/ view.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

# The /polls/<id>/ view.
def detail(request, poll_id):
    # Raise Http404 if poll_id doesn't exist.
    p = get_object_or_404(Poll, pk = poll_id)

    return render_to_response('polls/detail.html', {'poll': p})

# The /polls/<id>/results/ view.
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

# The /polls/<id>/vote/ view.
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
