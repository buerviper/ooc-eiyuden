from mastodon import Mastodon
from pathlib import Path
import os
import random
import yaml
import datetime
import time


# Access Mastodon instance
mastodon = Mastodon(
    access_token=os.environ['MASTODON_ACCESS_TOKEN'],
    api_base_url='mastodon.social'
)

date = datetime.datetime.now()

if int(date.strftime("%d")) == 24 and int(date.strftime("%m")) == 12:
    post_date = "christmas"
elif int(date.strftime("%d")) == 31 and int(date.strftime("%m")) == 10:
    post_date = "halloween"
elif int(date.strftime("%d")) == 27 and int(date.strftime("%m")) == 7:
    post_date = "anniversary-kickstarter"
elif int(date.strftime("%d")) == 23 and int(date.strftime("%m")) == 4:
    post_date = "anniversary-launch"
elif int(date.strftime("%d")) == 31 and int(date.strftime("%m")) == 12:
    post_date = "newyear"
else:
    post_date = "default"

# Function to post status with image
def post_status_with_image(name, spoiler_warning="False", status="#eiyuden #EiyudenChronicle #100HeroesStrong #jrpg", sensitivity=False, language="en"):
    description_file = open(image_path + "/descriptions/" + name + ".yml", "r")
    description = yaml.load(description_file, Loader=yaml.FullLoader)
    status = description["status"]
    spoiler_warning = description["spoiler_warning"]
    language = description["language"]
    if description["sensitivity"] == True:
        sensitivity = True
    mastodon.status_post(status,
                         media_ids=media_list,
                         spoiler_text=spoiler_warning,
                         sensitive=sensitivity,
                         language=language)


# Function to prepare media with image descriptions etc.
def media_description(media):
    description_file = open(image_path + "/descriptions/" + media + ".yml", "r")
    description = yaml.load(description_file, Loader=yaml.FullLoader)
    alt_text = description["description"]
    os.chdir(image_path)
    filename = media + file_extension
    if file_extension == ".png":
        file_format = "image/png"
    elif file_extension == ".jpg" or file_extension == ".jpeg":
        file_format = "image/jpeg"
    elif file_extension == ".gif":
        file_format = "image/gif"
    post = mastodon.media_post(filename, file_format, description=alt_text)
    media_list.append(post["id"])
    os.chdir("..")


image_path = "images-" + post_date

# Choose a random photo out of the /images folder
photo = random.choice([x for x in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, x))])

# Get name of photo without ending
name = Path(image_path + "/" + photo).stem

print(name)

# Get file format of photo
file_extension = Path(photo).suffix

# Create an empty list for all the photos/media we want to add
media_list = []

# Check if photo is part of a series
if name[-1].isdigit():
    # Get both images
    name_1 = name[:-1] + "1"
    name_2 = name[:-1] + "2"
    name_list = [name_1, name_2]
    # check if image 3 and 4 exist and add to list
    if os.path.exists(image_path + "/" + name[:-1] + "3" + file_extension):
        name_3 = name[:-1] + "3"
        name_list.append(name_3)
        if os.path.exists(image_path + "/" + name[:-1] + "4"+ file_extension):
            name_4 = name[:-1] + "4"
            name_list.append(name_4)
    for x in name_list:
        media_description(x)
else:
    # Get details of post
    media_description(name)

# wait 10 seconds for larger files to upload
time.sleep(10)

# Post a new status update
post_status_with_image(name)
