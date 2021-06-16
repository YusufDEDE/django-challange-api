# Django Challange API

## Hello there, <br>
The REST API connects all the profiles it creates with the auth 'User' model with signals on the Django side.

https://django-challange-api.herokuapp.com

#### `POST /users/sign-up/`

Handles POST requests to create user accounts.

```json
{
    "username": "yusufdede",
    "first_name": "Yusuf",
    "last_name": "Dadayev",
    "password": "yusuf123qwe",
    "email": "yusufdadayev95@gmail.com.",
    "phone": "+905550011498", # not required
    "about_us": "I'm FIXER!!" # not required
}
```

#### `GET /users/me/`

Authenticates user with basic authentication and returns authenticated user's data.

````json
{
    "bio": [
        {
            "username": "yusufdede",
            "first_name": "Yusuf",
            "last_name": "Dadayev",
            "email": "yusufdadayev95@gmail.com",
            "phone": "+905550011498",
            "about_us": "I'm FIXER!!"
        }
    ]
}
````

#### `PUT /users/me`
````json
{
    "username": "yusufdede",
    "first_name": "Yusuf",
    "last_name": "Dede",
    "password": "yusuf123qwe",
    "email": "yusufdede95@hotmail.com",
    "phone": "5550011498",
    "about_us": "Test about us bla bla bla!..."
}
````

#### `GET /users/search?keyword=<keyword>`

Requires basic authentication and returns a list of users that match the keyword filter.

- `GET /users/search?keyword=u` request 
````json
{
    "search_result": [
        {
            "username": "linusx",
            "first_name": "Linus",
            "last_name": "Torvalds",
            "email": "linustorvalds@hotmail.com",
            "phone": "+902243267326",
            "about_us": "Please software communitiy! Go to OPEN SOURCE!!"
        },
        {
            "username": "yusufdede",
            "first_name": "Yusuf",
            "last_name": "Dadayev",
            "email": "yusufdadayev95@gmail.com",
            "phone": "+905550011498",
            "about_us": "I'm FIXER!!"
        }
    ]
}
````


