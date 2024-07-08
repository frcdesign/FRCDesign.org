import yaml
import os

new_properties = {'repository': 'davidsdesignserver/FRCDesign.org', 'token': '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', 'enabled': True}

# Load the base configuration
with open('mkdocs.base.yml', 'r') as file:
    config = yaml.safe_load(file)

# Function to add or update properties
def update_plugin_properties(plugins, plugin_name, new_properties):
    for item in plugins:
        if isinstance(item, dict) and plugin_name in item:
            item[plugin_name].update(new_properties)
            break
    else:
        # Plugin not found, add new dictionary with the properties
        plugins.append({plugin_name: new_properties})

# Check the branch name (you might get this from environment variables or other methods)
branch = os.getenv('GIT_BRANCH', 'main')


# Add plugins based on the branch
if branch == 'main':
    # Ensure 'plugins' is a list in the config
    if 'plugins' not in config:
        config['plugins'] = []
    
    # Add the specific plugin for the main branch
    update_plugin_properties(config['plugins'], 'git-committers', new_properties)  # Replace with the actual plugin


# Write the modified configuration to mkdocs.yml
with open('mkdocs.yml', 'w') as file:
    yaml.safe_dump(config, file)

print(config)
print(f"Generated mkdocs.yml for branch: {branch}")
print(os.getenv('GITHUB_REF'))
