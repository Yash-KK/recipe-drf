# Recipe-DRF Application
### Technologies used: Django, Django Rest Framework, Docker.
<hr>
<br>

## Description
Recipe-DRF is a RESTful API built with Django and Django REST Framework (DRF) for managing recipes. It allows users to create, retrieve, update and delete recipes. Each recipe consists of a title, description, cooking time, price, link, tags, ingredients, and an optional image. Users can also filter recipes based on tags.

<br>

## Key Features
<ul>
  <li> <strong> User Authentication: </strong> Users can register, login, and authenticate to perform CRUD operations on recipes.</li>
  <li> <strong> Recipe Management:  </strong> Users can create new recipes, view existing recipes, update recipe details, and delete recipes.</li>
  <li> <strong> Tag and Ingredient Management:  </strong> Users can manage tags and ingredients associated with recipes.</li>
  <li> <strong> Image Upload:  </strong> Users can upload images for recipes using a separate API endpoint.</li>
  <li> <strong> Filtering: </strong> Recipes can be filtered based on tags, allowing users to find recipes with specific tags.</li>
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



## API
After successfull deployment of the image containers our backend is up and running on : [localhost:8000](http://127.0.0.1:8000/) <br>

<br>

The application generally supports all type of crud operations for an app:
<ul> 
  <li>
    View all existing recipes[GET]: <br>
    [http://127.0.0.1:8000/api/recipe/recipes/](http://127.0.0.1:8000/api/recipe/recipes/)
  </li>
  
   <li>
    View a particular recipe[GET]: <br>
    [http://127.0.0.1:8000/api/recipe/recipes/<recipe_id>/](http://127.0.0.1:8000/api/recipe/recipes/<recipe_id>/)
  </li>
</ul>
