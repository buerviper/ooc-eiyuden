import yaml
import os
from pathlib import Path

def generate_yaml_description(file_save, file_name):
    if file_name.split("-")[1] == "01":
        yaml.dump({'status': '#eiyuden #EiyudenChronicle #100HeroesStrong #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Eiyuden Chronicle.',
                   'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "rising":
        yaml.dump({'status': '#eiyuden #EiyudenChronicleRising #100HeroesStrong #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Eiyuden Chronicle: Rising.',
                   'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "kickstarter":
        yaml.dump({'status': '#eiyuden #EiyudenChronicle #100HeroesStrong #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Eiyuden Chronicle.',
                   'language': '', 'sensitivity': ''}, file_save)

def folder_choice(folder):
    for x in os.listdir("images-" + folder):
        if os.path.isfile(Path("images-" + folder + "/" + x)):
            name = Path("images-" + folder + "/" + x).stem
            if not os.path.exists("images-" + folder + "/descriptions/"+name + ".yml"):
                file_yml = open("images-" + folder + "/descriptions/" + name + ".yml", "w")
                generate_yaml_description(file_yml, name)

folder_list = ["default", "anniversary-kickstarter", "anniversary-launch", "christmas", "halloween", "newyear"]

for x in folder_list:
    folder_choice(x)