## (a) Process

1. Load the input JSON into a Python dictionary.
2. Extract the "original" and "change" sub-dictionaries.
3. Parse the "change" dictionary to get the changed milestone key (e.g. "m2") and the new date.
4. Parse all the milestone dates into datetime date objects.
5. Update the changed milestone date in the parsed dates.
6. Sort the milestones after the changed one into eligible milestones list.
7. Calculate spacing between eligible milestones based on project deadline.
8. Loop through eligible milestones.
9. Calculate target date based on spacing.
10. Skip weekends by adding days until not Sat/Sun.
11. Handle project deadline conflicts by incrementing deadline.
12. Convert dates back to strings.
13. Update original dict with updated dates.
14. Serialize back to JSON.
15. Return updated JSON.

## (b) Rules Implemented

- Only update milestones after the changed one (eligible milestones).
- Space eligible milestones evenly between changed one and deadline.
- Skip weekends when adjusting dates.
- Increment deadline if it conflicts after adjustment.
- Recalculate deadline if necessary
- Make minimum adjustment needed to deadline.
