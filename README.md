# Code for good
Code for good is a crowdfunding app, meant to support IT projects that matter. Anyone interested in them can support them either by donating maney or time coding along with others. 
Status: Finished all CRUD operations, except updating and deleting TimeDonations. 
## Deployed to Heroku: 
[Heroku app](https://quiet-hamlet-41512.herokuapp.com)

## MVP features
MVP
1. Sing up/login (auth)
2. See the list of projects
3. See a project, update and delete
4. See the list of pledges
5. See a pledge, update and delete
6. Donate time, see all time donations
7. Each project has a category
8. Show total of pledges

## Additional features (under way)
1. Send messages 
2. Show if a project has gained a desirable level of money/hours support
3. Promote projects

## Endpoints

[Get all projects](https://quiet-hamlet-41512.herokuapp.com/projects/)
![Screenshot from Insomnia](get_projects.png)

Request body to create a new project:
```
{
        "title": "Project 99",
	      "categories": [
        "health"
         ],
        "description": "The 99 project.",
        "goal": 150,
        "image": "https://via.placeholder.com/300.jpg",
	      "date_created": "2020-09-20T14:28:23.382748Z",
        "is_open": true
        
        
    }
```

![Screenshot from Insomnia](/Screenshots/create_a_projects.png)

Post a pledge
Request to create a new pledge: 
```
{
   "amount": 14,
  "comment": "Love this project!",
  "anonymous": false,
   "project_id": 2
}
```
![Screenshot from Insomnia](/Screenshots/create_a_pledge.png)

Projects with pledges
![Screenshot from Insomnia](/Screenshots/projects_with_pledges.png)

Get all pledges
[Get all pledges](https://quiet-hamlet-41512.herokuapp.com/pledges/)

Sing up/ login (https://quiet-hamlet-41512.herokuapp.com/users/)
![Screenshot from Insomnia](/Screenshots/unauth_request.png)

Request to create a new user:
```
{
  "username": "This field is required.",
  "email": "This field is required.",
  "password": "This field is required."
}
```
Get timedonation 
https://quiet-hamlet-41512.herokuapp.com/timedonation/
At the moment throws 500 error - to be fixed. 


## API specification
![Screenshot](api2.png)
