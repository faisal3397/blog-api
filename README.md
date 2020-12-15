# Blog API

## Introduction
This project is the final project in the Full-Stack Nanodegree which is presented by Udacity.
The main idea behind this project is to provide a Blog API, which allows the user to create, delete and edit posts.

The API has two kind of users:
 - Blog Owner, the one who's able to create, edit, and delete posts.
 - Authenticated User, the one who's able to view posts, and comment on them.

## Getting Started
- Base URL:  `https://blog-api-fsnd.herokuapp.com/`.

> Note: The API is hosted at Heroku, if you want to test the API you can just import the provided Postman collection and run it.

>If you want to run the development server, then you need to follow along with steps provided below.
### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/blog-api` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the database. You'll primarily work in app.py and can reference models.py. 



## Database Setup
With Postgres running, restore a database using the blog.psql file provided. From the `/blog-api` folder in terminal run:
```bash
psql blog < blog.psql
```

## Running the server

From within the `/src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 


## Testing
To run the tests, navigate to `/blog-api` directory in the terminal and run:
```
source setup.sh
dropdb blog_test
createdb blog_test
psql blog_test < blog.psql
python3 test_app.py
```

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "error": 404,
  "message": "Not found",
  "success": false
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Not Found
- 422: Unprocessable Entity
- 401: Unauthorized

## Endpoints

- ### GET /posts
    - General:
        - Returns an array that contains available posts.
        - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
        
    - Auth: None
    
    - Sample: `curl GET https://blog-api-fsnd.herokuapp.com/posts?page=1`
    
    
       {
            "posts": [
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "date": "Tue, 15 Dec 2020 08:04:58 GMT",
                    "id": 2,
                    "title": "My New Post 2"
                },
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "date": "Tue, 15 Dec 2020 08:05:58 GMT",
                    "id": 3,
                    "title": "My New Post 3"
                },
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "date": "Tue, 15 Dec 2020 08:06:58 GMT",
                    "id": 4,
                    "title": "My New Post 4"
                },
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "date": "Tue, 15 Dec 2020 08:07:58 GMT",
                    "id": 5,
                    "title": "My New Post 5"
                },
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "date": "Tue, 15 Dec 2020 08:08:58 GMT",
                    "id": 7,
                    "title": "My New Post 6"
                },
                {
                    "content": "Modified content 1232341242",
                    "date": "Tue, 08 Dec 2020 16:53:58 GMT",
                    "id": 1,
                    "title": "Modified title 123"
                }
            ],
            "success": true,
            "total_posts": 6
        }
        

    
- ### GET /posts/{id}/comments
    - General:
        - Returns an array that contains available comments for the requested post.
        
    - Auth: None
    - Sample: `curl GET https://blog-api-fsnd.herokuapp.com/posts/1/comments`  


    {
        "comments": [
            {
                "content": "Hi your post #1 is great",
                "date": "Tue, 08 Dec 2020 16:02:48 GMT",
                "id": 1,
                "post_id": 1
            },
            {
                "content": "I don't really agree with your post",
                "date": "Tue, 15 Dec 2020 08:07:48 GMT",
                "id": 2,
                "post_id": 1
            },
            {
                "content": "That info was so useful, thanks a lot and keep up the good work",
                "date": "Tue, 15 Dec 2020 08:07:48 GMT",
                "id": 3,
                "post_id": 1
            },
            {
                "content": "That info was so useful, thanks a lot and keep up the good work",
                "date": "Tue, 15 Dec 2020 08:07:48 GMT",
                "id": 4,
                "post_id": 1
            },
            {
                "content": "Hi your post #1 is great",
                "date": "Tue, 08 Dec 2020 16:02:48 GMT",
                "id": 5,
                "post_id": 1
            }
        ],
        "success": true
    }
   
- ### POST /posts
    - General:
        - Creates a Post, the user needs to provide an object that contains the title, the date, and content.
    - Auth: Requires Blog Owner's Token.
    
    - Sample: `curl -d '{"title": "My New Post 6","date": "Tue, 15 Dec 2020 08:08:58 GMT","content": "Lorem ipsum dolor sit amet"}' -H "Content-Type: application/json"  -H "Authorization: Bearer {token}" -X POST https://blog-api-fsnd.herokuapp.com/posts`
    
    
    {
        "post": {
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "date": "Tue, 15 Dec 2020 08:08:58 GMT",
            "id": 8,
            "title": "My New Post 6"
        },
        "success": true
    }

- ### POST /posts/{id}/comments
    - General:
        - Creates a Comment related to the requested post, the user needs to provide an object that contains the date, and content.
    - Auth: Requires Blog Owner's Token, or Authenticated User's Token.
    
    - Sample: `curl -d '{"content": "Hi your post #1 is great","date": "Tue, 08 Dec 2020 16:02:48 GMT"}' -H "Content-Type: application/json"  -H "Authorization: Bearer {token}" -X POST https://blog-api-fsnd.herokuapp.com/posts/1/comments`
    
    
    {
        "comment": {
            "content": "Hi your post #1 is great",
            "date": "Tue, 08 Dec 2020 16:02:48 GMT",
            "id": 6,
            "post_id": 1
        },
        "success": true
    }

- ### PATCH /posts/{id}
    - General:
        - Modifies a Post, the user needs to provide a post id in the url and an object that contains the post with the modified fields in the request's body.
    - Auth: Requires Blog Owner's Token.
    
    - Sample: `curl -d '{"title": "Modified title 123","date": "Tue, 08 Dec 2020 16:53:58 GMT","content": "Modified content 1232341242"}' -H "Content-Type: application/json"  -H "Authorization: Bearer {token}" -X PATCH https://blog-api-fsnd.herokuapp.com/posts/1`
    
    
    {
        "post": {
            "content": "Modified content 1232341242",
            "date": "Tue, 08 Dec 2020 16:53:58 GMT",
            "id": 1,
            "title": "Modified title 123"
        },
        "success": true
    }

- ### DELETE /posts/{id}
    - General:
        - Deletes a Post, the user needs to provide a post id in the url.
    - Auth: Requires Blog Owner's Token.
    
    - Sample: `curl -H "Content-Type: application/json"  -H "Authorization: Bearer {token}" DELETE https://blog-api-fsnd.herokuapp.com/posts/1`
    
    
    {
        "delete": 7,
        "success": true
    }
