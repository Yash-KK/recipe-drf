# Recipe-DRF Application
### Technologies used: Django, Django Rest Framework, Docker.
<hr>
<br>

## Description
Recipe-DRF is a RESTful API built with Django and Django REST Framework (DRF) for managing recipes. It allows users to create, retrieve, update and delete recipes. Each recipe consists of a title, description, cooking time, price, link, tags, ingredients, and an optional image. Users can also filter recipes based on tags.

<br>

## Key Features
<ul>
  <li> <strong> User Authentication: </strong> Users can register, login, and authenticate to perform CRUD operations on recipes.</li> <br>
  <li> <strong> Recipe Management:  </strong> Users can create new recipes, view existing recipes, update recipe details, and delete recipes.</li> <br>
  <li> <strong> Tag and Ingredient Management:  </strong> Users can manage tags and ingredients associated with recipes.</li> <br>
  <li> <strong> Image Upload:  </strong> Users can upload images for recipes using a separate API endpoint.</li> <br>
  <li> <strong> Filtering: </strong> Recipes can be filtered based on tags, allowing users to find recipes with specific tags.</li> <br>
</ul>

<br>

## Setup
<strong> Clone the git repository locally: </strong> <br>
```
git@github.com:Yash-KK/recepi-drf.git
```

<strong> Build and Run the Docker Container: </strong> <br>
```
sudo docker-compose up -d --build
```

<strong> Stopping a running container: </strong> <br>
```
sudo docker-compose stop
```

<strong> Removing the volumes and containers: </strong> <br>
```
sudo docker-compose down -v
```

<br>

## API
After successfull deployment of the image containers our backend is up and running on : <br>
* [localhost:8000](http://127.0.0.1:8000/) <br>

<br>

The application generally supports all type of crud operations for an app: <br>
* View all existing recipes[GET] and Create a new recipe instance[POST]: <br>
  [http://127.0.0.1:8000/api/recipe/recipes/](http://127.0.0.1:8000/api/recipe/recipes/)
  
* View a particular recipe[GET], Update[PUT/PATCH] and Delete[DELETE] : <br>
  [http://127.0.0.1:8000/api/recipe/recipes/<recipe_id>/](http://127.0.0.1:8000/api/recipe/recipes/<recipe_id>/)
  
For more information, visit: <br>
* [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

 <br>
 
 ## Debugging

<strong> To check running docker containers: </strong> <br>
 ```
 sudo docker container ls
 ```

<strong>To see all docker containers : </strong> <br>
```
sudo docker container ls -a
```

<strong>To view logs of a particular container while facing some issue: </strong>
```
sudo docker logs [container_id]
```

<br> 

## Testing

One can use clients like <strong> Thunder Cient </strong> extension in Vscode or <strong> Postman </strong> to test these API's
