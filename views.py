from flask import Blueprint, render_template, request, jsonify, redirect, url_for
views = Blueprint(__name__, "views")


@views.route('/')
def home():
    return render_template("index.html", name="Matiss", age= 33)
      
      
# <dynamic name change ir url> (request)
''' @views.route('/profile/<username>')
def profile(username):
  return render_template("index.html", name=username) '''
  
# query parametrs (jsonify)
@views.route('/profile')
def profile():
  # render profile.html 
  return render_template("profile.html") 
  # render name=name
'''   args = request.args # queary :?
  name = args.get('name')
  return render_template("index.html", name=name) '''




# return JSON
@views.route('/json')
def get_json():
    return jsonify({"name": "tim",'coolnes': 10})

# getting json data

@views.route('/data')
def get_data():
  data = request.json # sent
  return jsonify(data) # access


# redirect page (redirect, url_for) import

@views.route('/go-to-home')
def go_to_home():
  return redirect(url_for("views.get_json")) # .get_json (rediirect site)


    


