# BSL-Group

## Cloning the Repository
To clone the bsl-group.github.io repository to your local machine, follow these steps:

### Steps to Clone the Repository:
1. Open a terminal on your machine.
1. Navigate to the directory where you want to clone the repository.
    ```bash
    cd path/to/your/directory
    ```
1. Run the following command to clone the repository:
    ```bash
    git clone https://github.com/bsl-group/bsl-group.github.io.git
    ```
1. Navigate to the cloned directory:
    ```bash
    cd bsl-group.github.io
    ```

## Writing and Editing Posts
- Jekyll uses Markdown files for creating posts. The posts are stored in the `_posts` directory and should follow a specific naming convention: `YYYY-MM-DD-post-title.md`.
- The directory is organized into subdirectories such as home and research-papers, with each post being a Markdown file that contains front matter defining the title, date, tags, classes, sidebar navigation, category, excerpt, and a header image (teaser).

### Steps to Create a New Post:
1. Navigate to the `_posts` directory:
    ```bash
    cd _posts
    ```
1. Create a new Markdown file for your post:
    ```bash
    touch YYYY-MM-DD-your-post-title.md
    ```
1. Edit the file using your preferred text editor:
    ```bash
    nano YYYY-MM-DD-your-post-title.md
    ```
1. Add Front Matter: Each post requires a front matter block that defines metadata such as title, date, and layout. Example:
    ```yaml
    ---
    title: "Superplumes from the Core-Mantle Boundary to the Lithosphere: Implications for Heat Flux"
    date: 2014-06-17
    tags:
    []
    toc: true
    sidebar:
    nav: "all_posts_list"
    category: research-papers
    excerpt: "Superplumes from the Core-Mantle Boundary to the Lithosphere: Implications for Heat Flux"
    header:
    teaser: "/images/superplumes-from-the-core-mantle-boundary-to-the-lithosphere/QVplume.gif"
    ---
    ```
    - `title`: The title of your post.
    - `date`: The date of publication in YYYY-MM-DD format.
    - `tags`: A list of tags for categorizing the post (optional).
    - `toc`: Table of contents
    - `sidebar`: Specifies the sidebar navigation (e.g., nav: "all_posts_list").
    - `category`: The category the post belongs to (e.g., research-papers).
    - `excerpt`: A brief description or summary of the post.
    - `header`: Contains the teaser image path to be displayed at the top of the post.

1. Write your content using Markdown syntax. Here’s an example:
    ```markdown
    # Heading

    This is your content. You can write **bold text**, *italic text*, and more.

    ## Subheading

    Add images, links, and lists in Markdown.
    ```
1. Adding a Figure to a Post: To include a figure in your post, you can use HTML within your Markdown file. This is useful for customizing the size, alignment, and caption of the image.
    ```html
    <figure style="width: 350px; margin: 0 auto; text-align: center;">
    <img style="width: 100%" src="/images/theoretical_wave_propagation/Nact.gif">
    <figcaption><strong>Non-linear Asymptotic Coupling Theory</strong></figcaption>
    </figure>
    ```
    - <figure>: This tag wraps the image and the caption, allowing you to style the figure.
    - <img>: This tag includes the actual image. You can specify the width as a percentage to make the image responsive.
    - <figcaption>: This tag adds a caption below the image to describe it.
1. Save and exit the file.

## Writing and Editing Pages
In this Jekyll setup, pages are stored in the _pages directory, including specific subdirectories for different types of pages (e.g., members' profiles). Each page includes front matter that defines the permalink, classes, and other metadata like the author's name and GitHub profile.

### Structure of _pages Directory:
```bash
$ tree _pages/
_pages/
├── 404.md
├── members
│   ├── barbararomanowicz.md
│   ├── chaolyu.md
│   ├── jonathanwolf.md
│   ├── nicolasvalencia.md
│   └── utpalkumar.md
├── members.md
└── posts.md
```
- Each file in this directory represents a page or a category of pages. For example, member profile pages are stored under the _pages/members/ subdirectory.

### Steps to Create a New Page:
1. Navigate to the _pages directory:
    ```bash
    cd _pages
    ```
1. Create a new Markdown file for your page:
    ```bash
    touch new-page.md
    ```
1. Edit the file using your preferred text editor:
    ```bash
    nano new-page.md
    ```
1. Add Front Matter: Each page requires front matter to define metadata such as permalink, classes, GitHub link, and the author's name. For example:
    ```yaml
    ---
    permalink: "/new-page/"
    classes:
    - wide
    github: "https://github.com/example"
    author: "Author Name"
    ---
    ```
1. Write your content in Markdown:
    ```markdown
    # New Page Title

    This is the content of your new page. Use **Markdown** syntax to format your text, include images, or add links.
    ```
1. Save and exit the file.

## Adding Authors to the Blog
In this setup, authors are managed via the `_data/authors.yml` file, where each author’s information such as name, bio, avatar, and contact links is stored. This allows for a consistent display of author information across posts and pages.

### Steps to Add an Author:
1. Open the authors.yml file:
    ```bash
    nano _data/authors.yml
    ```
1. __Add a new author__ to the file by following the structure outlined below. Each author entry should contain their name, bio, avatar (image URL), and links (e.g., email). Here’s an example format:
    ```yml
    # /_data/authors.yml

    johnsmith:
    name: "John Smith"
    bio: "Research Scientist at Example Institute, specializing in geophysics and computational seismology."
    avatar: "https://example.com/images/johnsmith.jpg"
    links:
        - label: "Email"
        icon: "fas fa-fw fa-envelope-square"
        url: "mailto:john.smith@example.com"
        - label: "GitHub"
        icon: "fab fa-fw fa-github"
        url: "https://github.com/johnsmith"
    ```

1. Save and exit the file after making the necessary additions.

## Editing the `index.html` Page
The `index.html` file controls the content and layout of your website's homepage. The front matter at the top of the file defines the layout, author profile, classes, sidebar content, and GitHub link.

### Example Front Matter for index.html:
```yaml
---
layout: home
author_profile: false
classes:
  - landing
  - wide
sidebar:
  - image: "assets/images/barbara_romanowicz.jpg"
    text: "Prof. Barbara Romanowicz"
    subtext: "Professor of the Graduate School, Department of Earth and Planetary Science, UC Berkeley"
  - image: "images/semucb_wm1.png"
    nav: "all_posts_list"
    smalltext: "Whole-mantle depth cross-sections of relative shear-velocity variations in model SEMUCB-WM14, in the vicinity of major hotspots. [French et al., 2015]"
github: "https://github.com/bsl-group"
---
```
- `layout`: Specifies the layout used for the homepage.
- `author_profile`: Set to false to hide the author’s profile (Barbara's profile defined in `_config.yaml`) on the homepage.
- `classes`: Define additional CSS classes for customizing the homepage layout, such as landing or wide.
- `sidebar`: Configures the sidebar content, including images, text, and links to post lists or external sources.
- `github`: Adds a GitHub link to the homepage.

### Steps to Edit:
1. Open index.html in your preferred text editor:
    ```bash
    nano index.html
    ```
1. Modify the front matter fields as necessary to update the layout, sidebar content, or add new elements like text or images.
1. Save and exit after making your changes


## `_config.yml`
The `_config.yml` file in Jekyll is a configuration file that defines global settings for your site, such as the title, description, author information, theme options, and plugins. It allows you to customize various aspects of your site's behavior and appearance.

## Suggested reading for using Markdown
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax


