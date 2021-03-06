#
# Copyright (c) 2008-2009 Brad Taylor <brad@getcoded.net>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import simplejson

from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from berserk2.sprints.models import *

def reports_resolved_tasks_txt(request, sprint_id,
                               template_name='reports/resolved_tasks.txt'):
    sprint = get_object_or_404(Sprint, pk=int(sprint_id))
    tasks = Task.objects.filter(sprints=sprint)
    return render_to_response(template_name,
                              {'sprint': sprint,
                               'snapshots': [t.get_latest_snapshot() for t in tasks]},
                              mimetype='text/plain',
                              context_instance=RequestContext(request))
