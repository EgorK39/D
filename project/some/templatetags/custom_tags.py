from django import template
from datetime import datetime
import pytz
from datetime import datetime
from pprint import pprint

from some.models import UserModel

register = template.Library()


@register.simple_tag()
def current_time():
    tz = datetime.today().strftime('%H:%M')
    return tz


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
