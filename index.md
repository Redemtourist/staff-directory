---
layout: default
---

# Staff & Organization Directory

<ul>
{% for person in site.staff %}
  <li>
    <a href="{{ person.url }}">{{ person.name }}</a> – {{ person.role }}
  </li>
{% endfor %}
</ul>
