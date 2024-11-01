---
title: ""
permalink: "/earth-models/"
layout: archive
sidebar:
  nav: "all_posts_list"
classes:
  - wide
---
 
{% assign entries1 = site["earth-model"] %}
{% assign entries1 = entries1 | sort: 'date' | reverse %}


<section id="earth-model" class="taxonomy__section">
<h2 class="archive__subtitle" style="font-size: 1em;">Earth Models</h2>
<div class="entries-{{ page.entries_layout | default: 'list' }}">
  {% include posts-tag-earth-model.html taxonomy=page.taxonomy type=page.entries_layout %}
</div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }}
    &uarr;</a>
</section>

