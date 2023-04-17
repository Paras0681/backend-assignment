
# Movie List Collection API
    This API is created so that user can register and create collections of movies.
    This collection can later be used which has title and some description regarding the movies in the collection
## Note Also added the Postman collection for the testcases of the requests.
- Register:
    - URL(POST): http://localhost:8000/register/

#### Note: All the below requests will require access token which we get from the above register request.

- All Movies:
    - URL(GET) : http://localhost:8000/movies/


- List of Collections:
    - URL(GET): http://localhost:8000/collection/
    - URL(POST): http://localhost:8000/collection/
      - request.data = {
            "title": "Horror movies",
            "description": "Kamjor dilwale naa dekhe..",
            "movies": [
                {
                    "title": "Robin Hood",
                    "description": "Yet another version of the classic epic, with enough variation to make it interesting.",
                    "genres": "Drama,Action,Romance",
                    "uuid": "73399935-2165-41f0-a6a4-1336ef5e5c20"
                },
                {
                    "title": "Caged Heat 3000",
                    "description": "It's the year 3000 AD. The world's most dangerous women are banished to a remote asteroid 45 million light years from earth.",
                    "genres": "Science Fiction",
                    "uuid": "129cf5d9-827c-4e42-843e-1f87ef99452f"
                },
                {
                    "title": "The Burkittsville 7",
                    "description": "A film archivist revisits the story of Rustin Parr, a hermit thought to have murdered seven children while under the possession of the Blair Witch.",
                    "genres": "Horror",
                    "uuid": "5e904ce8-91b7-42b4-84d9-5b53f4cb8c74"
                }
            ]
        }

    - URL(PUT): http://localhost:8000/collection/<slug:collection_uuid>
        - request.data = {
            "title": "Horror movies",
            "description": "Kamjor dilwale naa dekhe....",
            "movies": [
                {
                    "title": "Caged Heat 3000",
                    "description": "It's the year 3000 AD. The world's most dangerous women are banished to a remote asteroid 45 million light years from earth. Kira Murphy doesn't belong; wrongfully accused of a crime she did not commit, she's thrown in this interplanetary prison and left to her own defenses. But Kira's a fighter, and soon she finds herself in the middle of a female gang war; where everyone wants a piece of the action... and a piece of her! \"Caged Heat 3000\" takes the Women-in-Prison genre to a whole new level... and a whole new galaxy!",
                    "genres": "Science Fiction",
                    "uuid": "129cf5d9-827c-4e42-843e-1f87ef99452f"
                },
                {
                    "title": "The Burkittsville 7",
                    "description": "A film archivist revisits the story of Rustin Parr, a hermit thought to have murdered seven children while under the possession of the Blair Witch.",
                    "genres": "Horror",
                    "uuid": "5e904ce8-91b7-42b4-84d9-5b53f4cb8c74"
                }
            ]
        }

    - URL(DELETE): http://localhost:8000/collection/slug:collection_uuid
       - Deletes the collection having collection_uuid


- Collection List Detial
    - URL(GET): http://localhost:8000/<slug:collection_uuid>
        - Gets detail view for the collection


- MiddlewareView
    - URL(GET): http://localhost:8000/request-count/
        - Gets the request count made to the application
    - URL(POST): http://localhost:8000/request-count/reset/
        - Resest the request count made to the application


#### Optimization changes made
    - User is not created each and everytime for the register call
    - One migraiton file instead of multiple ones
    - Proper code documention, optimization and error handling

#### Bugs and suggestions found
    - Bugs:
        - Can create collection even if movies list given empty
        - Can remove all the movies in PUT request
        - Movie list is not properly evaluated
    -Suggestion:
        - Can create a new post request for login instead of giving in the register url
