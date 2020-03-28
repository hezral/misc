import urllib.request
import json
import random
import string
import gi
import os
import subprocess

gi.require_version('Notify', '0.7')
gi.require_version('Gtk', '3.0')
from gi.repository import Notify, Gtk, GdkPixbuf

# Define a callback function
def my_callback_func():
    pass

APPINDICATOR_ID = "avatar"
Notify.init(APPINDICATOR_ID)

Notify.init("Test App")
notification = Notify.Notification.new("<b>A wild Pokemon appeared</b>","test")

notification.add_action(
    "action_click",
    "Reply to Message",
    my_callback_func,
    None # Arguments
)

# Use GdkPixbuf to create the proper image type
image = GdkPixbuf.Pixbuf.new_from_file("/home/adi/Work/publicapi-tests/abott.png")

# Use the GdkPixbuf image
notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)

notification.show()



#url = "http://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 721))
#url = "https://api.adorable.io/avatars/48/abott"

#f = open('avatar.png', 'wb')
#f.write(urllib.request.urlopen(url).read())
#f.close()

#icon = "/home/adi/Work/publicapi-tests/avatar.png"

#request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#response = urllib.request.urlopen(request)

#pokemon_name = json.loads(response.read().decode('utf-8'))['name']
#pokemon_name = string.capwords(pokemon_name)  # make it look nice
#pokemon_name = str(pokemon_name)
#pokemon_name = string.capwords(pokemon_name)


#Notify.Notification.new("<b>A wild Pokemon appeared</b>",pokemon_name,"internet-chat").show()
#Notify.Notification.new("<b>A wild Pokemon appeared</b>",pokemon_name,"internet-chat").show()


#`subprocess.Popen(["notify-send", "-i", icon, "something2", "something3"])

#print(os.path.abspath('internet-chat.svg'))