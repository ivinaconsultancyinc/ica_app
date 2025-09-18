import os
# Path to your templates folder
templates= "Insurance_app/templates"
# Favicon link using Jinja2 syntax
favicon_link = ''
def update_html_files_with_favicon(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            # Check if favicon link already exists
            if favicon_link in content:
                continue
            # Insert favicon link into  section
            if "" in content:
                updated_content = content.replace("", f"\n    {favicon_link}")
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"Updated: {filename}")
            else:
                print(f"No  tag found in: {filename}")
# Run the update function
update_html_files_with_favicon(templates) 


