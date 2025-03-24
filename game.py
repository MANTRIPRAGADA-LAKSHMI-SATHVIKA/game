import pygame
import random
from PIL import Image


pygame.mixer.init()
pygame.mixer.music.load("175205__minigunfiend__scary-creaking-knocking-wood.wav")  
pygame.mixer.music.play(-1)  


horror_images = {
    "haunted house": "haunted_house.jpg",
    "graveyard": "graveyard.jpg",
    "abandoned hospital": "hospital.jpg",
    "dark forest": "forest.jpg"
}


story_template = """
It was a dark and stormy night. {name} was walking through the {place}, their footsteps barely audible over the howling wind.
The trees swayed violently, their twisted branches clawing at the sky like skeletal fingers. Suddenly, {creepy_event}.

A cold chill ran down their spine. The air around them felt heavier, pressing against their chest like an unseen force.
They heard a {sound} coming from behind. It was faint at first, almost a whisper carried by the wind. But then it grew louder… closer.

With a sinking feeling, they turned around—only to see {scary_figure} staring at them. Its hollow eyes gleamed in the darkness,
void of any human emotion. The ground beneath them seemed to shift, their legs frozen in terror. The figure didn’t move,
but the suffocating silence made its presence unbearable.

Their heart pounded as they tried to {escape_method}, but the ground felt like quicksand beneath their feet.
The shadows stretched toward them, wrapping around like unseen hands. Then, in a voice barely above a whisper,
the figure leaned in and breathed,
\"{whisper}\"

The world blurred, their vision darkening at the edges. The last thing they saw before everything went black
was the figure’s twisted grin…

And then, silence.
"""


print("🕷️ Welcome to the Horror Mad Libs! Fill in the blanks with your choices. 🕷️\n")
words = {
    "name": input("Enter a name: "),
    "place": input("Enter a scary place (haunted house, graveyard, abandoned hospital, dark forest): ").lower(),
    "creepy_event": input("Enter a creepy event (a shadow moved, a door creaked open, whispers filled the air): "),
    "sound": input("Enter a scary sound (scream, footsteps, whispering, laughter): "),
    "scary_figure": input("Enter a horror character (ghost, vampire, shadow figure, zombie): "),
    "escape_method": input("Enter an escape method (run, scream, hide, faint): "),
    "whisper": input("Enter the last words you hear: ")
}


horror_story = story_template.format(**words)


print("\n🎃 Your Horror Story 🎃\n")
print(horror_story)

if words["place"] in horror_images:
    img = Image.open(horror_images[words["place"]]) 
else:
    img = Image.open("default_horror.jpg")  
img.show()

print("\n💀 The End… or is it? 💀")
