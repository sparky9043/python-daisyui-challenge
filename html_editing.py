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
        
    updated_html = html_base
    
    # Write index.html file after updating with Python
    with open(html_output, "w") as file:
        file.write(updated_html)
    
create_website("./template.html", "./index.html")