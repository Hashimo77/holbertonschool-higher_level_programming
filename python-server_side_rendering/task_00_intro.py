import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee details.
    """
    
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Create a copy of the template for this specific attendee
            content = template

            # List of expected placeholders based on the instructions
            placeholders = ["name", "event_title", "event_date", "event_location"]

            for key in placeholders:
                # Get value from dictionary. If key missing, return None.
                value = attendee.get(key)
                
                # Check if value is None or empty string, replace with "N/A"
                if value is None or value == "":
                    value = "N/A"
                
                # Replace the placeholder in the content
                # We use str(value) to ensure non-string types (if any) are converted
                content = content.replace("{" + key + "}", str(value))

            # 4. Generate Output Files
            output_filename = f"output_{index}.txt"
            
            # Check if file exists (optional based on hint, but usually 'w' overwrites)
            # Writing the file
            with open(output_filename, "w") as file:
                file.write(content)

        except Exception as e:
            # General error handling for unforeseen issues during processing
            print(f"An error occurred while processing output_{index}.txt: {e}")
