from django.db import models
import datetime

# Create your models here.
class Emp(models.Model):
    emp_name = models.TextField()
    emp_email = models.EmailField()
    emp_mobile = models.TextField()

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.TextField()
    title = models.TextField()
    creator = models.TextField()
    created_at = models.DateField(default=datetime.date.today)

class Issues(models.Model):
    id = models.IntegerField(primary_key=True)   
    type = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    project = models.TextField()
    reporter = models.TextField()
    assignee = models.TextField()
    status = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
    closed_at = models.DateField()
    comment = models.TextField()
    watcher = models.TextField()
    label = models.TimeField()

    







# a. Getting a list of all issues and subsequent assignee, reporter.

# b. Getting a list of all projects and subsequent issues with the assignee and reporter.

# c. Getting issues with ID, title, or description as argument.

# d. Getting a project with ID, or name.

# e. Getting issue with title. (If multiple issues share same title return multiple)

# Add APIs to create a new issue or update an existing issue by its ID.

# Make sure update/create operations adhere to above mentioned functional requirements, like:

# Issue's reporter cannot be changed.

# a. Creating new issues.

# b. Updating existing issues. (Change title, description, or name)

# c. Create a project.

# d. Create an issue under a project by using project id or project name (both options to be implemented)