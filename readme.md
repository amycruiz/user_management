

# The User Management System Final Project: Your Epic Coding Adventure Awaits! 🎉✨🔥

## Reflection Document: User Profile Management Feature Implementation

In this assignment I worked incredibly hard to implement the **User Profile Management** feature. This feature allows administrators to upgrade users to a professional status and send congratulatory emails to users upon their promotion. Additionally, I integrated error handling to address potential issues, such as SMTP failures, by adding try-catch blocks in certain test cases that would raise such errors. Overall, this document reflects on the challenges I faced, the learning I gained, and how the feature evolved.

### **New Feature Implementation: User Profile Management**

To implement this feature, I modified multiple files in the project:
1. **`user_model.py`**: I added a location field and implemented validation for the `is_professional` field.
2. **`user_schemas.py`**: I updated the user schema to support the new fields.
3. **`user_service.py`**: I created methods to handle user upgrades and send email notifications.
4. **`user_routes.py`**: I added an endpoint to allow admins to upgrade users.

As mentioned previously, my feature ensures that only authorized users (admins) can make the upgrades and incorporates a layer of error handling for SMTP failures, a crucial step for maintaining system robustness. Keep in mind, I also modified my tests files but they're all metioned below in my **Testing my User Profile Management Feature** section.

### **Challenges and Solutions**

While working on this feature, I encountered several challenges:

- **Handling Permissions**: Ensuring that only admins could perform the upgrade was a critical step. I used role-based checks within the `upgrade_to_professional` method to validate permissions before performing the upgrade.
- **Email Notifications**: Setting up email notifications posed its own set of challenges, particularly with dealing with SMTP failures. I used a try-catch block to gracefully handle email sending errors, ensuring that the feature would still function even if the email service encountered an issue.
- **Testing**: Writing tests to cover all edge cases was both challenging and rewarding. It was essential to test for various scenarios, including successful upgrades, permission-denied scenarios, and failures like attempting to upgrade a non-existent user. Each test case had to ensure the accuracy of the logic and the behavior of the system in real-world scenarios.

The most significant challenge was debugging the errors that arose from testing email failures. I had to modify my email service and test cases multiple times before achieving the desired behavior. By focusing on modular testing and breaking down the problem into smaller steps, I was able to resolve the issues effectively.

### **Testing my User Profile Management Feature**

Here are the 10 test cases I wrote to ensure my feature was functional and reliable:

#### **User Service Tests (4 test cases)**

1. **test_upgrade_to_professional_success**: Verifies that a user is successfully upgraded to professional status.
2. **test_upgrade_to_professional_user_not_found**: Ensures that a non-existent user cannot be upgraded.
3. **test_upgrade_to_professional_user_already_professional**: Checks that a user already marked as professional is not upgraded again.
4. **test_upgrade_to_professional_email_service_failure**: Simulates an email failure during the upgrade process and verifies error handling.

#### **Email Service Tests (2 test cases)**

1. **test_send_professional_upgrade_email**: Verifies that the email notification for professional upgrades is successfully sent.
2. **test_email_service_error_handling**: Tests that the email service can gracefully handle SMTP failures.

#### **User Model Tests (2 test cases)**

1. **test_location_field**: Validates that the location field is properly stored and retrieved.
2. **test_is_professional_validation**: Ensures the `is_professional` field only accepts boolean values.

#### **API Tests (2 test cases)**

1. **test_upgrade_to_professional_success**: Verifies the successful API response when upgrading a user to professional status.
2. **test_upgrade_to_professional_permission_denied**: Ensures that users without the correct permissions cannot upgrade a user's status.

### **DockerHub Deployment**
If my project deploys successfully on dockerhub when I merge my user-profile-management branch with my main, I will add an image in replacement of this text. 

