from config import *

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>avian9 Pokemon Collection</title>
        <link href="https://fonts.googleapis.com/css?family=Oswald:300,400|Roboto|Open+Sans:300,400,700" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css">
        <link rel="stylesheet" href="main.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
    
    {body:s}

    </body>
</html>"""

welcome = """
    <div class="welcome">
        <h2> {msg:s} </h2>
        {links:s}
    </div>
    """

carousel = """
     <div class="container">
            <h1> {name:s} </h1>
            <div id="{cid:s}" class="carousel slide" data-ride="carousel">
                <!-- Carousel indicators -->
                <ol class="carousel-indicators">
                    {cindicators:s}
                </ol>   
                <!-- Wrapper for carousel items -->
                <div class="carousel-inner">
                    {citems:s}
                </div>
                <!-- Carousel controls -->
                <a class="carousel-control left" href="#{cid:s}" data-slide="prev">
                    <span><i class="fa fa-angle-left"></i></span>
                </a>
                <a class="carousel-control right" href="#{cid:s}" data-slide="next">
                    <span><i class="fa fa-angle-right"></i></span>
                </a>
            </div>
        </div>"""

cindicator_first = """
                    <li data-target="#{cid:s}" data-slide-to="0" class="active"></li>"""

cindicator = """
                    <li data-target="#{cid:s}" data-slide-to="{slide:d}"></li>"""

citem_first = """
                    <div class="item active">
                        <img src="{img:s}" alt="">
                    </div>"""

citem = """
                    <div class="item">
                        <img src="{img:s}" alt="">
                    </div>"""

link = """
        <a href="{href:s}">{title:s}</a>"""

def generate_welcome():
    def generate_links():
        return '<br>'.join(list(map(lambda title:
                link.format(href=related_links[title], title=title),
                        related_links)))

    return welcome.format(msg=welcome_msg, links=generate_links()) 

def generate_navbar():
    navitems = ''.join(list(map(lambda cid:
        navitem.format(name=get_name(cid), cid=cid), config)))
    return navbar.format(navitems=navitems)


def generate_carousel(cid):
    name = get_name(cid)
    images = get_images(cid)

    def generate_cindicators(cid, num_slides):
        return cindicator_first.format(cid=cid) + ''.join(
            list(map(lambda i: cindicator.format(cid=cid, slide=i), 
                         range(1, num_slides))))

    def generate_citems(images):
        return citem_first.format(img=images[0]) + ''.join(
            list(map(lambda i: citem.format(img=images[i]), 
                             range(1, len(images)))))

    cindicators = generate_cindicators(cid, len(images))
    citems = generate_citems(images)

    return carousel.format(name=name, cid=cid, cindicators=cindicators,
                           citems=citems)

def generate_site():
    body = generate_welcome() + \
            ''.join(list(map(lambda name:
                                                generate_carousel(name), config)))
    site = html.format(body=body)
    with open('index.html', 'w') as f:
        f.write(site)

generate_site()
