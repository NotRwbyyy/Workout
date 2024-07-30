import webbrowser
from datetime import datetime
from jinja2 import Template

# Define the workout schedule with exercises
schedule = {
    0: ("Chest/Triceps", [
        "Bench Press: 3 x 10",
        "Incline Dumbbell Press: 3 x 10",
        "Tricep Dips: 3 x 10",
        "Tricep Pushdown: 3 x 10",
        "Skullcrushers: 3 x 10",
        "Calf Raises: 3 x 10",
        "Ab Crunches: 3 x 20"
    ]),
    1: ("Back/Biceps", [
        "Pull-Ups: 3 x 10",
        "Bent Over Row: 3 x 10",
        "Bicep Curls: 3 x 10",
        "Hammer Curls: 3 x 10",
        "Barbell Rows: 3 x 10",
        "Dumbbell Rows: 3 x 10",
        "Calf Raises: 3 x 10",
        "Ab Crunches: 3 x 20",
        "Hip Abductors: 3 x 10"
    ]),
    2: ("Abs/Legs", [
        "Barbell Squats: 3 x 10",
        "Front Barbell Squats: 3 x 10",
        "Bulgarian Dumbbell split squats: 3 x 10",
        "Leg Press: 3 x 10",
        "Leg Extensions: 3 x 10",
        "Ab Crunches: 3 x 20",
        "Plank: 3 x 1 minute"
        "Calf Raises: 3 x 10",
        "Hip Abductors: 3 x 10"
    ]),
    3: ("Chest/Triceps", [
        "Decline Dumbbell Bench Press: 3 x 10",
        "Incline Dumbbell Press: 3 x 10",
        "Shoulder press: 3 x 10",
        "Lat Raises: 3 x 10",
        "Dumbbell Flys: 3 x 10",
        "Dips: 3 x 20"
    ]),
    4: ("Back/Biceps", [
        "Pull-Ups: 3 x 10",
        "Lat Pulldowns: 3 x 10",
        "Preacher Curls: 3 x 10",
        "Zotman Curls: 3 x 10",
        "Barbell Curls: 7 x 7", 
    ]),
    5: ("Abs/Legs", [
        "Box Jumps: 3 x 10",
        "Lunges: 3 x 10",
        "Leg Press: 3 x 10",
        "Plank: 3 x 1 minute"
        "Calf Raises: 3 x 10",
        "Hip Abductors: 3 x 10",
        "Side planks: 3 x 30 seconds",
        "Candle Sticks: 3 x 12",
        "Dead Cockroach: 3 x 30 seconds"
    ]),
    6: ("Rest day!", [])
}

# Get the current day of the week
current_day = datetime.today().weekday()
workout, exercises = schedule.get(current_day, ("Rest day!", []))

# Read the HTML template
with open('dailyworkout.html', 'r') as file:
    html_template = file.read()

# Create a Jinja2 template from the HTML
template = Template(html_template)

# Render the HTML content with actual values
html_content = template.render(day=datetime.today().strftime('%A'), workout=workout, exercises=exercises)

# Write the updated HTML content to a new file
with open('dailyworkout.html', 'w') as file:
    file.write(html_content)

# Open the new HTML file in the default web browser
webbrowser.open_new_tab('dailyworkout.html')
