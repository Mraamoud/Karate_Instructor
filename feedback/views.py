from django.shortcuts import render
from feedback.models import ProgressHistory
from django.http import Http404
from django.core.serializers.json import DjangoJSONEncoder
import json

def user_progress(request, user_id):
    # Fetch progress history for the given user
    progress_data = ProgressHistory.objects.filter(user_id=user_id).order_by('session_id__session_date')

    # Check if data exists for the user
    if not progress_data.exists():
        raise Http404("No progress data found for this user.")

    # Prepare the data for Chart.js
    data = {
        "labels": [entry.session_id.session_date.strftime('%Y-%m-%d') for entry in progress_data],
        "scores": [entry.progress_score for entry in progress_data],
    }

    # Pass the serialized data to the template
    return render(request, 'progress_chart.html', {'data': json.dumps(data, cls=DjangoJSONEncoder)})
