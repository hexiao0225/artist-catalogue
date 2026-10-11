# Artist entries, part B. Sources from discovery3 (scraped pages) carry explicit credits:
# (source, title, kind, year, medium, note, collection, credit, sourceUrl)
from artists_a import ARTISTS

GLAD = 'https://www.gladstonegallery.com/artist/anicka-yi/'
YI = '© Anicka Yi. Courtesy Gladstone Gallery'
ARTISTS['anicka-yi'] = dict(
    name='Anicka Yi', born=1971, died=None, birthplace='Seoul, South Korea', basedIn='New York',
    nationality='Korean-American', categories=['bio-science', 'concept'],
    mediums=['Sculpture', 'Installation', 'Scent', 'Video', 'Biomaterials', 'Machines'],
    tags=['Bacteria', 'Smell', 'Machine ecologies', 'Kelp', 'Tempura-fried flowers', 'Art and science', 'Aerobes'],
    bio=("Anicka Yi (born 1971) was born in Seoul, grew up in California and lives in New York. She came to art without formal training, and "
         "since the 2010s has built a practice around the senses that art usually ignores, especially smell, and around materials that are "
         "alive, perishable or unstable: bacteria, kelp, tempura-fried flowers, soap, ants, sweat and scent. She works with scientists and "
         "engineers; for You Can Call Me F (The Kitchen, 2015) she grew bacteria sampled from a hundred women. Her Hugo Boss Prize "
         "exhibition Life Is Cheap (Guggenheim, 2017) included a wall of bacteria and the scent of Asian American women and ants. For In Love "
         "With the World (2021), the Hyundai Commission at Tate Modern, she filled the Turbine Hall with floating machines, 'aerobes', that "
         "drifted like jellyfish and seeds through changing scents. Recent sculptures are lantern-like forms of dried kelp lit from within, some "
         "housing animatronic insects, and fibre-optic works that move like living things."),
    studyNotes=[
        "Work with what is alive or decaying. Bacteria grow, kelp dries, fried flowers darken; the piece keeps changing after it is installed.",
        "Smell is a medium. She commissions scents as carefully as forms; ask what a room would smell like and why.",
        "Machines as organisms. The aerobes and the motorised fibre-optic sculptures behave like creatures; she imagines how machines might live alongside us.",
        "Collaborate with the lab. Much of the work depends on scientists, perfumers and engineers; the collaboration itself is part of the method.",
    ],
    links=[('Tate Modern: Hyundai Commission, Anicka Yi (2021)', 'https://www.tate.org.uk/whats-on/tate-modern/hyundai-commission-anicka-yi'),
           ('Gladstone Gallery', GLAD),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Anicka_Yi')],
    portrait=('discovery3/anicka-yi/p22.jpg', 'Photo: Sun Shi, courtesy UCCA Center for Contemporary Art'),
    works=[
        ('discovery3/anicka-yi/p05.jpg', 'In Love With the World', 'installation', '2021', 'Floating machines (aerobes) and scent, Hyundai Commission, Turbine Hall, Tate Modern', 'Jellyfish- and seed-like flying machines moved through the hall on their own, while the air was scented differently over the months.', None, '© Anicka Yi. Photo: Tate', 'https://www.tate.org.uk/whats-on/tate-modern/hyundai-commission-anicka-yi'),
        ('discovery3/anicka-yi/p11.jpg', 'Half Water, Half Mud, Half Sun II', 'sculpture', '2023', 'Kelp, aquazol, glycerin, crepeline, acrylic, LED and animatronic insect', None, None, YI, GLAD),
        ('discovery3/anicka-yi/p10.jpg', 'Half Water, Half Mud, Half Sun IV', 'sculpture', '2023', 'Kelp, aquazol, glycerin, crepeline, acrylic, LED and animatronic insect', None, None, YI, GLAD),
        ('discovery3/anicka-yi/p07.jpg', 'The Department of Autumn Grief', 'sculpture', '2026', 'Kelp, aquazol, glycerin, dye, crepeline, acrylic, LED, animatronic insect', None, None, YI, GLAD),
        ('discovery3/anicka-yi/p12.jpg', 'Night Writing', 'sculpture', '2025', 'PMMA optical fibre, LEDs, silicone, acrylic, epoxy, aluminium, steel, brass, motors and microcontrollers', 'A lit, motorised fibre-optic form that moves slowly, like a breathing creature.', None, YI + '. Photo: Andrea Rossetti', GLAD),
        ('discovery3/anicka-yi/p14.jpg', 'Amputation', 'sculpture', '2024', 'Foam, plaster, paint, tempura-fried flowers, glass, tubing', None, None, YI + '. Photo: Andrea Rossetti', GLAD),
        ('discovery3/anicka-yi/p20.jpg', 'Late Classical XIX', 'sculpture', '2022', 'Tempura-fried flowers, resin, plexiglas, stainless steel shelves, chrome-plated dumbbells', None, None, YI, GLAD),
        ('discovery3/anicka-yi/p17.jpg', 'Reverse Osmosis', 'painting', '2022', 'UV print on silk screen mesh in cherry frame', None, None, YI, GLAD),
        ('discovery3/anicka-yi/p13.jpg', 'Each Branch Of Coral Holds Up The Light Of The Moon (video still)', 'film', '2024', 'Animated colour video with sound, 16 min 8 s', None, None, YI, GLAD),
    ],
)

ANKER = '© Suzanne Anker'
ARTISTS['suzanne-anker'] = dict(
    name='Suzanne Anker', born=1946, died=None, birthplace='Brooklyn, New York', basedIn='New York',
    nationality='American', categories=['bio-science'],
    mediums=['Sculpture', 'Installation', 'Photography', 'Digital fabrication', 'Living plants'],
    tags=['Bio art', 'Petri dish', 'Genetics', 'Chromosomes', 'Plants and LEDs', 'Art and science'],
    bio=("Suzanne Anker (born 1946) is a visual artist and theorist who has worked at the meeting point of art and biology since the 1980s. "
         "She co-wrote The Molecular Gaze: Art in the Genetic Age (2004) with the sociologist Dorothy Nelkin, chaired the Fine Arts department "
         "at the School of Visual Arts in New York for many years, and founded its Bio Art Lab, one of the first labs of its kind in an art "
         "school. Her work draws on the images and tools of genetics, neuroscience and botany: chromosome forms cast as sculpture, Rorschach-like "
         "inkblots, petri dishes filled with organic and inorganic matter and photographed like small worlds (Vanitas in a Petri Dish), "
         "3D-printed sculptures made from those photographs (Remote Sensing), and plants grown under coloured LEDs in sealed growth chambers "
         "(Astroculture)."),
    studyNotes=[
        "Borrow the lab's tools and images. Petri dishes, chromosome charts and growth chambers become the frames and materials of the work.",
        "Translate between media. A photograph of a petri dish becomes a 3D scan and then a printed sculpture; each step changes what we see.",
        "Hold beauty and critique together. The works are seductive objects that also ask questions about how biology is represented and controlled.",
        "Teach and build structures. Founding a bio art lab inside an art school is part of her practice; consider what infrastructure your work needs.",
    ],
    links=[('Artist website', 'https://www.suzanneanker.com'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Suzanne_Anker')],
    portrait=None,
    works=[
        ('discovery3/suzanne-anker/p01.webp', 'Vanitas in a Petri Dish (installation view)', 'installation', '2010s', 'Petri dishes with organic and inorganic material, photographs and light', 'Rows of petri dishes become small still lifes, an update of the vanitas painting tradition.', None, ANKER, 'https://www.suzanneanker.com'),
        ('discovery/suzanne-anker/c03.jpg', 'Remote Sensing', 'sculpture', '2011', '3D-printed sculptures made from photographs of petri dishes', None, None),
        ('discovery/suzanne-anker/c01.jpg', 'Biota', 'sculpture', '2011', 'Mixed media', None, None),
        ('discovery/suzanne-anker/c02.jpg', 'Astroculture (Eternal Return)', 'installation', '2015', 'Plants grown under LED lights in growth chambers', 'Shown in a cathedral setting, the magenta growing light fills the nave.', None),
        ('discovery3/suzanne-anker/p04.webp', 'When Crystals Spawn Flowers', 'installation', '2024', 'Mixed media', 'Shown in the touring exhibition Bloom, about flowers and their relationship to humans.', None, ANKER, 'https://www.suzanneanker.com'),
        ('discovery3/suzanne-anker/p08.webp', 'Origins and Futures IV', 'sculpture', '2005', 'Sculpture on a glass base', 'Refers to A. G. Cairns-Smith\'s theory that life may have begun on clay crystals.', 'MACAM, Lisbon', ANKER, 'https://www.suzanneanker.com'),
    ],
)

KAC = '© Eduardo Kac'
ARTISTS['eduardo-kac'] = dict(
    name='Eduardo Kac', born=1962, died=None, birthplace='Rio de Janeiro, Brazil', basedIn='Chicago',
    nationality='Brazilian-American', categories=['bio-science'],
    mediums=['Transgenic art', 'Installation', 'Telepresence', 'Holopoetry', 'Space art', 'Mosaic'],
    tags=['Bio art', 'Transgenic art', 'GFP Bunny', 'Alba', 'Genetic code', 'Telepresence art', 'Poetry'],
    bio=("Eduardo Kac (born 1962) began as a poet and performance artist in Rio de Janeiro in the early 1980s, making holographic poems and "
         "early telecommunications and telepresence works before turning to living systems. He coined the term 'transgenic art' in 1998. "
         "In Genesis (1999) he translated a sentence from the Book of Genesis into Morse code and then into a synthetic gene, inserted it "
         "into bacteria, and let gallery visitors trigger mutations by switching on ultraviolet light over the internet. GFP Bunny (2000) "
         "centred on Alba, a rabbit bred with a fluorescent protein from a jellyfish, and on the public debate and the campaign to bring her "
         "home. Later works include Natural History of the Enigma (2003–08), a flower carrying his own DNA, and Inner Telescope (2017), "
         "made in orbit with the astronaut Thomas Pesquet. He teaches at the School of the Art Institute of Chicago."),
    studyNotes=[
        "The artwork extends beyond the object. GFP Bunny is a rabbit, a set of images, a debate in the press and a campaign; the discussion is part of the piece.",
        "Code as a bridge. Genesis moves a sentence through Morse code and genetic code, asking what happens to meaning when language becomes biology.",
        "Audience participation over a network. Visitors and remote users could change the bacteria in Genesis, which makes them responsible for the mutations.",
        "Ethics as material. Kac treats the responsibility of creating life, and caring for it afterwards, as a central question of the work.",
    ],
    links=[('Artist website', 'https://www.ekac.org'),
           ('GFP Bunny', 'https://www.ekac.org/gfpbunny.html'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Eduardo_Kac')],
    portrait=None,
    works=[
        ('discovery/eduardo-kac/c01.jpg', 'Genesis', 'installation', '1999', 'Transgenic installation: synthetic gene, bacteria, UV light, video, internet', 'Shown at Ars Electronica, Linz. Online visitors could switch on UV light over the bacteria, causing mutations in the "Genesis gene".', None),
        ('discovery3/eduardo-kac/p01.png', 'GFP Bunny (Alba)', 'performance', '2000', 'Transgenic artwork: a rabbit expressing green fluorescent protein, with the public dialogue around her', None, None, KAC, 'https://www.ekac.org/gfpbunny.html'),
        ('discovery/eduardo-kac/c05.jpg', 'Lagoogleglyph V', 'installation', '2022', 'Mosaic of coloured tiles, 6 × 15 m', 'A huge pixelated rabbit, meant to be seen from the sky and by satellite imaging.', None),
        ('discovery/eduardo-kac/c04.jpg', 'Lagoogleglyph V (detail)', 'installation', '2022', 'Mosaic of coloured tiles', None, None),
    ],
)

TAW = 'Courtesy Lenore G. Tawney Foundation'
TAWF = 'https://lenoretawney.org/work/fiber/'
TAWC = 'https://lenoretawney.org/work/collage/'
ARTISTS['lenore-tawney'] = dict(
    name='Lenore Tawney', born=1907, died=2007, birthplace='Lorain, Ohio', basedIn='New York',
    nationality='American', categories=['fibre'],
    mediums=['Weaving', 'Fibre sculpture', 'Collage', 'Assemblage', 'Drawing'],
    tags=['Woven forms', 'Open-warp weaving', 'Cloud series', 'Linen', 'Coenties Slip', 'Spirituality'],
    bio=("Lenore Tawney (1907–2007) helped turn weaving into sculpture. She studied sculpture with Alexander Archipenko and tapestry with "
         "the Finnish weaver Martta Taipale, and in 1957 moved from Chicago to a loft at Coenties Slip in lower Manhattan, where her neighbours "
         "included Agnes Martin, Ellsworth Kelly and Robert Indiana. There she developed open-warp weaving, leaving areas of bare warp so light "
         "and air pass through the cloth, and built tall, narrow, freestanding 'woven forms' in linen that hang like columns or figures. "
         "Dark River (1962) is over four metres tall. From the late 1970s she made 'Clouds', installations of thousands of linen threads hanging "
         "from a ceiling grid, and in parallel produced collages, assemblages, drawings on graph paper and artist's books full of feathers, "
         "eggs, bones and text."),
    studyNotes=[
        "Weave space, not just cloth. Open warps let light and the wall show through; what is left unwoven matters as much as the woven parts.",
        "Vertical scale. The woven forms are much taller than a person and hang free of the wall, so they read as sculpture.",
        "Thread as line and volume. In the Cloud works, thousands of single threads make a volume you can walk under; each thread is a drawn line.",
        "Small and large practices feed each other. The intimate collages and books sit alongside monumental weavings; compare their materials and rhythms.",
    ],
    links=[('Lenore G. Tawney Foundation', 'https://lenoretawney.org'),
           ('MoMA: Dark River on view', 'https://lenoretawney.org/lenore-tawneys-dark-river-on-view-for-the-first-time-at-moma/'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Lenore_Tawney')],
    portrait=('discovery3/lenore-tawney/p13.webp', 'Lenore Tawney weaving. Courtesy Lenore G. Tawney Foundation'),
    works=[
        ('discovery3/lenore-tawney/p05.webp', 'Cloud Labyrinth', 'installation', '1983', 'Linen threads hung from a canvas ceiling grid', 'Thousands of threads form a hanging volume you can walk beneath.', None, TAW, TAWF),
        ('discovery3/lenore-tawney/p27.jpg', 'Dark River', 'sculpture', '1962', 'Linen and wood', 'An open-warp woven form more than four metres tall.', 'The Museum of Modern Art, New York. Greta Daniel Design Fund', '© Lenore G. Tawney Foundation. Photo: The Museum of Modern Art', 'https://lenoretawney.org/lenore-tawneys-dark-river-on-view-for-the-first-time-at-moma/'),
        ('discovery3/lenore-tawney/p06.webp', 'Inquisition', 'sculpture', '1961', 'Woven fibre', None, None, TAW, TAWF),
        ('discovery3/lenore-tawney/p07.webp', 'Shrouded River', 'sculpture', '1966', 'Woven fibre', None, None, TAW, TAWF),
        ('discovery3/lenore-tawney/p01.webp', 'Shield IV', 'sculpture', '1966', 'Woven fibre', None, None, TAW, TAWF),
        ('discovery3/lenore-tawney/p08.webp', 'Written in Water', 'sculpture', '1979', 'Fibre', None, None, TAW, TAWF),
        ('discovery3/lenore-tawney/p10.webp', 'Waterfall', 'sculpture', '1974', 'Fibre', None, None, TAW, TAWF),
        ('discovery3/lenore-tawney/p18.webp', 'Labyrinth', 'drawing', '1967', 'Collage and ink on paper', None, None, TAW, TAWC),
        ('discovery3/lenore-tawney/p19.webp', 'Time Roars like a Seashell', 'drawing', '1967', 'Collage', None, None, TAW, TAWC),
        ('discovery3/lenore-tawney/p25.webp', 'Artist book with rodent skull', 'sculpture', 'c. 1985', 'Artist\'s book, collage and found objects', None, None, TAW, TAWC),
    ],
)

KREPS = 'https://www.andrewkreps.com/artists/hito-steyerl'
HS = '© Hito Steyerl. Courtesy the artist and Andrew Kreps Gallery, New York'
ARTISTS['hito-steyerl'] = dict(
    name='Hito Steyerl', born=1966, died=None, birthplace='Munich, Germany', basedIn='Berlin',
    nationality='German', categories=['concept'],
    mediums=['Video', 'Installation', 'Essay film', 'Writing', 'Lecture-performance'],
    tags=['Essay film', 'Poor image', 'Digital culture', 'Circulation', 'Surveillance', 'AI', 'Art and power'],
    bio=("Hito Steyerl (born 1966) is a filmmaker, artist and writer who studied cinematography in Tokyo and Munich and holds a PhD in philosophy. "
         "She began with documentary and essay films and has become one of the most influential artists working on how images are made and "
         "circulated in digital culture. Her essays, such as 'In Defense of the Poor Image' (2009), published in e-flux journal and collected in "
         "The Wretched of the Screen (2012), are as widely read as her films. Her video installations build whole environments around the "
         "screen: How Not to Be Seen: A Fucking Didactic Educational .MOV File (2013) is a deadpan tutorial on disappearing from surveillance; "
         "Liquidity Inc. (2014) is shown on a wave-shaped seating structure; Factory of the Sun (2015) filled the German Pavilion in Venice. "
         "Later works use game engines and machine learning to look at art markets, militarisation and AI."),
    studyNotes=[
        "One argument, many forms. The same ideas appear as an essay, a lecture, a video and an installation; each version reaches a different audience.",
        "Design the viewing space. Seating, lighting and grids are part of the work; the installation tells you how to watch.",
        "Mix registers. Documentary footage, tutorials, video games, jokes and theory sit side by side; humour carries a serious critique.",
        "Make the circulation visible. Compression, copying and online distribution are not side effects; they are what the work is about.",
    ],
    links=[('Andrew Kreps Gallery', KREPS),
           ("e-flux journal: 'In Defense of the Poor Image'", 'https://www.e-flux.com/journal/10/61362/in-defense-of-the-poor-image/'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Hito_Steyerl')],
    portrait='discovery/hito-steyerl/c18.jpg',
    works=[
        ('discovery3/hito-steyerl/p07.jpg', 'How Not to Be Seen: A Fucking Didactic Educational .MOV File', 'installation', '2013', 'Single-channel HD video, installation', 'A deadpan tutorial in five lessons on how to become invisible in an age of surveillance.', None, HS, KREPS),
        ('discovery3/hito-steyerl/p02.jpg', 'This is the Future', 'installation', '2019', 'Video installation, 58th Venice Biennale', None, None, HS, KREPS),
        ('discovery3/hito-steyerl/p09.jpg', 'Drill', 'installation', '2019', 'Multi-channel video installation, Park Avenue Armory, New York', None, None, HS, KREPS),
        ('discovery3/hito-steyerl/p03.jpg', 'The City of Broken Windows', 'installation', '2018', 'Video installation, Castello di Rivoli, Turin', None, None, HS, KREPS),
        ('discovery/hito-steyerl/c03.jpg', 'HellYeahWeFuckDie', 'installation', '2016', 'Video installation, shown at Skulptur Projekte Münster 2017', 'The title combines the most common words in English-language pop song titles of the 2010s.', None),
    ],
)

ARTISTS['vera-molnar'] = dict(
    name='Vera Molnar', born=1924, died=2023, birthplace='Budapest, Hungary', basedIn='Paris',
    nationality='Hungarian-French', categories=['code'],
    mediums=['Computer drawing', 'Plotter drawing', 'Painting', 'Sculpture', 'Notebooks'],
    tags=['Algorithmic art', 'Machine imaginaire', 'Rule-based work', 'Generative art', 'Geometric abstraction', 'Disorder'],
    bio=("Vera Molnar (1924–2023) was one of the first artists to make work with a computer. Trained in Budapest, she moved to Paris in 1947 "
         "and was a co-founder of the Groupe de Recherche d'Art Visuel in 1960. Before she had access to a machine she worked with what she "
         "called a 'machine imaginaire': she wrote simple rules and executed them by hand, systematically varying squares, lines and grids. In "
         "1968 she began working on a computer at a university research centre in Paris, writing programs in Fortran and Basic and drawing "
         "the results with a plotter. Series such as Interruptions (1968–69), (Des)Ordres (1974) and Lettres de ma mère (1981–90) explore how "
         "a small dose of randomness, '1% disorder', brings an ordered system to life. She worked until her death in 2023, a few months before "
         "her centenary; the Centre Pompidou opened a major exhibition of her work in 2024."),
    studyNotes=[
        "Rules first, machine second. Her 'machine imaginaire' shows that algorithmic thinking does not need a computer; write the rule, then run it by hand.",
        "One per cent disorder. Introduce a small amount of randomness into a strict system and watch where it breaks; that tension is the work.",
        "Series, not single images. She explored a rule across hundreds of variations; the meaning is in comparing them.",
        "Sixty years of the same questions. From the 1950s to the 2020s she kept working with squares and lines; the depth comes from long, patient iteration.",
    ],
    links=[('Centre Pompidou: Vera Molnar, Parler à l\'œil (2024)', 'https://www.centrepompidou.fr/'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Vera_Moln%C3%A1r')],
    portrait='discovery/vera-molnar/c01.png',
    works=[
        ('discovery/vera-molnar/c04.jpg', 'Interruptions à recouvrements', 'drawing', '1969', 'Computer-generated plotter drawing', 'Short lines rotate at random within a grid; areas left blank interrupt the pattern.', None),
        ('discovery/vera-molnar/c07.jpg', 'Metal relief in the exhibition "Parler à l\'œil", Centre Pompidou', 'sculpture', 'Photo 2024', 'Metal', None, None),
        ('discovery/vera-molnar/c06.jpg', 'Notebooks, shown at the Centre Pompidou', 'drawing', 'Photo 2024', 'Artist\'s notebooks', 'Her working notebooks record rules, variations and calculations.', None),
        ('discovery/vera-molnar/c02.jpg', 'Geometric work in red', 'painting', 'Photo 2013', 'Paint', None, None),
    ],
)

REAS = '© Casey Reas'
ARTISTS['casey-reas'] = dict(
    name='Casey Reas', born=1972, died=None, birthplace='Troy, Ohio', basedIn='Los Angeles',
    nationality='American', categories=['code'],
    mediums=['Software', 'Generative art', 'Prints', 'Video', 'Machine learning'],
    tags=['Processing', 'Generative art', 'Process Compendium', 'GANs', 'Sol LeWitt', 'Open source'],
    bio=("Casey Reas (born 1972) is an artist and educator who writes software to make images, prints and moving-image works. With Ben Fry "
         "he created Processing (2001) at the MIT Media Lab, an open-source programming language for artists and designers that has taught "
         "a generation of artists and designers to code. His Process series (2004–2010), collected in Process Compendium, follows Sol LeWitt's wall drawings: "
         "each Process is a short text instruction about simple 'elements' and their behaviours, realised in software as a dense, evolving "
         "drawing. Since 2018 he has used generative adversarial networks, in Compressed Cinema (2018–2023) and In Silico, and released work on "
         "the blockchain, including the Caesuras identity. He is a professor in Design Media Arts at UCLA and co-founded the platform Feral File."),
    studyNotes=[
        "Write the rule in words first. Each Process is a short English text before it is code, so the idea can exist in more than one medium.",
        "Simple elements, complex results. A circle that moves and reacts to touching neighbours is enough to generate a whole field of drawings.",
        "Tools are part of the art. Building Processing, a tool others use, is as significant as any single artwork.",
        "Show the system's variations. Compare two outputs of the same rule side by side; the differences reveal the system.",
    ],
    links=[('Artist website', 'https://reas.com'),
           ('Processing', 'https://processing.org'),
           ('Wikipedia', 'https://en.wikipedia.org/wiki/Casey_Reas')],
    portrait='discovery/casey-reas/c18.jpg',
    works=[
        ('discovery3/casey-reas/p01.jpg', 'Process (from Process Compendium)', 'drawing', '2004–2010', 'Software, and prints made from it', 'Each Process starts from a written instruction about simple elements and their behaviours.', None, REAS, 'https://reas.com/process'),
        ('discovery3/casey-reas/p05.png', 'In Silico', 'painting', '2025', 'Three large-format prints made from GAN outputs trained on plant imagery', None, None, REAS, 'https://reas.com/in-silico'),
        ('discovery3/casey-reas/p04.jpg', 'Untitled film still 5.1', 'photograph', '2019/2023', 'Image generated by a GAN trained on frames from a feature film', 'From Compressed Cinema, which also compresses whole films into short videos.', None, REAS, 'https://reas.com/compressed-cinema'),
        ('discovery3/casey-reas/p07.jpg', 'AAI (Anarchic Artificial Intelligence), as Caesuras', 'drawing', '2021', 'Generative still image (PNG)', 'Recursive grids that subdivide into dense, unstable patterns.', None, REAS, 'https://reas.com/caesuras'),
        ('discovery3/casey-reas/p06.jpg', 'Still Life, installation view at bitforms gallery', 'installation', '2016–2023', 'Generative software', 'From Atomism, works that break digital images into their smallest units and recompose them.', None, REAS, 'https://reas.com/atomism'),
        ('discovery/casey-reas/c04.png', 'Processing (with Ben Fry)', 'installation', '2001–', 'Open-source programming language and environment', 'The software tool he co-created, used by artists, designers and students worldwide.', None),
    ],
)

ZL = 'Courtesy Zach Lieberman'
ARTISTS['zach-lieberman'] = dict(
    name='Zach Lieberman', born=1977, died=None, birthplace=None, basedIn='New York',
    nationality='American', categories=['code'],
    mediums=['Software', 'Interactive installation', 'Generative art', 'Teaching'],
    tags=['openFrameworks', 'Creative coding', 'Daily sketches', 'EyeWriter', 'School for Poetic Computation', 'Poetic computation'],
    bio=("Zach Lieberman (born 1977) is an artist, researcher and educator who uses code to make poetic, playful, often interactive work. "
         "He co-created openFrameworks, an open-source C++ toolkit for creative coding, with Theo Watson and Arturo Castro. In 2009 he "
         "worked with the Graffiti Research Lab, Free Art and Technology and others on the EyeWriter, a low-cost eye-tracking system that let "
         "the graffiti artist TEMPT1, paralysed by ALS, draw again with his eyes. In 2013 he co-founded the School for Poetic Computation in "
         "New York, an artist-run school about art, code and hardware. He has posted a new generative sketch almost every day since 2016, and "
         "leads the Future Sketches group at the MIT Media Lab, which looks at the history of computational art and drawing."),
    studyNotes=[
        "Sketch every day. A daily practice of small experiments in code builds a personal visual language and a huge archive of ideas.",
        "Build tools and share them. openFrameworks and the EyeWriter are open-source; making tools others can use is part of the art.",
        "Code with care. The EyeWriter shows technology made with and for a specific person, with a clear human purpose.",
        "Teaching as practice. The School for Poetic Computation treats education itself as a creative work.",
    ],
    links=[('Artist website', 'https://zach.li'),
           ('EyeWriter', 'https://eyewriter.org'),
           ('School for Poetic Computation', 'https://sfpc.study'),
           ('openFrameworks', 'https://openframeworks.cc')],
    portrait='discovery/zach-lieberman/c01.jpg',
    works=[
        ('discovery3/zach-lieberman/p13.png', 'Sketch', 'drawing', 'c. 2019', 'Real-time generative software', 'One of his daily code sketches of colour, form and movement.', None, ZL + ' / MIT Media Lab', 'https://www.media.mit.edu/groups/future-sketches/overview/'),
        ('discovery3/zach-lieberman/p02.jpg', 'EyeWriter (with TEMPT1, Free Art and Technology, openFrameworks, Graffiti Research Lab)', 'installation', '2009', 'Low-cost eye-tracking glasses and open-source drawing software', 'Built so that TEMPT1, paralysed by ALS, could draw graffiti with his eyes.', None, 'EyeWriter project (eyewriter.org)', 'https://eyewriter.org'),
        ('discovery3/zach-lieberman/p05.jpg', 'EyeWriter: TEMPT1 tag shown in a gallery', 'installation', '2009', 'Projection of a tag drawn with eye movements', None, None, 'EyeWriter project (eyewriter.org)', 'https://eyewriter.org'),
        ('discovery3/zach-lieberman/p07.jpg', 'EyeWriter: TEMPT1 tag projected onto a building', 'installation', '2009', 'Projected tag drawn with eye movements', None, None, 'EyeWriter project (eyewriter.org)', 'https://eyewriter.org'),
        ('discovery3/zach-lieberman/p10.png', 'EyeWriter: tag drawn by TEMPT1', 'drawing', '2009', 'Digital drawing made with eye-tracking software', None, None, 'EyeWriter project (eyewriter.org)', 'https://eyewriter.org'),
    ],
)
