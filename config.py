title = "zard9 Charizard Collection"

config = {
    # name	: (is_holo, num_images)
    "ZF"    	: ("Skyridge Crystal Charizard", 2),
    "ZE"	: ("Skyridge Crystal Charizard Reverse Holo", 2),
    "ZR"        : ("PSA 10 Pre-Release Teamup Charizard", 1),
    "ZO"	: ("BNIB CP6 Booster Box", 1),
    "ZN"    	: ("BNIB Pokemon Center 2016 Pokemon Card Game Art Collection", 2),
    "S"		: ("Base Set Charizard", 2),
    "T"		: ("Base Set 2 Charizard", 2),
    "ZC"	: ("Legendary Reverse Charizard", 2),
    "ZL"    	: ("Shining Charizard", 2),
    "ZM"    	: ("XY Evolution Pre-Release Charizard", 2),
    "U"		: ("CP6 Charizard", 2),
    "V"		: ("CP6 Charizard", 2),
    "W"		: ("Anniversary Charizard", 2),
    "A"		: (0, 2),
    "B"		: (0, 2),
    "C"		: (0, 2),
    "D"		: (0, 2),
    "E"		: (0, 2),
    "F"		: (0, 2),
    "G"		: (0, 2),
    "H"		: (0, 2),
    "I"		: (0, 2),
    "J"		: (0, 2),
    "K"		: (0, 2),
    "L"		: (0, 2),
    "M"		: (0, 2),
    "N"		: (0, 2),
    "O"		: (0, 2),
    "P"		: (0, 2),
    "Q"		: (0, 2),
    "R"		: (0, 2),
    "X"		: (0, 2),
    "Y"		: (0, 2),
    "Z"		: (0, 2),
    "ZB"	: (1, 2),
    "ZG"    	: (0, 2),
    "ZH"    	: (0, 2),
    "ZI"    	: (0, 2),
    "ZJ"    	: (0, 2),
    "ZK"    	: (0, 2),
}

img_folder = "images/"
file_type = ".jpg"

reverses = ["ZB", "ZC", "ZE"]

def is_holo(cid):
    return cid in reverses 

def get_images(cid):

    def get_file_name(index):
        img = img_folder + cid + str(index)
        if is_holo(cid):
            img += "R"
        img += file_type
        return img

    return list(map(lambda index: get_file_name(index), 
                    range(1, config[cid][1] + 1)))

def get_name(cid):
    name = config[cid][0]
    if name == 0:
        return "Holo"
    elif name == 1:
        return "Reverse Holo"
    else:
        return name

welcome_msg = """Selling this entire Charizard collection for $45,000 SGD. 
    Contact me <a href="https://www.carousell.sg/zard9/">@zard9</a> on
    CarousellSG.""" 

related_links = {
   # "pikachu"   :   "https://www.google.com",
   # "raichu"    :   "https://www.facebook.com"
}
