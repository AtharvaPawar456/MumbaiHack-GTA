#  i have created this file - GTA

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import SensorData, Nodedata, Clusterdata
# import uuid
# import random

# import folium

# import ast
# from datetime import datetime, timedelta

# You can use the ast module in Python to safely convert a string representation of a list to an actual list. Here's how you can do it:

# from django.http import HttpResponse
# from .models import Product, Contact

# Create your views here.


def welcome(request):
    return render(request, 'mozoop/welcome.html')

def home(request):
    return render(request, 'mozoop/home.html')







def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'mozoop/register.html',
                  {'error_message': error_message})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'mozoop/login.html',
                  {'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view













# @login_required
# def viewNodes(request):
#     try:

#         user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#         user_clusterdata = Clusterdata.objects.filter(
#             user_name=request.user.username)
#         # print("user_nodes : ", user_nodes)
#         # print("username : ", request.user.username)

#         # Pass the list of nodes to the template
#         context = {
#             'user_nodes': user_nodes,
#             'user_clusterdata': user_clusterdata,
#         }
#         return render(request, 'agroapp/nodes.html', context)

#     except:
#         return render(request, 'agroapp/nodes.html')


# @login_required
# def addnode(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         node_name = request.POST.get('node_name')
#         Loc_lat = request.POST.get('lat')
#         Loc_long = request.POST.get('long')
#         api_key = generate_unique_api_key()

#         # Create a new node
#         Nodedata.objects.create(user_name=user_name,
#                                 node_name=node_name,
#                                 Loc_lat=Loc_lat,
#                                 Loc_long=Loc_long,
#                                 api_key=api_key)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     return render(request, 'agroapp/addnode.html')


# @login_required
# def addcluster(request):
#     if request.method == 'POST':
#         selected_nodes = request.POST.getlist('selected_nodes')
#         user_name = request.user.username
#         cluster_name = request.POST.get('cluster_name')

#         print("Selected Nodes:", selected_nodes, user_name, cluster_name)

#         # Create a new node
#         Clusterdata.objects.create(user_name=user_name,
#                                    cluster_name=cluster_name,
#                                    clust_data=selected_nodes)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#     context = {
#         'user_nodes': user_nodes,
#     }
#     return render(request, 'agroapp/addcluster.html', context)


# def get_the_map(lat, long, node_name):
#     # Specify the latitude and longitude
#     # lat, lon = 123.13, 123.34

#     # Create a Folium map centered at the specified location
#     my_map = folium.Map(location=[lat, long], zoom_start=16)

#     # Add a marker at the specified location
#     folium.Marker([lat, long], popup=node_name).add_to(my_map)
#     # folium.Marker([lat, long], popup=node_name, icon=folium.Icon(color='red')).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html

#     # Pass the HTML content to the template
#     # return render(request, 'mymaps.html', {'map_html': map_html})


# def get_the_map_multipal_loc(locations):
#     # Create a Folium map centered at the first location
#     first_location = locations[0]

#     my_map = folium.Map(
#         location=[first_location['lat'], first_location['long']],
#         zoom_start=16)

#     # Add markers for each location
#     for location in locations:
#         folium.Marker([location['lat'], location['long']],
#                       popup=location['node_name']).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html


# # @login_required
# def viewNodeData(request):
    # Get parameters from the GET request

    # username = request.GET.get('username', '')  # Hacker Trap
    # username = request.user.username
    # nodename = request.GET.get('nodename', '')
    # # lat = request.GET.get('lat', '')
    # # long = request.GET.get('long', '')

    # if Nodedata.objects.filter(node_name=nodename).exists():
    #     # Use the parameters as needed in your view logic
    #     try:
    #         # Example: Retrieve sensor data based on the node name

    #         sensor_data = SensorData.objects.filter(
    #             nodename=nodename).order_by('-timestamp')
    #         # sensor_data = SensorData.objects.filter(nodename=nodename)

    #         # Retrieve the latest data for the specified nodename
    #         latest_sensor_data = SensorData.objects.filter(
    #             nodename=nodename).order_by('-timestamp').first()

    #         latest_5_sensor_data_list = SensorData.objects.filter(
    #             nodename=nodename).order_by('-timestamp')[:5]
    #         latest_5_sensor_data_list = latest_5_sensor_data_list[::-1]

    #         # if not latest_5_sensor_data_list:
    #         # latest_5_sensor_data_list = latest_sensor_data
    #         # latest_sensor_data = "null"

    #     except:
    #         sensor_data = "null"
    #         latest_sensor_data = "null"
    #         latest_5_sensor_data_list = "null"

    #     user_node_data = Nodedata.objects.filter(node_name=nodename).first()

    #     if user_node_data:
    #         api_key = user_node_data.api_key
    #         user_name = user_node_data.user_name
    #         lat = user_node_data.Loc_lat
    #         long = user_node_data.Loc_long
    #     else:
    #         api_key = 'Not available'
    #         user_name = 'Not available'
    #         lat = 'Not available'
    #         long = 'Not available'

    #     map_html = get_the_map(lat, long, nodename)

    #     # Pass data to the template
    #     context = {
    #         'username': user_name,
    #         'nodename': nodename,
    #         'lat': lat,
    #         'long': long,
    #         'api_key': api_key,
    #         'sensor_data': sensor_data,
    #         'latest_data': latest_sensor_data,
    #         'map_html': map_html,
    #         'latest_5_sensor_data_list': latest_5_sensor_data_list,
    #     }
    #     return render(request, 'agroapp/nodedata.html', context)
    # else:
    #     context = {"message": "wrong_route"}
    #     return render(request, 'agroapp/nodedata.html', context)


# # @login_required
# def viewclusterData(request):

#     # username = request.GET.get('username', '')  # Hacker Trap
#     # username = request.user.username
#     clustername = request.GET.get('clustername', '')

#     if Clusterdata.objects.filter(cluster_name=clustername).exists():
#         try:

#             cluster_data = Clusterdata.objects.filter(cluster_name=clustername)
#             # Extract 'clust_data' from each object and store it in a list
#             list_of_clust_data = [entry.clust_data for entry in cluster_data]

#             all_node_names = ast.literal_eval(list_of_clust_data[0])
#             all_nodeData = []

#             for item in all_node_names:
#                 __nodedata = Nodedata.objects.filter(node_name=item).first()
#                 all_nodeData.append(__nodedata)

#             locations = []
#             all_sensor_data = {nodeName: [] for nodeName in all_node_names}
#             all_latest_sensor_data = []
#             all_latest_5_sensor_data_list = []

#             for node_D in all_nodeData:
#                 locations.append({
#                     'lat': node_D.Loc_lat,
#                     'long': node_D.Loc_long,
#                     'node_name': node_D.node_name
#                 })

#             for __nodeNames in all_node_names:
#                 # print("__nodeNames : ",__nodeNames)

#                 valu = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')

#                 # print("valu : ", valu)

#                 all_sensor_data[__nodeNames].append(valu)
#                 # values['dadar'].append('Data 1 for Dadar')

#                 # print("all all_sensor_data :", all_sensor_data)

#                 all_latest_sensor_data.append(
#                     SensorData.objects.filter(
#                         nodename=__nodeNames).order_by('-timestamp').first())

#                 ___all_lat_5_sensor_data_list = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')[:5]
#                 ___all_lat_5_sensor_data_list = ___all_lat_5_sensor_data_list[::
#                                                                               -1]
#                 all_latest_5_sensor_data_list.append(
#                     ___all_lat_5_sensor_data_list)

#             # print("all_latest_5_sensor_data_list :", all_latest_5_sensor_data_list)

#             # user_node_data = Nodedata.objects.filter(node_name=nodename).first()
#             # sensor_data = SensorData.objects.filter(nodename=nodename)

#             # print("locations : ", locations)
#             map_html = get_the_map_multipal_loc(locations)

#         except:
#             all_sensor_data = "null"
#             all_latest_sensor_data = "null"
#             all_latest_5_sensor_data_list = "null"
#             map_html = "null"

#         # print("all_latest_5_sensor_data_list : " , all_latest_5_sensor_data_list)
#         # Pass data to the template
#         context = {
#             # 'username': user_name,
#             'clustername': clustername,
#             # 'lat': lat,
#             # 'long': long,
#             # 'api_key': api_key,
#             'all_sensor_data': all_sensor_data,
#             'all_latest_sensor_data': all_latest_sensor_data,
#             'all_latest_5_sensor_data_list': all_latest_5_sensor_data_list,
#             'map_html': map_html,
#         }
#         return render(request, 'agroapp/clusterdata.html', context)

#     else:
#         context = {"message": "wrong_route"}
#         return render(request, 'agroapp/clusterdata.html', context)




# route : http://127.0.0.1:8000/read_sensor_data/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar


# def read_sensor_data(request):
#     if request.method == 'GET':
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             sensor_data = SensorData.objects.filter(nodename=nodename)
#             # Convert QuerySet to a list of dictionaries
#             sensor_data_list = list(sensor_data.values())

#             ret_data = {
#                 'user_name': username,
#                 'node_name': nodename,
#                 'sensor_Data': sensor_data_list,
#             }
#             return JsonResponse(ret_data)
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


# # route : http://127.0.0.1:8000/sensordata/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar&Depth_1=45.3&Depth_2=49.3&Depth_3=55.9&temperature=55.9&humidity=55.9


# def get_formatted_datetime():
#     # Get the current date and time
#     now = datetime.now()

#     # Add 6 hours to the current time
#     future_time = now + timedelta(hours=6)

#     # Define the month names
#     month_names = [
#         "January", "February", "March", "April", "May", "June", "July",
#         "August", "September", "October", "November", "December"
#     ]

#     # Extract the components of the date and time
#     month = month_names[future_time.month - 1]  # Adjust index to start from 0
#     day = future_time.day
#     year = future_time.year
#     hour = future_time.strftime("%I")  # 12-hour format
#     minute = future_time.minute
#     ampm = future_time.strftime("%p").lower()  # AM or PM

#     # Format the date and time string
#     formatted_date_time = f"{month} {day}, {year}, {hour}:{minute} {ampm}."

#     return formatted_date_time


# # @csrf_exempt
# def sensor_data(request):
#     if request.method == 'GET':
#         # Get parameters from the GET request
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         depth_1 = float(request.GET.get('Depth_1', None))
#         depth_2 = float(request.GET.get('Depth_2', None))
#         depth_3 = float(request.GET.get('Depth_3', None))

#         temperature = float(request.GET.get('temperature', None))
#         humidity = float(request.GET.get('humidity', None))

#         timestampManual = get_formatted_datetime()
#         print("timestampManual :", timestampManual)

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             # Save data to the database
#             sensor_data = SensorData(
#                 nodename=nodename,
#                 depth_1=depth_1,
#                 depth_2=depth_2,
#                 depth_3=depth_3,
#                 temperature=temperature,
#                 humidity=humidity,
#                 timestamp=timestampManual  # Set the timestamp manually
#             )
#             sensor_data.save()

#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


'''
node_prabhadevi
9650ad02-52e0-4825-8f63-ef2b5235ee77

node_dadar
5df155f4-9161-44b9-8ff5-9c821709e1bf
'''
'''
import random

def generate_api_key():
    key_length = 36  # Length of the API key
    dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

    characters = "abcdef0123456789"

    api_key = ''.join(random.choice(characters) if i not in dash_positions else '-' for i in range(key_length))
    return api_key

# Example usage
api_key = generate_api_key()
print(api_key)

'''


# def generate_api_key():
#     key_length = 36  # Length of the API key
#     dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

#     characters = "abcdefghijklmnopqrstwxyz0123456789"

#     api_key = ''.join(
#         random.choice(characters) if i not in dash_positions else '-'
#         for i in range(key_length))
#     return api_key


# def generate_unique_api_key():
#     while True:
#         # api_key = str(uuid.uuid4())
#         api_key = str(generate_api_key())
#         if not Nodedata.objects.filter(api_key=api_key).exists():
#             return api_key


# def your_view_function(request):
#     # Your view logic here
#     api_key = generate_unique_api_key()

#     # Use api_key in your view logic or save it to the database

#     return HttpResponse(f"Generated API Key: {api_key}")


# ------------------------------------
# Sample Code Below
# ------------------------------------

# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n])

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)

# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)

#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })

# # def index(request):
# #     return HttpResponse('Teamzeffort    |      index Page')