You can view my DockerHub repository [here](https://hub.docker.com/repository/docker/amycruiz/project2/general).

### **Conclusion**

This project was a tremendous learning experience and was by no means easy to complete. There were many times I felt as though I wasn't capable of completing it, but in the end, it all worked out. I truly put my all into it, and although I am certainly no coder, I am proud of the way I got my feature to work and the test cases I created for it. It all deepened my understanding of building robust features, handling errors gracefully, and ensuring the system is reliable through comprehensive testing. The biggest takeaway was the importance of not giving up and taking a bit of time off from coding, then coming back the next day when things are less stressful. Ultimately, by successfully implementing the ***User Profile Management*** feature, adding relevant tests, and deploying my project to DockerHub, I was able to demonstrate both my technical and problem-solving skills in a real-world scenario.

## Introduction: Buckle Up for the Ride of a Lifetime 🚀🎬

Welcome to the User Management System project! 🏫👨‍🏫⭐ This project is your gateway to coding glory, providing a bulletproof foundation for a user management system that will blow your mind! 🤯 You'll bridge the gap between the realms of seasoned software pros and aspiring student developers like yourselves. 

### [Instructor Video - Project Overview and Tips](https://youtu.be/gairLNAp6mA) 🎥

- [Introduction to the system features and overview of the project - please read](system_documentation.md) 📚
- [Project Setup Instructions](setup.md) ⚒️
- [Features to Select From](features.md) 🛠️
- [About the Project](about.md)🔥🌟

## Goals and Objectives: Unlock Your Coding Superpowers 🎯🏆🌟

Get ready to ascend to new heights with this legendary project:

1. **Practical Experience**: Dive headfirst into a real-world codebase, collaborate with your teammates, and contribute to an open-source project like a seasoned pro! 💻👩‍💻🔥
2. **Quality Assurance**: Develop ninja-level skills in identifying and resolving bugs, ensuring your code quality and reliability are out of this world. 🐞🔍⚡
3. **Test Coverage**: Write additional tests to cover edge cases, error scenarios, and important functionalities - leave no stone unturned and no bug left behind! ✅🧪🕵️‍♂️
4. **Feature Implementation**: Implement a brand new, mind-blowing feature and make your epic mark on the project, following best practices for coding, testing, and documentation like a true artisan. ✨🚀🎆
5. **Collaboration**: Foster teamwork and collaboration through code reviews, issue tracking, and adhering to contribution guidelines - teamwork makes the dream work, and together you'll conquer worlds! 🤝💪🌍
6. **Industry Readiness**: Prepare for the software industry by working on a project that simulates real-world development scenarios - level up your skills to super hero status  and become an unstoppable coding force! 🔝🚀🏆⚡

## Managing the Project Workload: Stay Focused, Stay Victorious ⏱️🧠⚡

This project requires effective time management and a well-planned strategy, but fear not - you've got this! Follow these steps to ensure a successful (and sane!) project outcome:

1. **Select a Feature**: [Choose a feature](features.md) from the provided list of additional improvements that sparks your interest and aligns with your goals like a laser beam. ✨⭐🎯 This is your chance to shine!

2. **Test Coverage Improvement**: Review the existing test suite and identify gaps in test coverage like a pro. Create 10 additional tests to cover edge cases, error scenarios, and important functionalities related to your chosen feature. Focus on areas such as user registration, login, authorization, and database interactions. Simulate the setup of the system as the admin user, then creating users, and updating user accounts - leave no stone unturned, no bug left behind! ✅🧪🔍🔬 Become the master of testing!

3. **New Feature Implementation**: Implement your chosen feature, following the project's coding practices and architecture like a coding ninja. Write appropriate tests to ensure your new feature is functional and reliable like a rock. Document the new feature, including its usage, configuration, and any necessary migrations - future you will thank you profusely! 🚀✨📝👩‍💻⚡ Make your mark on this project!

4. **Maintain a Working Main Branch**: Throughout the project, ensure you always have a working main branch deploying to Docker like a well-oiled machine. This will prevent any last-minute headaches and ensure a smooth submission process - no tears allowed, only triumphs! 😊🚢⚓ Stay focused, stay victorious!

## Commands

1. Start and build a multi-container application:

```
docker compose up --build
```

2. Goto http://localhost/docs to view openapi spec documentation

Click "authorize" input username: `admin@example.com` password: `secret`

3. Goto http://localhost:5050 to connect and manage the database.

The following information must match the ones in the `docker-compose.yml` file.

Login:

- Email address / Username: `admin@example.com`
- Password: `adminpassword`

When add new server:

- Host name/address: `postgres`
- Port: `5432`
- Maintenance database: `myappdb`
- Username: `user`
- Password: `password`

## Optional Commands

### Run `pytest` inside the containers:

Run all tests:

```
docker compose exec fastapi pytest
```

Run a single test:

```
docker compose exec fastapi pytest tests/test_services/test_user_service.py::test_list_users
```

### Creating database migration:

```
docker compose exec fastapi alembic revision --autogenerate -m 'added admin'
```


### Apply database migrations:

```
docker compose exec fastapi alembic upgrade head
```


## Submission and Grading: Your Chance to Shine 📝✏️📈

1. **Reflection Document**: Write a document file (`.md` file, at least 400 words) reflecting on your learnings throughout the course and your experience working on this epic project. Include **10 NEW tests, and 1 Feature** you'll be graded on. Make sure your project successfully deploys to DockerHub and include a link to your Docker repository in the document - let your work speak for itself! 📄🔗💥

2. **Commit History**: Show off your consistent hard work through your commit history like a true coding warrior. **Projects with less than 10 commits will get an automatic 0 - ouch!** 😬⚠️ A significant part of your project's evaluation will be based on your use of issues, commits, and following a professional development process like a boss - prove your coding prowess! 💻🔄🔥

3. **Deployability**: Broken projects that don't deploy to Dockerhub or pass all the automated tests on GitHub actions will face point deductions - nobody likes a buggy app! 🐞☠️ Show the world your flawless coding skills!

### Grading Rubric: (100 Points)

#### 1. Reflection Document (20 Points)

- 10 Points: Quality and completeness of the reflection document, including insights into learnings, challenges faced, and how they were overcome. Must meet the minimum word count (400 words).
- 5 Points: Clear and detailed description of the new feature implemented, including its purpose, usage, and configuration.
- 5 Points: Inclusion of DockerHub deployment link and evidence of successful deployment.

#### 2. Commit History and Professional Development Process (20 Points)

- 20 Points: Consistent commit history with meaningful commit messages. Projects with fewer than 10 commits receive 0 points in this category.


#### 3. Test Coverage and Quality Assurance (30 Points)

- 15 Points: Quality and thoroughness of 10 new test cases, covering edge cases, error scenarios, and critical functionalities.
- 10 Points: New test cases must integrate well with the existing test suite and pass on GitHub Actions.
- 5 Points: Tests demonstrate creativity and critical thinking, ensuring robust quality assurance for both existing and new features.

#### 4. New Feature Implementation (30 Points)

- 15 Points: Functionality and reliability of the new feature, including adherence to project coding standards and architecture.
- 10 Points: Tests written for the new feature ensure it works as intended and handles edge cases.
- 5 Points: Documentation of the new feature, including its purpose, configuration, and any necessary migrations.

#### 5. Deployability (20 Points)

- 10 Points: Working deployment to DockerHub, with no critical issues or broken functionalities.
- 10 Points: Maintains a clean and functional main branch throughout the project lifecycle.

### Notes:

This is our final assignment. You have two weeks to complete it, and late submissions will not be accepted.

Remember, it's more important to make something work reliably and be reasonably complete than to implement an overly complex feature. Focus on creating a feature that you can build upon or demonstrate in an interview setting - show off your skills like a rockstar! 💪🚀🎓

Don't forget to always have a working main branch deploying to Docker at all times. If you always have a working main branch, you will never be in jeopardy of receiving a very disappointing grade :-). Keep that main branch shining bright!

Let's embark on this epic coding adventure together and conquer the world of software engineering! You've got this, coding rockstars! 🚀🌟✨
