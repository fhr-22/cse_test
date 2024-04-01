# Site - Dept of CSE, Kalyani University

Static website, with easy notice uploads directly from the Github web UI. 

Built using Github Actions and static hosting provided by Vercel.

> [!IMPORTANT]  
> - Any of the following modifications to the source code (and subsequently updates to the website) are only possible if you're logged in and own the repository, or have write access to it.
> - After performing any change such as creating/uploading/modifying a file, make sure to click the  **"Commit changes"** button.


## Uploading Notices

To upload a notice, simply upload a file to the [site/notice_files](site/notice_files) folder and confirm using the `Commit changes` button. The `/notices.html` page on the site will automatically be updated, with the file name used for the notice link.


## Updating site pages

The source templates for the site pages are in the [templates](templates) folder. After editing the file and commiting, wait for a site rebuild for the changes to be visible.

## Adding a page

To create a page with the name `new_page.html` follow the given steps:

- Create a new file in the  [templates](templates) folder (`new_page.html`)
- Populate the file as required, using the appropriate template directives. Refer to the files already present in the folder. For example, 
```
{% extends "header_footer.html" %}

{% block description %}New Page - Dept. of CSE, KU{% endblock %}
{% block title %}KUCSE - New Page{% endblock %}

{% block content %}

<h1> New Page </h1>

<p> Example text. </p>

{% endblock %}
```

- Update the build script - [`render_static_pages.py`](build_scripts/render_static_pages.py) by appending the following at the end of the file : `render_and_save_template("new_page.html")`.

- To add a navbar entry for the newly added page, update the [`header_footer.html`](templates/header_footer.html) template by adding a new link to the existing navbar section. For example, 
```
   <nav>
        <a href="notices.html">NOTICES</a>
        <a href="people.html">PEOPLE</a>
        <a href="courses.html">COURSES</a>
        <a href="highlights.html">HIGHLIGHTS</a>
        <a href="new_page.html">NEW PAGE</a>
    </nav>

```


