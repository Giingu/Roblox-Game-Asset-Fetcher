import requests
import random
import time
from tqdm import tqdm
from alive_progress import alive_bar

# Define the Place IDs in a JSON format
place_ids = [11572762117, 14184086618, 13157638696]

# Function to get Universe ID from Place ID
def get_universe_id(place_id):
    url = f"https://apis.roproxy.com/universes/v1/places/{place_id}/universe"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('universeId')
    else:
        print(f"Failed to get Universe ID for Place ID: {place_id}")
        return None

# Function to get Game Icon from Universe ID
def get_game_icon(universe_id):
    url = f"https://thumbnails.roproxy.com/v1/games/icons?universeIds={universe_id}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data'][0]['imageUrl']
    else:
        print(f"Failed to get Game Icon for Universe ID: {universe_id}")
    return None

def print_progress(elapsed, total, progress):
    wait_bar_length = 20
    progress_bar_length = 20

    wait_filled_length = int(elapsed / total * wait_bar_length)
    prog_filled_length = int(progress / 100 * progress_bar_length)

    wait_bar = '█' * wait_filled_length + '-' * (wait_bar_length - wait_filled_length)
    prog_bar = '█' * prog_filled_length + '-' * (progress_bar_length - prog_filled_length)

    print(f"\rWaiting: {total - elapsed}s [{wait_bar}] Progress: {progress:.0f}% [{prog_bar}]", end="", flush=True)

# Main loop to repeatedly fetch the game icons
while True:
    print("Starting new loop...\n")

    for idx, place_id in enumerate(place_ids, start=1):
        universe_id = get_universe_id(place_id)
        if universe_id:
            icon_url = get_game_icon(universe_id)
            result = f"Game {idx} / {len(place_ids)}:\nGame Icon URL for Place ID {place_id}: {icon_url}\n"
        else:
            result = f"Game {idx} / {len(place_ids)}:\nNo Universe ID found for Place ID {place_id}\n"

        print(result)

        if idx < len(place_ids):
            wait_time = random.randint(5, 20)
            progress = idx / len(place_ids) * 100
            for elapsed in range(0, wait_time):
                print_progress(elapsed, wait_time, progress)
                time.sleep(1)
            print("\r" + " " * 80, end="\r", flush=True)  # Clear the line after waiting

    print("Cooling down for 60 seconds...")
    with alive_bar(60, title="Cooldown", bar="blocks") as bar:
        for _ in range(60):
            time.sleep(1)
            bar()
