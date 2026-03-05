def create_website(template_file, html_output):
    """Function that reads the contents of a template html file
    dynamically update its content, and outputs into an index.html file

    Args:
        template_file (string): path to the template.html file
        html_output (string): path to the index.html file
    """
    
    # Read template.html file and store boilerplate code
    html_base = ""
    with open(template_file, "r") as website:
        html_base = website.read()

    # Update Title
    new_title = "My Website"
    modified_html = html_base.replace("<title>Document", f"<title>{new_title}")
    
    # Implement DaisyUI
    daisy_ui = """
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
    """
    
    modified_html = modified_html.replace("</head>", f"{daisy_ui}</head>")
    
    # Apply Theme
    data_theme = "halloween"
    modified_html = modified_html.replace('<html lang="en">',
                                          f'<html lang="en" data-theme="{data_theme}">')
    
    # Add Title to Body
    h1_tag = "<h1>Welcome to My Website</h1>"
    modified_html = modified_html.replace("</body>", f"{h1_tag}</body>")

    
    # Write index.html file after updating with Python
    with open(html_output, "w") as file:
        file.write(modified_html)
    
create_website("./template.html", "./index.html")