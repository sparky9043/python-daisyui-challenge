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
    
    # Helper function to add element before body tag and return modified_html
    def add_to_body(modified_html, element_to_add):
        modified_html = modified_html.replace("</body>", f"{element_to_add}</body>")
        return modified_html
    
    # Apply Theme
    data_theme = "halloween"
    modified_html = modified_html.replace('<html lang="en">',
                                          f'<html lang="en" data-theme="{data_theme}">')
    
    # Add Title to Body
    h1_tag = "<h1>Welcome to My Website</h1>"
    modified_html = add_to_body(modified_html, h1_tag)

    # Add Card to HTML
    card = """
    <div class="card bg-base-100 w-96 shadow-sm">
    <figure>
        <img
        src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
        alt="Shoes" />
    </figure>
    <div class="card-body">
        <h2 class="card-title">Card Title</h2>
        <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
        <div class="card-actions justify-end">
        <button class="btn btn-primary">Buy Now</button>
        </div>
    </div>
    </div>
    """
    modified_html = add_to_body(modified_html, card)
    
    # Write index.html file after updating with Python
    with open(html_output, "w") as file:
        file.write(modified_html)
    
create_website("./template.html", "./index.html")