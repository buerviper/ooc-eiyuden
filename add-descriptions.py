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

for x in os.listdir("images"):
    if os.path.isfile(os.path.join("images", x)):
        name = Path("images/" + x).stem
        if not os.path.exists("images/descriptions/"+name + ".yml"):
            file_yml = open("images/descriptions/" + name + ".yml", "w")
            generate_yaml_description(file_yml, name)
