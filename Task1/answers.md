# Task 1

## Question

Say we are planning a feature in a project management web application that allows hobbyists to track their hobby projects. The feature is an in-app reminder for the hobbyist to complete the current task in their project before the task’s deadline. So far, we’ve confirmed the feature requirements with stakeholders, created diagrams and even wireframes. Next we want to plan the implementation of the feature. List the implementation steps that a software developer needs to take to implement the feature. By ‘step’ we mean some work that depends only on work done before it. For example: “write handler function for generating notification content” is a step because it only depends on input to the function.

## Answers

### Data Model Design

1. Define the data structure for storing project tasks, deadlines, and any relevant information.
2. Establish relationships between different entities, such as projects, tasks, and users.

### Database Schema Creation

3. Create the necessary database tables and fields to store project-related data.
4. Implement any required database migrations to update the existing schema.

### Integration with Task Creation:

5. Modify or extend the task creation functionality to include setting deadlines for tasks.
6. Ensure that the deadline information is stored in the database.

### User Interface Changes:

7. Update the user interface to display and allow users to set task deadlines within the project management application.
8. Integrate the deadline information into the task details view.

### Notification Service Integration:

9. Integrate a notification service or library that can handle in-app reminders.
10. Configure the service to trigger reminders based on task deadlines.

### Testing

11. Conduct unit tests for individual components such as data models, notification service, and scheduler.
12. Perform integration tests to ensure seamless interaction between different parts of the feature.

### Documentation

13. Update project documentation to include information about the new feature.
14. Provide guidelines for users on how to utilize the in-app reminder functionality.
