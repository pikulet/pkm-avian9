config = {
    "Card 1"    :   ("c1", ["c1-a.jpg", "c1-a.jpg"]),
    "Card 2"    :   ("c2", ["c1-a.jpg", "c1-a.jpg", "c1-a.jpg"])
}

def get_cid(name):
    return config[name][0]

def get_images(name):
    return config[name][1]

img_folder = "images/"

welcome_msg = """Selling this entire collection for $88,888 SGD. 
    Contact me @zard9 on CarousellSG"""

related_links = {
    "pikachu"   :   "https://www.google.com",
    "raichu"    :   "https://www.facebook.com"
}
