# Artist entries, part A: artists whose images came from Wikimedia Commons (round 1).
# Each work: (source, title, kind, year, medium, note, collection)
# source is "discovery/<slug>/<file>" (Commons manifest supplies credit + sourceUrl).

ARTISTS = {}

ARTISTS['neri-oxman'] = dict(
    name='Neri Oxman', born=1976, died=None, birthplace='Haifa, Israel', basedIn='New York',
    nationality='Israeli-American', categories=['bio-science', 'code'],
    mediums=['Architecture', 'Design', 'Biomaterials', '3D printing', 'Computational design'],
    tags=['Material ecology', 'Silk Pavilion', 'Biomaterials', 'Digital fabrication', 'Mediated Matter', 'Nature-inspired design'],
    bio=("Neri Oxman (born 1976) is an architect, designer and researcher who coined the term 'Material Ecology' for design that is grown, "
         "computed and fabricated together with natural systems. She studied medicine and architecture in Israel and London before a PhD at MIT, "
         "where she founded the Mediated Matter group at the MIT Media Lab. Her work moves between the lab and the gallery: 3D-printed "
         "objects whose material properties vary across their surface (Raycounting, Monocoque, Beast), wearable pieces made with Iris van Herpen, "
         "printed glass, and structures made with living organisms, most famously the Silk Pavilion (2013), whose silk was spun by "
         "thousands of silkworms on a robotically woven frame. MoMA gave her a solo exhibition, 'Material Ecology', in 2020. "
         "That year she left MIT and founded the design company OXMAN in New York."),
    studyNotes=[
        "The organism is a collaborator. In the Silk Pavilion a robot lays down a scaffold and the silkworms finish it, so the final form is negotiated between a program and an animal's behaviour.",
        "Variation across one material. Instead of assembling parts, she grades stiffness, colour or opacity continuously through a single printed object. Look at Monocoque and Beast and ask where the 'joints' have gone.",
        "Computation as a way of reading nature. Many works start from a simulation of light, heat or force, then use that data to decide where material goes.",
        "The lab and the museum are one practice. Prototypes, diagrams and research photos are shown alongside finished objects; the process is part of the work.",
    ],
    links=[('MoMA: Neri Oxman: Material Ecology (2020)', 'https://www.moma.org/calendar/exhibitions/5090'),
           ('OXMAN', 'https://oxman.com'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Neri_Oxman')],
    portrait='discovery/neri-oxman/c28.jpg',
    works=[
        ('discovery/neri-oxman/c12.png', 'Silk Pavilion', 'installation', '2013', 'Silk spun by about 6,500 silkworms over a CNC-woven silk scaffold', 'A robot wove a base frame of silk threads, then the silkworms were released onto it and filled in the gaps, guided by light and heat.', 'MIT Media Lab'),
        ('discovery/neri-oxman/c13.png', 'Silk Pavilion (silkworms at work)', 'installation', '2013', 'Live silkworms on the woven scaffold', None, None),
        ('discovery/neri-oxman/c26.jpg', 'Silkworm spinning on a flat surface', 'photograph', 'c. 2013', 'Research photograph', 'Studies of how silkworms respond to flat and curved surfaces informed the pavilion\'s design.', None),
        ('discovery/neri-oxman/c08.jpg', 'Raycounting', 'sculpture', '2007', 'Silk-coated nylon, 3D printed', 'Form generated from how light falls across a surface.', 'Museum of Modern Art, New York'),
        ('discovery/neri-oxman/c18.jpg', 'Monocoque', 'sculpture', '2007', '3D-printed resin', 'A skin that is also its own structure, with thickness varying where it carries load.', None),
        ('discovery/neri-oxman/c19.jpg', 'Cartesian Wax', 'sculpture', '2007', 'Resin tiles', None, None),
        ('discovery/neri-oxman/c10.jpg', 'Beast (prototype chaise longue)', 'sculpture', '2010', 'Multi-material 3D print', 'Material stiffness varies across the surface in response to the pressure of a seated body.', None),
        ('discovery/neri-oxman/c09.jpg', 'Anthozoa (with Iris van Herpen and Craig Carter)', 'sculpture', '2013', 'Multi-material 3D-printed garment', None, None),
        ('discovery/neri-oxman/c30.png', 'Glass bowl from G3DP (Glass 3D printing)', 'sculpture', '2015', 'Additively manufactured optically transparent glass', None, None),
    ],
)

ARTISTS['heather-dewey-hagborg'] = dict(
    name='Heather Dewey-Hagborg', born=1982, died=None, birthplace=None, basedIn='New York',
    nationality='American', categories=['bio-science', 'code'],
    mediums=['Sculpture', 'Installation', 'Software', 'Biotechnology', 'Video'],
    tags=['DNA phenotyping', 'Biohacking', 'Genetic surveillance', 'Stranger Visions', 'Forensics', 'Privacy', 'Portraiture'],
    bio=("Heather Dewey-Hagborg (born 1982) is an information artist and biohacker whose work asks what can be read about a person from "
         "the biological traces they leave behind. For Stranger Visions (2012–13) she collected hairs, chewing gum and cigarette ends from the "
         "streets of New York, extracted and analysed the DNA in a community biology lab, and used software to generate 3D-printed portraits of "
         "what the anonymous strangers might look like. Invisible (2014) answered with a pair of sprays to erase and obscure the DNA one "
         "leaves in public. With Chelsea Manning she made Probably Chelsea (2017), thirty possible faces generated from Manning's DNA, "
         "showing how much the same genome can be read in different ways. She has a PhD in Electronic Arts from Rensselaer Polytechnic Institute, "
         "and her early work used software, AI and sound before she turned to genetics."),
    studyNotes=[
        "Start with a found sample. The work begins on the street, with gum and hair; the collecting walk is as much a part of the method as the lab.",
        "Code and biology in one pipeline. Sequencing, a statistical model and a 3D printer each make decisions; the portrait is only as 'true' as the assumptions inside the software.",
        "The portrait as a critique. The faces look convincing, which is the point: they show how forensic phenotyping can produce confident images from uncertain data.",
        "Make the counter-tool too. Invisible turns the critique into a product with packaging and a launch video, so the work operates in the world rather than only describing it.",
    ],
    links=[('Artist website', 'https://deweyhagborg.com'),
           ('Stranger Visions', 'https://deweyhagborg.com/projects/stranger-visions'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Heather_Dewey-Hagborg')],
    portrait='discovery/heather-dewey-hagborg/c21.jpg',
    works=[
        ('discovery/heather-dewey-hagborg/c13.jpg', 'Stranger Visions', 'installation', '2012–13', '3D-printed portraits generated from DNA, with samples and documentation', 'Each face is a computational guess at the person who left a hair or a cigarette end on a New York street.', None),
        ('discovery/heather-dewey-hagborg/c17.jpg', 'Stranger Visions: Sample 3', 'sculpture', '2012', 'Full-colour 3D print generated from DNA analysis', None, None),
        ('discovery/heather-dewey-hagborg/c15.jpg', 'Stranger Visions: collected sample (chewing gum)', 'photograph', '2012', 'Documentation photograph', 'Discarded chewing gum, one of the samples collected for the project.', None),
        ('discovery/heather-dewey-hagborg/c16.jpg', 'Stranger Visions: collected sample (cigarette end, Myrtle Avenue, Brooklyn)', 'photograph', '2012', 'Documentation photograph', None, None),
        ('discovery/heather-dewey-hagborg/c10.jpg', 'Invisible', 'sculpture', '2014', 'Two sprays (Erase and Replace) with packaging', 'One spray removes DNA traces; the other masks what remains with noise.', None),
        ('discovery/heather-dewey-hagborg/c12.jpg', 'Invisible (video still)', 'film', '2014', 'Video', None, None),
    ],
)

ARTISTS['sheila-hicks'] = dict(
    name='Sheila Hicks', born=1934, died=None, birthplace='Hastings, Nebraska', basedIn='Paris',
    nationality='American', categories=['fibre'],
    mediums=['Weaving', 'Fibre sculpture', 'Installation', 'Textile'],
    tags=['Fibre art', 'Colour', 'Minimes', 'Wrapped bundles', 'Soft sculpture', 'Architecture'],
    bio=("Sheila Hicks (born 1934) studied painting at Yale under Josef Albers before turning to thread. Travels in South America, where she "
         "studied pre-Columbian textiles, set the direction of her work, and she has lived in Paris since 1964. She works at two extremes: "
         "'minimes', small weavings made on a portable frame loom that she treats like sketchbook pages, and monumental works for "
         "architecture, from wall hangings for corporate lobbies to cascades of wrapped and bundled fibre that spill across floors and walls. "
         "Linen, wool, silk, cotton and synthetic fibres are wrapped, knotted, stacked and piled in saturated colour. Major works include The "
         "Principal Wife (1964–68, MoMA), Escalade Beyond Chromatic Lands at the 2017 Venice Biennale, and the 2018 retrospective 'Lignes de vie' "
         "at the Centre Pompidou."),
    studyNotes=[
        "Keep a small format going. The minimes are a daily practice; ideas are tested at palm size before they reach architectural scale.",
        "Colour is physical. Pigment sits inside the fibre, so a colour changes with how tightly a bundle is wrapped and how the light falls across it.",
        "Gravity does the composing. Many pieces are piled, hung or let fall, so their final shape is partly decided by weight and the site.",
        "Think architecture. Her large works are made for specific rooms, and she often lets them flow over thresholds and corners.",
    ],
    links=[('Centre Pompidou: Sheila Hicks, Lignes de vie (2018)', 'https://www.centrepompidou.fr/en/program/calendar/event/c9EKaEn'),
           ('MoMA collection', 'https://www.moma.org/artists/2640'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Sheila_Hicks')],
    portrait='discovery/sheila-hicks/c02.jpg',
    works=[
        ('discovery/sheila-hicks/c26.jpg', 'Wrapped columns (exhibition view, Textile Museum of Canada)', 'installation', 'Photo 2016', 'Wrapped fibre', 'Bundles of thread tightly wrapped in bands of colour.', None),
        ('discovery/sheila-hicks/c28.jpg', 'Coiled bundle (exhibition view, Textile Museum of Canada)', 'sculpture', 'Photo 2016', 'Linen and wool fibre', None, None),
        ('discovery/sheila-hicks/c30.jpg', 'Wrapped fibre hanging (exhibition view, Textile Museum of Canada)', 'installation', 'Photo 2016', 'Wrapped fibre', None, None),
        ('discovery/sheila-hicks/c25.jpg', 'Fibre cascade at the Château de Chaumont-sur-Loire', 'installation', 'Photo 2018', 'Fibre installation', None, None),
        ('discovery/sheila-hicks/c24.jpg', 'Hanging at the Château de Chaumont-sur-Loire', 'installation', 'Photo 2018', 'Fibre installation', None, None),
        ('discovery/sheila-hicks/c23.jpg', 'Exhibition at Demisch Danant, New York', 'sculpture', 'Photo 2019', 'Fibre', None, None),
        ('discovery/sheila-hicks/c05.jpg', 'Wall hanging at the Stedelijk Museum, Amsterdam', 'sculpture', 'Photo 1974', 'Woven and wrapped fibre', 'From her 1974 exhibition of wall hangings and textile sculptures at the Stedelijk.', None),
    ],
)

ARTISTS['el-anatsui'] = dict(
    name='El Anatsui', born=1944, died=None, birthplace='Anyako, Ghana', basedIn='Nsukka, Nigeria',
    nationality='Ghanaian', categories=['fibre'],
    mediums=['Sculpture', 'Installation', 'Wood', 'Metal'],
    tags=['Bottle caps', 'Found materials', 'Cloth', 'Kente', 'Nsukka School', 'Large-scale'],
    bio=("El Anatsui (born 1944) trained at Kwame Nkrumah University of Science and Technology in Kumasi and taught for decades at the "
         "University of Nigeria, Nsukka. His early work was carved and burned wood, often cut with a chainsaw and marked with signs drawn from "
         "West African writing systems. From the late 1990s he began joining thousands of aluminium caps and seals from liquor bottles with "
         "copper wire into huge, flexible sheets. They hang like cloth, recalling kente and other textiles, while carrying histories of trade, "
         "consumption and colonial exchange in their material. The sheets have no fixed shape: each installation folds and drapes them anew. "
         "He received the Golden Lion for Lifetime Achievement at the 2015 Venice Biennale and made Behind the Red Moon for Tate Modern's "
         "Turbine Hall in 2023."),
    studyNotes=[
        "A material with a past. Each bottle cap carries a brand, a drink and a trade route; the work is built from that history, not just from metal.",
        "Metal that behaves like cloth. Stitching small rigid units with wire turns them into a fabric that can fold, drape and hang.",
        "No fixed form. He lets installers decide how a sheet is folded, so the same work changes from venue to venue.",
        "Labour and community. The sheets are made by teams of assistants in his studio; repetition and collective making are part of the meaning.",
    ],
    links=[('Tate Modern: El Anatsui, Behind the Red Moon (2023)', 'https://www.tate.org.uk/whats-on/tate-modern/hyundai-commission-el-anatsui'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/El_Anatsui')],
    portrait=None,
    works=[
        ('discovery/el-anatsui/c15.jpg', 'Energy Spill', 'sculpture', '2010', 'Aluminium bottle caps and copper wire', None, 'Private collection'),
        ('discovery/el-anatsui/c16.jpg', 'Energy Spill (detail)', 'sculpture', '2010', 'Aluminium bottle caps and copper wire', None, 'Private collection'),
        ('discovery/el-anatsui/c06.jpg', 'Nukae-1', 'sculpture', '2006', 'Aluminium and copper wire', 'Part of the Gawu series of metal "cloths".', None),
        ('discovery/el-anatsui/c07.jpg', 'Nukae-1 (detail)', 'sculpture', '2006', 'Aluminium and copper wire', None, None),
        ('discovery/el-anatsui/c01.jpg', "Man's Cloth", 'sculpture', '1998–2001', 'Aluminium bottle tops and copper wire', None, 'British Museum, London'),
        ('discovery/el-anatsui/c02.jpg', "Man's Cloth (detail)", 'sculpture', '1998–2001', 'Aluminium bottle tops and copper wire', None, 'British Museum, London'),
        ('discovery/el-anatsui/c09.jpg', 'Broken Bridge II', 'installation', '2012', 'Pressed tin and mirrors', 'A wall installation along the High Line in New York.', None),
        ('discovery/el-anatsui/c20.jpg', 'Early wood reliefs', 'sculpture', '1990s', 'Tropical hardwood, cut and burned', 'Shown in Nigerian Modernism at Tate Modern, London.', None),
    ],
)

ARTISTS['do-ho-suh'] = dict(
    name='Do Ho Suh', born=1962, died=None, birthplace='Seoul, South Korea', basedIn='London',
    nationality='Korean', categories=['fibre'],
    mediums=['Sculpture', 'Installation', 'Fabric', 'Drawing', 'Printmaking'],
    tags=['Home', 'Memory', 'Translucent fabric', 'Architecture', 'Displacement', 'Scale'],
    bio=("Do Ho Suh (born 1962) studied oriental painting in Seoul before moving to the United States, where he studied at the Rhode Island "
         "School of Design and Yale. His best-known works are full-scale replicas of the places he has lived, sewn from translucent polyester "
         "fabric: his childhood home in Seoul, his apartment and corridor at 348 West 22nd Street in New York, stairs, doorways and light switches, "
         "all rendered in luminous colour and hung so that visitors can walk through them. The fabric makes architecture portable and "
         "weightless, like a memory carried from place to place. He also makes works about the individual and the collective, such as "
         "fields of tiny figures holding up a floor or a wall, and 'rubbing' works that trace the surfaces of a building in pencil. Fallen "
         "Star (2012) at UC San Diego sets a small house tilted on the corner of a campus building."),
    studyNotes=[
        "Memory as a measured copy. He measures his homes precisely, then remakes them in a material that cannot keep them solid.",
        "Translucency changes architecture. Walls you can see through make every room a view of the next one; colour codes each space.",
        "The detail carries the weight. Light switches, door handles and radiators are sewn at full scale, and they are what make the spaces feel lived in.",
        "One and many. The figure works ask how individuals add up to a crowd or a structure; look at how the scale shifts as you move closer.",
    ],
    links=[('Tate: Staircase-III', 'https://www.tate.org.uk/art/artworks/suh-staircase-iii-t13368'),
           ('Lehmann Maupin', 'https://www.lehmannmaupin.com/artists/do-ho-suh'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Do_Ho_Suh')],
    portrait=None,
    works=[
        ('discovery/do-ho-suh/c01.jpg', 'Staircase-III', 'installation', '2010', 'Polyester and stainless steel', 'A full-size staircase from his New York building, sewn in red fabric and suspended at ceiling height.', 'Tate'),
        ('discovery/do-ho-suh/c09.jpg', 'New York apartment, in fabric', 'installation', 'Photo c. 2018', 'Polyester fabric and stainless steel', 'A walk-through fabric replica of rooms from his New York home, shown at Bristol Museum & Art Gallery.', None),
        ('discovery/do-ho-suh/c08.jpg', 'New York apartment, in fabric (detail)', 'installation', 'Photo c. 2018', 'Polyester fabric and stainless steel', None, None),
        ('discovery/do-ho-suh/c03.jpg', 'Bridging Home', 'installation', '2010', 'Mixed media', 'A traditional Korean house wedged between two buildings in Liverpool, made for the Liverpool Biennial.', None),
        ('discovery/do-ho-suh/c05.jpg', 'Bridging Home (street view)', 'installation', '2010', 'Mixed media', None, None),
        ('discovery/do-ho-suh/c10.jpg', 'Fallen Star', 'installation', '2012', 'Cottage on the roof edge of Jacobs Hall', 'A small blue house set at a tilt on the edge of a seventh-storey building.', 'Stuart Collection, University of California San Diego'),
        ('discovery/do-ho-suh/c13.jpg', 'Wall of cast figures, U.S. Food and Drug Administration', 'installation', 'Photo c. 2014', 'Cast resin figures', 'Thousands of small figures in shifting colours, interlocked into a wall.', 'U.S. Food and Drug Administration, White Oak campus, Maryland'),
        ('discovery/do-ho-suh/c29.jpg', 'Wall of cast figures (detail)', 'installation', 'Photo c. 2014', 'Cast resin figures', None, 'U.S. Food and Drug Administration, White Oak campus, Maryland'),
    ],
)

ARTISTS['felix-gonzalez-torres'] = dict(
    name='Felix Gonzalez-Torres', born=1957, died=1996, birthplace='Guáimaro, Cuba', basedIn='New York',
    nationality='Cuban-American', categories=['concept'],
    mediums=['Installation', 'Sculpture', 'Photography', 'Billboards', 'Paper stacks', 'Light strings'],
    tags=['Candy spills', 'Paper stacks', 'Participation', 'Loss', 'AIDS crisis', 'Minimalism', 'Love'],
    bio=("Felix Gonzalez-Torres (1957–1996) was born in Cuba and lived in New York from 1979. He was a member of the collective Group "
         "Material and made a body of work that uses the forms of Minimalism and Conceptual art to speak about love, loss and public life during "
         "the AIDS crisis. His works are often defined by instructions rather than objects: piles of wrapped sweets that visitors may take from "
         "and that are replenished; stacks of printed paper sheets to be carried away; strings of light bulbs; pairs of synchronised clocks; "
         "billboards of an empty, unmade bed. 'Untitled' (Portrait of Ross in L.A.) (1991) begins with 175 pounds of candy, the ideal body weight "
         "of his partner Ross Laycock, who died of AIDS-related illness in 1991. Gonzalez-Torres died in 1996; he represented the United States at "
         "the Venice Biennale posthumously in 2007."),
    studyNotes=[
        "One concept, many forms. Candy, paper, clocks, light bulbs, billboards and text all carry the same idea of a body that is present and diminishing.",
        "The work is a set of instructions. Owners receive a certificate and guidelines; each installation can be different in size and shape, so the idea, not the object, is the artwork.",
        "Participation completes it. Visitors take a sweet or a sheet; the work only means something when it is shared and slowly disappears.",
        "Restraint carries emotion. The forms look cool and minimal, but titles and materials load them with love and grief. Look at what is left unsaid.",
    ],
    links=[('Felix Gonzalez-Torres Foundation', 'https://www.felixgonzalez-torresfoundation.org'),
           ('Art Institute of Chicago: "Untitled" (Portrait of Ross in L.A.)', 'https://www.artic.edu/artworks/152961/untitled-portrait-of-ross-in-l-a'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Felix_Gonzalez-Torres')],
    portrait=None,
    works=[
        ('discovery/felix-gonzalez-torres/c04.jpg', '"Untitled" (Portrait of Ross in L.A.)', 'installation', '1991', 'Candies individually wrapped in multicoloured cellophane, endless supply; ideal weight 175 lb', 'Visitors may take a sweet; the pile is replenished, so it shrinks and is restored again and again.', 'Art Institute of Chicago'),
        ('discovery/felix-gonzalez-torres/c05.jpg', '"Untitled" (Portrait of Ross in L.A.), a visitor taking a sweet', 'installation', '1991', 'Candies in cellophane, endless supply', None, None),
        ('discovery/felix-gonzalez-torres/c17.jpg', '"Untitled" (Perfect Lovers)', 'sculpture', '1987–1990', 'Two clocks, side by side, initially set to the same time', 'Two identical wall clocks start in sync and will drift apart; when one stops, it is reset.', 'Glenstone'),
        ('discovery/felix-gonzalez-torres/c03.jpg', '"Untitled"', 'installation', '1989', 'Billboard', 'A billboard over Sheridan Square, near the Stonewall Inn, listing dates from gay history and the AIDS crisis.', None),
        ('discovery/felix-gonzalez-torres/c25.jpg', '"Untitled" (Republican Years)', 'installation', '1992', 'Print on paper, endless copies', 'A stack of sheets visitors can take away.', None),
        ('discovery/felix-gonzalez-torres/c14.jpg', '"Untitled" (Lovers – Paris)', 'installation', '1993', 'Light bulbs, porcelain light sockets, extension cords', None, 'National Gallery of Art, Washington'),
        ('discovery/felix-gonzalez-torres/c21.jpg', '"Untitled" (Water)', 'installation', '1995', 'Strands of beads and hanging device', 'A curtain of blue beads that visitors pass through.', 'Baltimore Museum of Art'),
        ('discovery/felix-gonzalez-torres/c16.jpg', '"Untitled" (Passport)', 'installation', '1991', 'Paper, endless copies', None, None),
        ('discovery/felix-gonzalez-torres/c18.jpg', '"Untitled" (text portrait)', 'installation', '1989', 'Paint on wall', 'A frieze of events and dates that together form a portrait.', None),
    ],
)

ARTISTS['pipilotti-rist'] = dict(
    name='Pipilotti Rist', born=1962, died=None, birthplace='Grabs, Switzerland', basedIn='Zurich',
    nationality='Swiss', categories=['concept', 'light'],
    mediums=['Video installation', 'Film', 'Public art', 'Design', 'Music'],
    tags=['Immersive video', 'Colour', 'Body', 'Pleasure', 'Projection', 'Pop music'],
    bio=("Pipilotti Rist (born 1962) studied commercial art, illustration and photography in Vienna and video in Basel, and played in the band "
         "Les Reines Prochaines. Her early single-channel videos, such as I'm Not The Girl Who Misses Much (1986), distort pop songs and her own "
         "body; Ever Is Over All (1997), in which a woman smashes car windows with a flower while a police officer salutes, won a prize at the "
         "Venice Biennale. She went on to fill whole rooms with projected colour: Pour Your Body Out (7354 Cubic Meters) took over MoMA's atrium "
         "in 2008, and Pixel Forest (2016) hangs thousands of LEDs like rain. She also works in public space: a bright pink tram for Geneva, a red "
         "rubber 'city lounge' in St. Gallen (with Carlos Martinez), illuminated lamp sculptures. Her one feature film, Pepperminta, was released in 2009."),
    studyNotes=[
        "Same sensibility, any medium. Song, single-channel video, room-sized projection, furniture, a tram, a public square: the colour, humour and bodily closeness stay the same.",
        "Design the viewer's body. She adds sofas, carpets, cushions and beds so people lie down and look up; posture changes how video is watched.",
        "Projection meets architecture. Images are thrown onto ceilings, corners, objects and floors instead of a screen; look for how the edges of the image are handled.",
        "Joy as a critical tool. Pleasure and playfulness are used to question how women's bodies are shown, not just to entertain.",
    ],
    links=[('Hauser & Wirth', 'https://www.hauserwirth.com/artists/2808-pipilotti-rist/'),
           ('MoMA: Pour Your Body Out (2008)', 'https://www.moma.org/calendar/exhibitions/84'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Pipilotti_Rist')],
    portrait='discovery/pipilotti-rist/c24.jpg',
    works=[
        ('discovery/pipilotti-rist/c18.jpg', 'Pepperminta (film still)', 'film', '2009', 'Feature film, colour', None, None),
        ('discovery/pipilotti-rist/c19.jpg', 'The Room (Das Zimmer)', 'installation', '1994/2000', 'Audio-video installation with oversized furniture', 'Visitors sit on an outsized armchair and sofa and watch a small TV, made to feel like children.', None),
        ('discovery/pipilotti-rist/c01.jpg', 'Projection installation at Mudam, Luxembourg', 'installation', 'Photo 2006', 'Video projection', 'From the museum\'s opening exhibition.', None),
        ('discovery/pipilotti-rist/c03.jpg', 'Monochrome Rose (interior)', 'installation', '2016', 'Tram painted and fitted out in pink, Geneva', 'A working tram in which everything, inside and out, is pink.', None),
        ('discovery/pipilotti-rist/c06.jpg', 'Monochrome Rose', 'installation', '2016', 'Tram, Geneva', None, None),
        ('discovery/pipilotti-rist/c23.jpg', 'Stadtlounge (with Carlos Martinez)', 'installation', '2005', 'Red rubber granulate covering a city square, furniture and lighting', 'A public square in St. Gallen treated as an outdoor living room.', None),
        ('discovery/pipilotti-rist/c26.jpg', 'Tastende Lichter', 'installation', '2020', 'Projection onto architecture, Zurich', None, None),
        ('discovery/pipilotti-rist/c29.jpg', 'Wasting Life on You', 'installation', '2025', 'Light installation', None, 'Depot Boijmans Van Beuningen, Rotterdam'),
    ],
)

ARTISTS['james-turrell'] = dict(
    name='James Turrell', born=1943, died=None, birthplace='Los Angeles, California', basedIn='Flagstaff, Arizona',
    nationality='American', categories=['light'],
    mediums=['Light installation', 'Architecture', 'Land art'],
    tags=['Light and Space', 'Skyspace', 'Ganzfeld', 'Perception', 'Roden Crater', 'Projection pieces'],
    bio=("James Turrell (born 1943) studied perceptual psychology at Pomona College before turning to art in Los Angeles, where he became "
         "a central figure in the Light and Space movement. His first works, from 1966, were projection pieces in which a beam of light "
         "seems to become a solid shape in the corner of a dark room. He went on to make Skyspaces, chambers with an opening in the roof that "
         "frame the sky as a flat field of colour, Ganzfelds that dissolve all sense of depth, and works that use the architecture of whole "
         "buildings. Since 1979 he has been transforming Roden Crater, an extinct volcano in Arizona, into a naked-eye observatory. Aten Reign "
         "(2013) filled the rotunda of the Guggenheim with changing coloured light. He received the National Medal of Arts in 2013."),
    studyNotes=[
        "Light is the material, perception is the subject. There is often no object at all; what you see is your own eye adjusting.",
        "Frame the sky. A Skyspace is an aperture with a carefully shaped edge, so the sky reads as a painted surface on the ceiling. Watch how dusk changes it.",
        "Time is part of the work. Many pieces need several minutes of looking before they change; the duration is designed.",
        "Architecture as instrument. Rooms are built to remove edges, shadows and reference points, and that precise construction is what makes the light seem to float.",
    ],
    links=[('Artist website', 'https://jamesturrell.com'),
           ('Roden Crater', 'https://rodencrater.com'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/James_Turrell')],
    portrait='discovery/james-turrell/c29.jpg',
    works=[
        ('discovery/james-turrell/c17.jpg', 'Aten Reign', 'installation', '2013', 'Daylight and LED light, Solomon R. Guggenheim Museum', 'Two views of the rotunda, transformed into nested rings of shifting colour.', None),
        ('discovery/james-turrell/c28.jpg', 'Dividing the Light', 'installation', '2007', 'Skyspace with LED lighting', 'A canopy over a pool frames the sky; at dusk, lights shift the colour around the opening.', 'Pomona College, Claremont'),
        ('discovery/james-turrell/c21.jpg', 'Alta Pink', 'installation', '1968', 'Projected light (projection piece)', 'A beam of light projected into a corner reads as a solid, glowing pyramid.', None),
        ('discovery/james-turrell/c19.jpg', 'Raemar Magenta', 'installation', 'Raemar series, from 1968', 'Light installation (shallow space construction)', 'Shown in the stables at Houghton Hall, Norfolk.', None),
        ('discovery/james-turrell/c36.jpg', 'Three Gems', 'installation', '2005', 'Skyspace, stucco and concrete', None, 'de Young Museum, San Francisco'),
        ('discovery/james-turrell/c06.jpg', 'Skyspace, Piz Uter (interior)', 'installation', '2005', 'Skyspace', None, 'Zuoz, Switzerland'),
        ('discovery/james-turrell/c13.jpg', 'Cat Cairn: The Kielder Skyspace', 'installation', '2000', 'Skyspace, stone', None, 'Kielder Water & Forest Park, Northumberland'),
        ('discovery/james-turrell/c01.jpg', 'Roden Crater', 'installation', '1979–ongoing', 'Extinct volcanic crater, Painted Desert, Arizona', 'An extinct volcano being turned into a sequence of chambers and tunnels for viewing the sky.', None),
    ],
)

ARTISTS['dan-flavin'] = dict(
    name='Dan Flavin', born=1933, died=1996, birthplace='Jamaica, Queens, New York', basedIn='New York',
    nationality='American', categories=['light'],
    mediums=['Fluorescent light', 'Installation', 'Drawing'],
    tags=['Minimalism', 'Fluorescent tubes', 'Colour', 'Readymade', 'Site-specific', 'Corners'],
    bio=("Dan Flavin (1933–1996) made art from commercially available fluorescent tubes, in standard lengths and a limited range of colours. "
         "His first such work, the diagonal of May 25, 1963 (to Constantin Brancusi), was a single gold tube fixed at an angle to a wall. "
         "From then on he arranged tubes and fixtures in corners, across corridors and through whole buildings, letting coloured light flood "
         "the surrounding space. He dedicated many works to friends and artists, including the long series of 'monuments' for V. Tatlin. Late "
         "works include a church in Milan (Santa Maria Annunciata in Chiesa Rossa), Richmond Hall at the Menil Collection in Houston, and six "
         "buildings at the Chinati Foundation in Marfa, all completed around the time of his death in 1996."),
    studyNotes=[
        "Off-the-shelf parts, strict rules. He used only standard tubes and fixtures; the creativity is in placement, colour and dedication.",
        "The light spills beyond the object. The tubes are the source, but the work is the coloured space and wall they produce. Notice where colours mix.",
        "Corners and corridors. He often used architectural edges to split and frame the light, turning a room into the composition.",
        "Titles as dedications. Each piece names a person or an event; the industrial material is given a personal address.",
    ],
    links=[('Dia Art Foundation', 'https://www.diaart.org/'),
           ('Chinati Foundation', 'https://chinati.org'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Dan_Flavin')],
    portrait=None,
    works=[
        ('discovery/dan-flavin/c11.jpg', 'untitled (to Donald Judd, colorist) 1–5', 'installation', '1987', 'Fluorescent light fixtures with coloured tubes', None, 'Tate'),
        ('discovery/dan-flavin/c35.jpg', '"monument" for V. Tatlin', 'sculpture', '1966', 'Cool white fluorescent light', 'One of a series of works, made over decades, honouring the Russian Constructivist Vladimir Tatlin.', 'National Gallery of Art, Washington'),
        ('discovery/dan-flavin/c10.jpg', 'untitled (Santa Maria Annunciata in Chiesa Rossa)', 'installation', '1996', 'Fluorescent light in green, blue, pink, gold and ultraviolet', 'His last work, completed just after his death, lighting the nave, transept and apse of a church in Milan.', None),
        ('discovery/dan-flavin/c14.jpg', 'untitled (Marfa project)', 'installation', '1996', 'Fluorescent light in six buildings', None, 'Chinati Foundation, Marfa, Texas'),
        ('discovery/dan-flavin/c08.jpg', 'untitled (Richmond Hall)', 'installation', '1996', 'Fluorescent light', 'Green tubes run along the outside of the building; the interior is lit in coloured light.', 'Menil Collection, Houston'),
        ('discovery/dan-flavin/c19.jpg', 'to the people of Baden-Baden', 'installation', '1989', 'Red and yellow fluorescent light on a building facade', None, 'Staatliche Kunsthalle Baden-Baden'),
        ('discovery/dan-flavin/c34.jpg', 'untitled (for Eric Zetterquist)', 'sculpture', '1990', 'Fluorescent light', None, 'Situation Kunst, Bochum'),
        ('discovery/dan-flavin/c02.jpg', 'quietly, to the memory of Mia Visser', 'installation', '1977', 'Fluorescent light', None, 'Kröller-Müller Museum, Otterlo'),
    ],
)

ARTISTS['carlos-cruz-diez'] = dict(
    name='Carlos Cruz-Diez', born=1923, died=2019, birthplace='Caracas, Venezuela', basedIn='Paris',
    nationality='Venezuelan', categories=['light'],
    mediums=['Painting', 'Sculpture', 'Public art', 'Installation', 'Print'],
    tags=['Op art', 'Kinetic art', 'Physichromie', 'Colour theory', 'Chromosaturation', 'Public space'],
    bio=("Carlos Cruz-Diez (1923–2019) was a Venezuelan artist who spent his career showing that colour is not fixed to an object but is an event "
         "that happens in space and time, in front of the viewer. Working in Caracas and, from 1960, in Paris, he developed a set of research "
         "series that he pursued for six decades: Physichromies, panels of thin vertical blades that produce colours not present in the paint as "
         "the viewer moves; Induction Chromatique; Chromointerférences; Transchromies made with overlapping coloured transparent plastics; and "
         "Chromosaturation rooms flooded with red, green and blue light. He also worked at the scale of cities, from the floors and walls of "
         "Simón Bolívar International Airport at Maiquetía to pedestrian crossings and public sculpture."),
    studyNotes=[
        "Colour happens in the eye. Many colours you see in a Physichromie are not painted anywhere; they are produced by adjacent blades and your movement.",
        "Move to see it. Walk past the works: the colour shifts with your position and the daylight, so time and the viewer are built in.",
        "Systematic research. He named and numbered his series like experiments and pursued them for decades, so each work is a variation on a rule.",
        "From the studio to the city. The same principles scale from a panel to an airport floor; look at how a public work holds up in sunlight and crowds.",
    ],
    links=[('Cruz-Diez Foundation', 'https://cruz-diez.com'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Carlos_Cruz-Diez')],
    portrait='discovery/carlos-cruz-diez/c21.jpg',
    works=[
        ('discovery/carlos-cruz-diez/c17.jpg', 'Ambientación de Color Aditivo (floor at Maiquetía airport)', 'installation', '1974–78', 'Floor of coloured stripes', 'Walking over the stripes, travellers see colours mix and change.', 'Simón Bolívar International Airport, Maiquetía, Venezuela'),
        ('discovery/carlos-cruz-diez/c26.jpg', 'Labyrinthe de Transchromie A', 'installation', '1965/2017', 'Coloured transparent panels', 'Overlapping coloured planes that recombine as visitors walk between them.', None),
        ('discovery/carlos-cruz-diez/c20.jpg', 'Physichromie, homage to Andrés Bello (double concave-convex)', 'sculpture', '1982', 'Painted metal blades on a curved double-sided structure', None, 'Plaza Venezuela, Caracas'),
        ('discovery/carlos-cruz-diez/c16.jpg', 'Arcos de Inducción Cromática para Margarita', 'sculpture', '1997', 'Painted metal arches', None, 'Porlamar, Margarita Island, Venezuela'),
        ('discovery/carlos-cruz-diez/c33.jpg', 'Fisicromía para Madrid', 'sculpture', '1991', 'Double-sided physichromie', None, 'Parque Juan Carlos I, Madrid'),
        ('discovery/carlos-cruz-diez/c09.jpg', 'Physichromie at the Universidad de Los Andes', 'sculpture', 'Photo 2010s', 'Painted metal blades', None, 'Universidad de Los Andes, Mérida, Venezuela'),
    ],
)

ARTISTS['olafur-eliasson'] = dict(
    name='Olafur Eliasson', born=1967, died=None, birthplace='Copenhagen, Denmark', basedIn='Berlin and Copenhagen',
    nationality='Danish-Icelandic', categories=['light'],
    mediums=['Installation', 'Sculpture', 'Architecture', 'Photography', 'Public art'],
    tags=['Perception', 'Weather', 'Climate', 'Light', 'Colour', 'Studio practice'],
    bio=("Olafur Eliasson (born 1967) grew up between Denmark and Iceland and studied at the Royal Danish Academy of Fine Arts. He runs a large "
         "studio in Berlin of craftspeople, architects, technicians and researchers. His work uses light, water, fog, mirrors, colour and "
         "temperature to make people aware of how they perceive. The weather project (2003) filled Tate Modern's Turbine Hall with a huge "
         "artificial sun in a haze, and visitors lay on the floor to watch themselves in the mirrored ceiling. He has made artificial waterfalls "
         "in New York (2008), a ring-shaped rainbow walkway on the roof of ARoS in Aarhus (Your rainbow panorama, 2011), blocks of Greenland "
         "ice left to melt in city squares (Ice Watch, from 2014), and the solar-powered lamp Little Sun (2012). He has increasingly turned his "
         "studio towards climate and social questions."),
    studyNotes=[
        "Show the mechanism. He often leaves the machinery (lamps, pumps, scaffolding) visible, so you see both the effect and how it is made.",
        "Viewers as the subject. Mirrors, coloured light and fog turn the audience into part of the picture; the work is about seeing yourself seeing.",
        "Phenomena over objects. Weather, colour and reflection are the material; he builds conditions rather than things.",
        "A studio as a lab. Look at the range of research, models and collaborations; the large works rest on years of small experiments with light and geometry.",
    ],
    links=[('Studio Olafur Eliasson', 'https://olafureliasson.net'),
           ('Tate: The weather project', 'https://www.tate.org.uk/whats-on/tate-modern/unilever-series/unilever-series-olafur-eliasson-weather-project'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Olafur_Eliasson')],
    portrait='discovery/olafur-eliasson/c22.jpg',
    works=[
        ('discovery/olafur-eliasson/c08.jpg', 'The weather project', 'installation', '2003', 'Monofrequency lamps, projection foil, haze machines, mirror foil, aluminium and scaffolding', 'A semicircle of yellow lamps, doubled by a mirrored ceiling into a sun, in Tate Modern\'s Turbine Hall.', None),
        ('discovery/olafur-eliasson/c11.jpg', 'Your rainbow panorama', 'installation', '2006–2011', 'Circular walkway of coloured glass on the museum roof', 'Walking the ring, the city outside changes colour step by step.', 'ARoS Aarhus Kunstmuseum'),
        ('discovery/olafur-eliasson/c01.jpg', 'The New York City Waterfalls', 'installation', '2008', 'Four temporary waterfalls on scaffolding', 'Water pumped from the East River and dropped from scaffolding towers, one under the Brooklyn Bridge.', None),
        ('discovery/olafur-eliasson/c12.jpg', 'Cold Wind Sphere', 'sculpture', '2012', 'Stainless steel, colour-effect filter glass, mirror, lamp', None, None),
        ('discovery/olafur-eliasson/c19.jpg', 'No future is possible without a past', 'sculpture', '2017', 'Polished metal ceiling sculpture', None, 'Bloomberg, London'),
        ('discovery/olafur-eliasson/c24.jpg', 'East window, Greifswald Cathedral', 'installation', '2024', 'Coloured glass', 'A window made as a homage to Caspar David Friedrich, in his home town.', 'Greifswald Cathedral, Germany'),
        ('discovery/olafur-eliasson/c33.jpg', 'East window, Greifswald Cathedral (reflection)', 'installation', '2024', 'Coloured light reflected in the west window', None, 'Greifswald Cathedral, Germany'),
    ],
)

ARTISTS['refik-anadol'] = dict(
    name='Refik Anadol', born=1985, died=None, birthplace='Istanbul, Turkey', basedIn='Los Angeles',
    nationality='Turkish', categories=['code', 'light'],
    mediums=['Data sculpture', 'Projection', 'Machine learning', 'Immersive installation', 'Architecture'],
    tags=['AI art', 'Data painting', 'Machine Hallucinations', 'Archives', 'Projection mapping', 'Latent space'],
    bio=("Refik Anadol (born 1985) is a media artist who works with large datasets and machine learning, turning archives of images, sound "
         "and sensor readings into moving 'data paintings' and 'data sculptures' at architectural scale. He studied in Istanbul and at UCLA's "
         "Design Media Arts programme and runs a studio in Los Angeles. WDCH Dreams (2018) projected the LA Philharmonic's digital archive onto the "
         "outside of the Walt Disney Concert Hall. The Machine Hallucinations series (from 2019) trains models on millions of photographs of "
         "cities, nature or space and then 'dreams' through what the model has learned. Unsupervised (2022–23) did this with MoMA's own collection "
         "in the museum's lobby. Other works use EEG recordings (Melting Memories, 2018) or wind data."),
    studyNotes=[
        "The dataset is the subject. Every work starts from a specific archive or sensor stream; ask what was collected, by whom, and what was left out.",
        "Moving between images. The flowing forms are walks through the model's 'latent space', where one image morphs into another.",
        "Architecture as a screen. Walls, buildings and rooms become displays; the site is part of the composition.",
        "Scale and immersion. The work is designed for bodies standing in front of something huge; compare the experience with watching the same video on a laptop.",
    ],
    links=[('Studio website', 'https://refikanadol.com'),
           ('MoMA: Refik Anadol: Unsupervised', 'https://www.moma.org/calendar/exhibitions/5535'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Refik_Anadol')],
    portrait=None,
    works=[
        ('discovery/refik-anadol/c03.jpg', 'Unsupervised', 'installation', '2022', 'Machine-learning model trained on MoMA\'s collection data, displayed on a large LED screen', 'Shown in the lobby of the Museum of Modern Art, New York.', None),
        ('discovery/refik-anadol/c02.jpg', 'WDCH Dreams', 'installation', '2018', 'Projection onto the facade of the Walt Disney Concert Hall, Los Angeles', 'The LA Philharmonic\'s digital archives, processed by machine learning and mapped onto the building.', None),
        ('discovery/refik-anadol/c04.jpg', 'Machine Hallucinations (NYC)', 'installation', '2019', 'Immersive projection, ARTECHOUSE New York', None, None),
        ('discovery/refik-anadol/c01.jpg', 'Latent Being', 'installation', '2019', 'Data installation, Kraftwerk Berlin', None, None),
        ('discovery/refik-anadol/c07.jpg', 'Archive Dreaming', 'installation', '2017', 'Immersive installation built from the SALT Research archive, Istanbul', None, None),
        ('discovery/refik-anadol/c06.jpg', 'Infinity Room', 'installation', '2015', 'Mirrored room with projection and sound', None, None),
        ('discovery/refik-anadol/c05.png', 'Winds of Yawanawa', 'installation', '2024', 'AI data painting', None, None),
    ],
)
