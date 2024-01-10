
import datetime
import json

def adjust_dates(input_json):
    data = json.loads(input_json)

    original = data["original"]
    change = data["change"]

    # Parse dates
    original_dates = {k: datetime.datetime.strptime(v, "%Y-%m-%d").date() for k, v in original.items()}
    changed_key, changed_date_string = list(change.items())[0]
    changed_date = datetime.datetime.strptime(changed_date_string, "%Y-%m-%d").date()

    # Update changed date
    original_dates[changed_key] = changed_date

    # Ensure changed date is not on a weekend
    while changed_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        changed_date += datetime.timedelta(days=1)
    if original_dates["project deadline"] == changed_date:
        changed_date -= datetime.timedelta(days=1)

    # Get eligible milestones
    milestone_keys = sorted([k for k in original if k.startswith('m')], key=lambda x: int(x[1:]))
    changed_milestone_index = milestone_keys.index(changed_key)
    eligible_milestones = milestone_keys[changed_milestone_index + 1:]

    # Recalculate deadline if necessary
    project_deadline = original_dates["project deadline"]
     # Copy
    new_dates = dict(original_dates) 
    # Assume will need to adjust at least once
    adjustment_made = True  

    while adjustment_made:
        adjustment_made = False
        next_date = changed_date
        days_apart = (project_deadline - changed_date).days / (len(eligible_milestones) + 1)

        for i, milestone in enumerate(eligible_milestones, start=1):
            next_date += datetime.timedelta(days=int(days_apart))

            # Skip weekends
            while next_date.weekday() >= 5:
                next_date += datetime.timedelta(days=1)

            # Ensure we aren't setting the date to the project deadline
            while next_date >= project_deadline:
                # Flag that we're moving the project deadline back
                adjustment_made = True  
                project_deadline += datetime.timedelta(days=1)
                next_date -= datetime.timedelta(days=int(days_apart))
                # Re-check for weekends
                while next_date.weekday() >= 5:  
                    next_date += datetime.timedelta(days=1)

            new_dates[milestone] = next_date
        
        # Reflect any changes
        new_dates["project deadline"] = project_deadline  

    # Format dates for output
    output_dates = {k: new_dates[k].strftime("%Y-%m-%d") for k in original_dates}
    data["original"] = output_dates
    return json.dumps(data)

input_json = '{"original": {"m1": "2023-10-02", "m2": "2023-10-06", "m3": "2023-10-12", "m4": "2023-10-18", "m5": "2023-10-24", "project deadline": "2023-10-30"}, "change": {"m2": "2023-10-23"}}'
print(adjust_dates(input_json))
