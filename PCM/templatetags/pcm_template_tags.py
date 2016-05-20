# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
import datetime
register = template.Library()

@register.inclusion_tag('tags/spacing_work.html')
def SpacingProgress(**kwargs):
    StartTime=kwargs['StartTime']
    EndTime=kwargs['EndTime']

    result = {}
    if not StartTime is None and not EndTime is None:
        result['StartTime'] = StartTime
        result['EndTime'] = EndTime
        spacework = int((EndTime - StartTime).total_seconds())
        result['spacework'] = spacework
        result['percent'] = spacework * 100 / 32400
        spacetext = ''
        if spacework > 86400:
            spacetext = spacetext + str(spacework // 86400) + ' д. '
            spacework = spacework % 86400
        if spacework > 3600:
            spacetext = spacetext + str(spacework // 3600) + ' ч. '
            spacework = spacework % 3600
        if spacework > 60:
            spacetext = spacetext + str(spacework // 60) + ' мин. '
        result['spacetext'] = spacetext

    return {'result': result}


t = get_template('tags/spacing_work.html')
register.inclusion_tag(t)(SpacingProgress)

@register.filter()
def previus_day(value):
    return  value - datetime.timedelta(days=1)

@register.filter()
def next_day(value):
    return  value + datetime.timedelta(days=1)



