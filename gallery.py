from pyscript import display
photos = [

    {"name": "Alice", "caption": "Science Fair Fun!", "img": "IMG-0135-A.jpg"},
    {"name": "Bob", "caption": "Soccer Tournament Day", "img": "soccer.jpg"},
    {"name": "Charlie", "caption": "Art Class Creations", "img": "art_class.jpg"},
    {"name": "Diana", "caption": "Field Trip Adventures", "img": "field_trip.jpg"},
    {"name": "Ethan", "caption": "Science Lab Experiments", "img": "lab.jpg"},
    {"name": "Fiona", "caption": "Basketball Practice", "img": "basketball.jpg"},
    {"name": "George", "caption": "Music Class Fun", "img": "music.jpg"},
    {"name": "Hannah", "caption": "Field Day Games", "img": "field_day.jpg"},
]

gallery_html = ""

for photo in photos:
    card = f"""
    <div class='card'>
      <img src='{photo["img"]}' alt='{photo["caption"]}' />
      <h3>{photo["name"]}</h3>
      <p>{photo["caption"]}</p>
    </div>
    """
    gallery_html += card

    print(gallery_html)