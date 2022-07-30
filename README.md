# Team-management-app

The project folder structure contains two apps: teammanagement/ and base/

teammanagement coontains the general setup of the project, whereas base/ contains the app with the functionality for Team management application.


### base/models.py:
This file contains the database that stores each user in the database management app. The data gets pulled from this database and is displayed on the client side.

param Models.model : model

I am using Member model to store the data: <br/>

first_name: stores first name of the user <br/>
last_name: stores last name of the user <br/>
email: stores the users email address <br/>
phone: stores the users phone number

### base/urls.py:
This file contains the url routing for the base application section of teammanagement app.

its consists of a list of url routes: <br/>

'' : base path that displays the MemberList (ListView) <br/>
'member/<int:pk>/' : displays MemberDetail (DetailView) and uses member.id as a int parameter <br/>
'member-create/' : displays MemberCreate (CreateView) <br/>
'member-update/<int:pk>/' : displays MemberUpdate (UpdateView) and uses member.id as a int parameter <br/>
'member-delete/<int:pk>/' : displays DeleteView and uses member.id as a int parameter <br/>

### base/views.py:
This file contains the views that display a response according to the url request mentioned in the urls.py file

It consists of multiple views:

#### class MemberList
param ListView : View

uses class-based and the member model to return members from database

#### class MemberDetail
param DetailView : View

uses class-based and member view to return each member

#### class MemberCreate
param CreateView : View

uses class-based and create view to create a new member

#### class MemberUpdate
param UpdateView : View

uses class-based view and update view to update a member with specific id

#### class DeleteView
param DeleteView : View

uses class-based and delete view to delete a member with specific id

### base/templates/base:
consists of all the html code to display content from each view. Each view is selected according to the url routing mentioned in urls.py



