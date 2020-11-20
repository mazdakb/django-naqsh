## [{{merge_date.strftime('%Y-%m-%d')}}]
{%- for change_type, pulls in grouped_pulls.items() %}
{%- if pulls %}
### {{ change_type }}
{%- for pull_request in pulls %}
- {{ pull_request.title }} ([#{{ pull_request.number }}]({{ pull_request.url }}))
{%- endfor -%}
{% endif -%}
{% endfor -%}
