# RightSpot
Right Spot is an app that helps you find the perfect location for your start-up by compiling useful information from a variety of sources, all in one place. We currently use data from Google Places API and a hand-picked dataset derived from 8 different ONS (Office for National Statistics, UK) surveys to display the information for each location.

## This Repository
This ‘RightSpot’ repository is a team effort, built by [Andy](https://github.com/andy-ag) and myself in 6 days. We built this website as the third of four projects for the Software Engineering Immersive course from [General Assembly](https://generalassemb.ly/).

This website is a full stack app built with the Python based Django web framework. It consists of four apps for each distinct feature:
- RightSpot: Default app with basic files and settings needed for any Django web application.
- main_app: Responsible for rendering the web pages and handling user requests. Communicates with the other two apps using RESTful API calls.
- location_services: Provides an internal API layer for using various external APIs for location data, including Google Maps and What3Words. 
- data: Provides another internal API layer to retrieve ONS data for a given district. This data was collected and processed in Python using a Jupyter notebook.

# Live Preview
<p align="center">
Check out this site deployed on <a href="https://fly.io/">Fly.io</a>
<br>
  <a href="https://rightspot.fly.dev/" target="_blank"><strong>https://rightspot.fly.dev/</strong></a>
</p>

# Getting Started
## Prerequisites
- Python: You will need to have Python installed on your machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/
- Django: You will need to have Django installed on your machine. You can install Django using pip, the Python package manager, by running the command pip install django in your terminal.
- SQL database:
```dotenv
// .env
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
```
- Google API credentials: This project uses Google Maps APIs, so you will need to obtain API credentials from the Google Cloud Console.
```dotenv
// .env
GOOGLE_MAPS_API_KEY=
```
- What3Words credentials: This project uses What3Words as a second method to search for a location, so you will need to obtain API credentials from their site here.
```dotenv
// .env
W3W_API_KEY=
```

## Installation
1. Clone the project repository: `git clone https://github.com/Dinssa/RightSpot.git`
2. Navigate to the root directory of the project using `cd <project_directoy>`
3. Create a virtual environment for the project using `python -m venv env`
4. Activate the virtual environment using `source env/bin/activate` command on Linux/Mac or `env\Scripts\activate` command on Windows.
5. Install the required dependencies using `pip install -r requirements.txt` command.
6. Create a .env file in the RightSpot app directory of the project and add the required environment variables. The variables are listed in the prerequisites or you can copy the ‘.env copy’ file and modify it with your values.
7. Run the database migrations using `python manage.py migrate` command.
8. Create a superuser account using `python manage.py createsuperuser` command and follow the prompts to enter your username, email, and password.
9. Start the development server using `python manage.py runserver` command.
10. Open your web browser and navigate to http\:\/\/localhost:8000/ to view the website.

# Teamwork
Working as a team of two, we divided our responsibilities according to our natural areas of focus. I took charge of the frontend development, which involved designing and styling the app, creating the templates, and connecting them with the backend. My partner handled the backend development, which required collecting external data, transforming it into a usable format, and implementing user authentication. We complemented each other’s abilities and contributed to both frontend and backend aspects of the app, creating a balanced and robust product.

# Brief
General Project Requirements:
- Be a full-stack Django application.
- Connect to and perform data operations on a PostgreSQL database (the default SQLLite3 database is not acceptable).
- If consuming an API (OPTIONAL), have at least one data entity (Model) in addition to the built-in User model. The related entity can be either a one-to-many (1:M) or a many-to-many (M:M) relationship.
- If not consuming an API, have at least two data entities (Models) in addition to the built-in User model. It is preferable to have at least one one-to-many (1:M) and one many-to-many (M:M) relationship between entities/models.
- Have full-CRUD data operations across any combination of the app's models (excluding the User model). For example, creating/reading/updating posts and creating/deleting comments qualifies as full-CRUD data operations.
- Authenticate users using Django's built-in authentication.
- Implement authorization by restricting access to the Creation, Updating & Deletion of data resources using the login_required decorator in the case of view functions; or, in the case of class-based views, inheriting from the LoginRequiredMixin class.
- Be deployed online using Heroku.

Other Requirements:
- Your team must manage team contributions and collaboration using Git/GitHub team work-flow.

# Planning
## Entity Relationship Diagram
[![ERD](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216553&authkey=%21AALR6OvkPyaDFfc&width=900)](#)  

The ERD consists of 5 models:
- User
- Project
- Deck (not implemented)
- Location
- Static Data

## Mockups
[![Home page](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216554&authkey=%21AM0wLcM_byIUuVk&width=900)](#)  

On the home page, users can easily search for their desired location by entering either a full or partial address, with autocomplete suggestions, or a three-word address based on the what3words system. What3words is a system that gives every 3m x 3m square on the planet a unique name consisting of three words, which can be useful in countries where formal address systems are not available.

[![Individual location page](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216555&authkey=%21AC6kOzZ1VxR_MLw&width=700)](#)  

Once a valid location is entered, our site shows relevant economic statistics and information for that place. We have summarised some of the data into key indicators that users may find helpful, and we also provide access to all the data for those who want to explore them further. If logged in, users can save a location they’d like to view later or add to a project.

[![Saved locations page](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216558&authkey=%21AF8k7g7dD6u0KaA&width=700)](#)  

Users can easily access their saved locations from a dedicated page, but they must be logged in.

[![Projects page](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216556&authkey=%21ACFF8CokwfXbb1w&width=700)](#)  

The app allows users to create projects and save different locations under each project. This helps users to compare and evaluate various locations for a specific purpose. For example, a user who wants to open a cafe in London can save several potential locations across the city and decide which one is the best.

[![Individual project page](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216557&authkey=%21AP_QMEcMjPS4hLU&width=700)](#)  

On each project page, users can see all the saved locations on a map, write notes related to the project, and select two locations to compare on a separate page.

# Build Process
## Teamwork
The build process for this website required us to first decide how we would work together and split the responsibilities between us both. To manage our tasks and collaborate effectively we followed these key steps:
- We used GitHub Projects to create a kanban board and list each task, assign it to the person who would develop it, and track the progress and status of each task. Our board can be viewed [here](https://github.com/orgs/rightspot-ga/projects/1).
- We had morning standups to discuss what we built the day before, what we were doing today, and what tasks to prioritise. This way, we kept each other updated and focused on the project goals.
- We used separate branches for each feature, working in different branches and merging them to the main branch after testing and reviewing the code. This way, we maintained a clean and stable codebase and avoided conflicts and errors.

## First Steps
Following our initial separation of responsibilities in the frontend and backend we both set to work building the skeleton frontend and backend. I created a basic frontend with the templates we might need and designed the global navigation bar. The navbar is mainly collapsed with clear icons and tooltips that show the page name. When expanded, the user can see the full page name, but this is optional.

## Code Snippets
### Base Template
Creating the frontend skeleton consisted of django template blocks. These are sections of code that I defined in a base template and then overrode or extended by child templates. Each page on the site inherits from the base template and can have different content for each block.

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    ...

    {% block extra_head %}
    {% endblock extra_head %}

    <title>
        {% block title %}
        {% endblock title %}
        | RightSpot
    </title>
</head>
<body class="bg-ivory">
   <div id="sidebar" class="vertical-nav bg-primary">
   ...
   </div>
   <main id="content" class="page-content">
        {% block content %}
        {% endblock content %}
    </main>
    <footer class="text-white">
    ...
    </footer>
    {% block body_bottom %}
    {% endblock body_bottom %}
</body>
</html>
```

The base template consists of the following blocks: `extra_head` for additional imports within a specific page’s head; `title` for the page title within the meta data; `content` for all the main page content; and `body_bottom` for additional scripts added at the end of the html after the footer. These blocks allow me to create consistent and reusable templates with customised content for each page.

### Home Page
The home page allows you to search for a location by entering either a place name or a three-word address. The place name option uses Google Maps Autocomplete, which suggests places in the UK and geocodes them into coordinates. Geocoding is the process of converting an address or a place name into a location on the earth’s surface. The three-word address option uses what3words, which assigns a unique combination of three words to every 3-metre square area on the globe. This is also a form of geocoding, but it uses words instead of numbers to represent locations. Both options send a GET request to /locations/ with the location input and render the location detail template.

```html
{% extends 'base.html' %}
{% load static %}

{% block extra_head %}
<script src="https://maps.googleapis.com/maps/api/js?key={{ google_api_key }}&libraries=places&callback=initAutocomplete" async defer></script>
<script type="module" src="https://cdn.what3words.com/javascript-components@4-latest/dist/what3words/what3words.esm.js"></script>
<script nomodule src="https://cdn.what3words.com/javascript-components@4-latest/dist/what3words/what3words.js"></script>
{% endblock extra_head %}

{% block title %}
Search & Get Location Data
{% endblock title %}

{% block content %}
<div class="container d-flex flex-column align-items-center">
   ...
   <div class="row d-flex flex-column">
        <div class="bg-secondary ...">
            ...
            <form id="normal-search" class="" action="/locations/" method="GET">
                <span class="input-group ...">
                    <input type="text" id="location_search" name="gQuery" class="" placeholder="Enter a location...">
                    <button type="submit" id="location_search_btn" class="btn ..."><span class="pe-3 ...">Search</span><i class="bi bi-search"></i></button>
                </span>
            </form>
            <form id="what3-auto" class="my-4" action="/locations/" method="GET">
                <div class="input-group ...">
                    ...
                    <div class="input-group ...">
                        <div>
                            <what3words-autosuggest api_key="{{ w3w_api_key }}" clip_to_country="GB">
                                <input type="text" />
                            </what3words-autosuggest>
                        </div>  
                        <div>
                            <button type="submit" class="btn ..."><i class="bi bi-search"></i></button>
                        </div>  
                    </div>        
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

The template has two search forms: one with an input field with an ID of location_search, which is linked to the Google Maps Autocomplete service in the initAutocomplete() function; and one with a what3words-autosuggest custom element, which is loaded from a CDN and provides suggestions for three-word addresses. You can use either option to search for a location easily and accurately.

### Location Page
```python
location_name = request.GET.get('gQuery') or request.GET.get('what3words_3wa')
       
    geocode_url = get_api_base_url(request) + '/location_services/geocode'
    geocode_params = {'query': location_name}
    geocode_data = fetch_from_api(geocode_url, geocode_params)
    if not geocode_data:
            return redirect('home')
       
    lat = geocode_data['lat']
    lon = geocode_data['lng']
    ...
```

This code is a snippet from the location_detail view, which handles the search query from the home page and displays the location details.

The code gets the search query from either the gQuery or the what3words_3wa parameter in the request. The gQuery parameter is used for the Google Maps Autocomplete input, and the what3words_3wa parameter is used for the what3words input. The search query is stored in the location_name variable.

For all location related api I’ve created the location_services app with internal api endpoints. One of these endpoints is /location_services/geocode, which can geocode a search query into latitude and longitude coordinates. The endpoint accepts the query as a parameter and returns the geocode_data variable as the response. If the response is empty, the app redirects to the home page.

To make our internal api more understandable and maintainable, I have written swagger documentation for each endpoint. This document explains how the geocoding endpoint works, which can be useful for me, my partner, and any future developers who want to work on our code:

[![Example swagger documentation](https://onedrive.live.com/embed?resid=3AAE4294F4C93984%216559&authkey=%21AGoefRLZ6BmPAsM&width=700)](#)  
You can find all internal api documentation at: https://rightspot.fly.dev/swagger/.

Now with the latitude and longitude we can use them to retrieve a tally of all the nearby places of note, for example, supermarkets, schools, hotels and more using another api within the location_services app at /location_services/nearbyplaces.

```python
# Fetch nearby places
    nearbyplaces_url = get_api_base_url(request) + '/location_services/nearbyplaces'
    nearbyplaces_params = {'lat': lat, 'lng': lon, 'radius': 1000}
    nearbyplaces = fetch_from_api(nearbyplaces_url, nearbyplaces_params)
    if not nearbyplaces:
            return redirect('home')
```
This returns a list with each place nearby. It has to be tallied up and each of the same place type counted using the tallyPlaces helper function.
```python
def tallyPlaces(nearbyplaces):
    # Tally nearby places types
    places_type_counts = {}
    for place in nearbyplaces['results']:
            if 'types' in place:
                for place_type in place['types']:
                        if place_type in places_type_counts:
                                places_type_counts[place_type] += 1
                        else:
                                places_type_counts[place_type] = 1

    # Sort places types by count
    places_type_counts = {k: v for k, v in sorted(places_type_counts.items(), key=lambda item: item[1], reverse=True)}

    # Remove types not needed
    for type_not_needed in types_not_needed:
            if type_not_needed in places_type_counts:
                    del places_type_counts[type_not_needed]

    # Add icons to places types
    places_types = []
    for place_type in places_type_counts:
            places_types.append({
                    'name': place_type,
                    'count': places_type_counts[place_type],
                    'icon': places_icon_lookup.get(place_type, 'bi-geo-alt')
            })
   
    # Format places types
    for place_type in places_types:
        # Replace "_" with " " in place types
        place_type['name'] = place_type['name'].replace('_', ' ')
        # Add 's' to end of place types if count > 1
        if place_type['count'] > 1:
            place_type['name'] = place_type['name'] + 's'
        # Capitalise place types
        place_type['name'] = place_type['name'].title()

    return places_types
```
This function takes a list of nearby places and tallies the types of places, sorts them by count, removes unwanted types, adds icons to the types, and formats the types for display. The formatted types are returned as a list of dictionaries containing the name, count, and icon of each type.

Now to make this app more useful, we need to get the core data from our database with ONS statistics. This data is based on the ‘district’ of a location, which is its general area, such as a town name or a borough within a city. To get the district and other details for a given GPS location, we can use another API endpoint form location_services at the endpoint /location_services/geodetails.
```python
# Fetch address details
    geodetails_url = get_api_base_url(request) + '/location_services/geodetails'
    geodetails_params = {'lat': lat, 'lng': lon}
    addressparts = fetch_from_api(geodetails_url, geodetails_params)
    if not addressparts:
            return redirect('home')

# Get district name for ONS data matching
    district = check_uk_district(addressparts)
```
Within the result addressparts, there should be an attribute called ‘district’ which needs to be checked against a constant list of available districts in the UK.

We then use the ‘data’ app, which my partner developed, to get the ONS data for the ‘district’ of a location. The /data/ons endpoint takes a district query and returns the ONS data. Then, it stores the formatted data in a yearly dictionary. The comparison variables dictionary contains this yearly dictionary. Finally, we make a location dictionary with the query, coordinates, address, nearby places, and comparison variables.

Finally we render the Django template…
```python
return render(request, 'locations/detail.html', {
                    'name': f"{location['address']['postcode']}, {location['address']['country']}",
                    'stats': stats,
                    'names': inverse_names,
                    'demographics': demographics_final_order_list,
                    'socioeconomics': socioeconomics_final_order_list,
                    'industry': industry_final_order_list,
                    'nearby': tallyPlaces(nearbyplaces),
                    'location': location,
                    'projects': Project.objects.filter(user=request.user) if isinstance(request.user, User) else None,
                    'google_api_key': env('GOOGLE_MAPS_API_KEY'),
    })
```

The render function takes the following variables as arguments:
- name: a string that represents the location’s postcode and country, such as “CR0 1EA, UK”.
- stats: a dictionary that stores various statistics about the location, such as population, area, and density.
- names, demographics, socioeconomics, and industry: lists of dictionaries that contain data about the location’s name history, demographic composition, socioeconomic indicators, and industry sectors.
- nearby: a list of dictionaries that contain data about places that are close to the location, such as name, distance, and type.
- location: a dictionary that contains information about the location itself, such as its query, coordinates, and address.
- projects: a list of projects that are associated with the current user, if they are logged in. Otherwise, this variable is empty.
- google_api_key: a string that contains the Google Maps API key, which is used to render a map of the location on the web page.

# Challenges
- Using the Google Maps JavaScript API to display and initialise a map was a reasonably challenging task, as it required following the documentation carefully and setting the API parameters correctly from the variables passed to the template by the view.

# Wins
- Separating out the internal API into their own app was a good example of modular design, which creates independent components that are reusable and easy to maintain. This abstraction benefited the project in several ways, such as allowing for low-level changes in the API without affecting the high-level functionality in the frontend.
- The app we built showcases strong collaboration and good domain expertise. We each contributed to the functionality of the app in our respective area, and we communicated effectively throughout the project. We were able to complete the app within the time limit and achieve a high-quality result.

# Key Learnings & Takeaways
- My confidence in using external APIs has increased, especially with Google Maps. This is the second project where I have used their API and I have learned from my previous experience to become more familiar with the tools.
- As a team member, I enhanced my team communication skills through regular standups and frequent interactions. I also developed my project management skills, using Github tools such as issue tracking and projects (kanban board) to work together smoothly and effectively.

# Bugs
- During the final stages of this project, I encountered a problem when I refactored the navigation bar into a separate file from the base template. The toolbar tooltips did not load properly or change according to the toolbar status (expanded or collapsed). To fix this, one option is to revert the refactor and keep the navigation bar in the base template, as that worked well before. Another option is to debug the separate file and find out what caused the tooltips to malfunction.

# Future Improvements
- A future improvement for our project would be to present the data in a more visual and useful way, using graphs, charts, and other statistics visualisation techniques. This would make the data easier to understand and compare, as well as more attractive and engaging.

