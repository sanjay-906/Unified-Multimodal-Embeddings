# animals
an = [
    "Dog", "Rooster", "Pig",
    "Cow", "Frog", "Cat",
    "Hen", "Insects (flying)",
    "Sheep", "Crow"
]

# natural soundscapes and water sounds
ns_and_ws = [
    "Rain", "Sea waves", "Crackling fire",
    "Crickets", "Chirping birds", "Water drops",
    "Wind", "Pouring water",
    "Toilet flush", "Thunderstorm"
]

# human and non speech sounds
h_and_nss = [
    "Crying baby", "Sneezing", "Clapping",
    "Breathing", "Coughing", "Footsteps",
    "Laughing", "Brushing teeth", "Snoring",
    "Drinking, sipping"
]

# interior domestic sounds
ids = [
    "Door knock", "Mouse click", "Keyboard typing",
    "Door, wood creaks", "Can opening",
    "Washing machine", "Vacuum cleaner",
    "Clock alarm", "Clock tick", "Glass breaking"
]

# exterior urban noises
eun = [
    "Helicopter", "Chainsaw", "Siren",
    "Car horn", "Engine", "Train",
    "Church bells", "Airplane", "Fireworks",
    "Hand saw"
]


def return_categories():
    return an + ns_and_ws + h_and_nss + ids + eun
