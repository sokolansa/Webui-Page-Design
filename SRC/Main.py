import os

# 1. Run the webui
# 2. 

def create_project_folder(folder_name):
    """
    Creates a project folder with the specified name and initializes an index.html file 
    with a properly indented structure, along with CSS and JS subdirectories.
    
    :param folder_name:
    """
    base_path = os.path.abspath(folder_name)
    subfolders = ["CSS", "JS"]

    try:
        # Create the main folder
        os.makedirs(base_path, exist_ok=True)
        
        # Create subfolders
        for subfolder in subfolders:
            os.makedirs(os.path.join(base_path, subfolder), exist_ok=True)
        
        # Create the index.html file with a formatted structure
        html_path = os.path.join(base_path, "index.html")
        if not os.path.exists(html_path):
            with open(html_path, 'w') as file:
                file.write("""<!DOCTYPE html>
<html>
<head>
    <title>Project</title>
</head>
<body>
    
</body>
</html>""")
        
        print(f"Project folder '{folder_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_web_element(folder_name, element_type, content=""):
    """
    Adds a given type of web element to the <body> section of the index.html file.
    
    :param folder_name: The name of the folder containing index.html.
    :param element_type: The type of web element to insert (e.g., 'button', 'input', 'div').
    :param content: The content or attributes to include inside the web element.
    """
    html_path = os.path.join(folder_name, "index.html")
    
    try:
        if not os.path.exists(html_path):
            raise FileNotFoundError(f"No index.html file found in {folder_name}.")
        
        # Read the existing content of the file
        with open(html_path, "r") as file:
            lines = file.readlines()
        
        # Locate the <body> tag and insert the new element
        for i, line in enumerate(lines):
            if "<body>" in line:
                indent = "    "  # Four spaces for indentation
                if element_type.lower() in {"input", "img"}:  # Self-closing tags
                    element = f"{indent*2}<{element_type} {content.strip()} />\n"
                else:
                    element = f"{indent*2}<{element_type}>{content}</{element_type}>\n"
                lines.insert(i + 1, element)
                break
        
        # Write the updated content back to the file
        with open(html_path, "w") as file:
            file.writelines(lines)
        
        print(f"Added <{element_type}> element to index.html inside <body>.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
create_project_folder("MyWebsite")  # First, create the project structure
add_web_element("MyWebsite", "button", "Click Me!")  # Adds a <button> element
add_web_element("MyWebsite", "input", 'type="text" placeholder="Enter text"')  # Adds an <input> element
add_web_element("MyWebsite", "div", "Hello World!")  # Adds a <div> element