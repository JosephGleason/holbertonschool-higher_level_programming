#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        filled = template
        name = person.get("name", "N/A") or "N/A"
        title = person.get("event_title", "N/A") or "N/A"
        date = person.get("event_date", "N/A") or "N/A"
        location = person.get("event_location", "N/A") or "N/A"
        
        filled = filled.replace("{name}", name)
        filled = filled.replace("{event_title}", title)
        filled = filled.replace("{event_date}", date)
        filled = filled.replace("{event_location}", location)
        
        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as f:
            f.write(filled)