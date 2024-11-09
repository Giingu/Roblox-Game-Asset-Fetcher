# Roblox Game Icon Fetcher

## Overview

This script is designed to help developers and users fetch game icons from the Roblox platform using Place IDs. By querying the Roblox Universe API, the script obtains Universe IDs and then retrieves the corresponding game icons. Each iteration includes a wait period and a cooldown, which ensures the process doesn’t overload the server.

## Features

- **Place ID to Universe ID Conversion**: Retrieves Universe IDs using Place IDs.
- **Game Icon Retrieval**: Fetches game icons based on Universe IDs.
- **Progress Bars**: Shows fetching progress with `tqdm` and `alive_progress` for a user-friendly experience.
- **Randomized Waiting**: Adds a randomized waiting time between requests.
- **Cooldown**: A cooldown period after each loop to avoid rate limiting.

## Prerequisites

- Python 3.x
- `requests` library for HTTP requests
- `tqdm` and `alive_progress` for progress bars

Install required packages:
```bash
pip install requests tqdm alive-progress
```

## Usage

1. Define the Place IDs in the `place_ids` list.
2. Run the script:
   ```bash
   python fetch_icons.py
   ```
3. The script will loop through each Place ID, retrieve its Universe ID, and fetch the game icon URL, displaying the URLs along with progress and cooldown indicators.

## License

This project is licensed under the MIT License.
