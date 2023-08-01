from mastodon import Mastodon
from pathlib import Path
import os
import random
import yaml


# Access Mastodon instance
mastodon = Mastodon(
    access_token=os.environ['MASTODON_ACCESS_TOKEN'],
    api_base_url='botsin.space'
)


# Function to post status with image
def post_status_with_image(name, spoiler_warning="False", status="#eiyuden #EiyudenChronicle #100HeroesStrong #jrpg #christmas #MerryChristmas", sensitivity="False", language="en"):
    description_file = open("images-christmas/descriptions/" + name + ".yml", "r")
    description = yaml.load(description_file, Loader=yaml.FullLoader)
    status = description["status"]
    spoiler_warning = description["spoiler_warning"]
    language = description["language"]
    sensitivity = description["sensitivity"]
    mastodon.status_post(status, media_ids=media_list, spoiler_text=spoiler_warning, sensitive=sensitivity,
                         language=language)


# Function to prepare media with image descriptions etc.
def media_description(media):
    description_file = open("images-christmas/descriptions/" + media + ".yml", "r")
    description = yaml.load(description_file, Loader=yaml.FullLoader)
    alt_text = description["description"]
    os.chdir("images-christmas")
    filename = media + file_extension
    if file_extension == ".png":
        file_format = "image/png"
    elif file_extension == ".jpeg":
        file_format = "image/jpeg"
    elif file_extension == ".gif":
        file_format = "image/gif"
    post = mastodon.media_post(filename, file_format, description=alt_text)
    media_list.append(post["id"])
    os.chdir("..")


# Choose a random photo out of the /images folder
photo = random.choice([x for x in os.listdir("images-christmas") if os.path.isfile(os.path.join("images-christmas", x))])

# Get name of photo without ending
name = Path("images-christmas/" + photo).stem

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
    if os.path.exists("images-christmas/" + name[:-1] + "3.png"):
        name_3 = name[:-1] + "3"
        name_list.append(name_3)
        if os.path.exists("images-christmas/" + name[:-1] + "4.png"):
            name_4 = name[:-1] + "4"
            name_list.append(name_4)
    for x in name_list:
        media_description(x)
else:
    # Get details of post
    media_description(name)

# Post a new status update
post_status_with_image(name)
