proverb_frames = ["My grandmother used to say...",
                  "My grandfather used to say...",
                  "There is an old Persian saying that goes like this...",
                  "There is an old Chinese saying that goes like this...",
                  "A wise old elf once said..."]


#lists cannot have space
freq_countable_noms = ["idiot", "toaster", "legend", "death wish", "marketing idea", "psychic", "knife", "sandwich", "lettuce",
"kitten", "friendly grandma", "french chef", "corn cake", "candlestick maker", "coffee pot", "tank", "skinny woman", "private investor",
"elastic band", "telephone", "pistol", "legal warrant", "famous landscape painting", "Irish song", "volcanic crater", "travel guidebook",
"electric furnace", "oven", "sneaky criminal", "laptop", "dragon", "pervert", "toilet seat", "haunted graveyard", "really tough guy",
"wrinkle", "multi-billionaire", "mental disorder", "hyena", "bat-shit crazy Amish folk", "beautiful elastic band", "lover", "Christmas party",
"baby-shower", "machete",  "drug addict", "cold-hearted Eskimo", "bug", "virus", "bad mood", "confrontational freak", "light bulb",
"broken promises"]



freq_mass_noms =  ["therapy", "antidepressant drug", "mad cow disease", "karate","liquid oxygen", "messiness", "trust fund","dog poop",
"meditation", "boiling water", "misfortune", "failure", "natural history", "divergent thinking", "guilt", "morality"]


# no determiner needed
freq_plural-count_noms = ["hairy legs","laser beams", "scented candles"]



# to be preceded by "the"
freq_unique_noms = ["love of her life"]



#no multi-word expressions
mass_noms = ["water", "oil", "peanut butter", "air", "homework", "money", "petrol", "money", "hair", "jewelry", "toothpaste",
"wood", "soap", "honey", "cheese", "tea", "coffee", "happiness", "patience", "pride", "travel", "self-esteem", "bad advice",
"advice", "rice", "furniture", "glass", "radiation", "meat", "research", "clothing", "bacon", "chess", "clay", "coal", "confusion",
"consciousness", "cream", "dust", "darkness", "education", "empathy", "enthusiasm", "feedback", "fitness", "flattery", "foliage",
"fun", "garbage", "gold", "gossip", "grammar", "gratitude", "gravel", "guilt", "happiness", "hardware", "hate", "hay", "help",
"heat", "health", "hesitation", "homework", "honesty", "honor", "hospitality", "hostility", "humanity", "humility", "ice",
"immortality", "independence", "information", "integrity", "justice", "knowledge", "literacy", "logic", "luck", "lumber",
"luggage", "mail", "management", "merchandise", "morale", "mud", "music", "nonsense", "oppression", "optimism", "oxygen",
"participation", "peace", "perseverance", "pneumonia", "poetry", "police", "pride", "privacy", "propaganda", "recovery",
"rust", "satisfaction", "shame", "stamina", "starvation", "steam", "support", "sweat", "thunder", "timber", "toil", "traffic",
"trash", "understanding", "valor", "violence", "warmth", "waste", "weather", "wheat", "wisdom", "work", "powder", "grain",
"childhood", "stress", "gas", "carbon dioxide", "sunshine", "snow", "equipment", "fame", "fire", "flour", "juice", "laughter",
"leisure", "literature", "motherhood", "racism", "rain", "relaxation", "seafood", "smoke", "silence", "safety", "danger",
"yoga", "youth", "tea", "pollution", "power", "pee", "obesity", "nutrition", "milk", "wine", "help", "English", "Chinese",
"Spanish", "Italian", "cement", "bread", "cotton", "adolescence", "sexism", "insurance", "electricity", "cowardice", "evidence",
"greed", "chaos", "clarity", "sadness", "soccer", "tennis", "judo", "karate", "chess", "silver", "diabetes", "measles", "polio",
"malaria", "influenza", "physics", "biology", "chemistry", "geography", "mathmatics", "transportation", "paper", "wood", "steam",
"smog", "nitrogen", "chalk", "grass", "sand", "poker", "hockey", "fun", "wealth", "Arabic", "enjoyment", "dirt", "dust", "scenery",
"makeup", "meat", "truth", "corn", "sugar", "adulthood", "aggression", "anger", "alcohol", "assistance", "ballet", "beauty",
"beef", "blood", "bread", "cardboard", "cash", "compassion", "corruption", "economics", "envy", "ethics", "evolution", "fame",
"freedom", "garlic", "genetics", "golf", "harm", "hatred", "height", "humor", "hydrogen", "importance", "inflation", "iron",
"irony", "jam", "joy", "kindness", "labour", "lava", "leather", "linguistics", "livestock", "loneliness", "love", "luck",
"machinery", "magic", "mayonnaise", "metal", "methane", "money", "mud", "music", "nature", "news", "nonsense", "nurture",
"obedience", "passion", "pasta", "poetry", "poverty", "power", "progress", "publicity", "punctuation", "quartz", "quality",
"quantity", "rain", "recreation", "relaxation", "respect", "reliability", "revenge", "rubbish", "rum", "salt", "sand",
"seafood", "seaside", "shame", "silence", "sleep", "snow", "soil", "soap", "sorrow", "sport", "strength", "stuff",
"stupidity", "sugar", "sunshine", "symmetry", "thirst", "time", "trust", "underwear", "unity", "veal", "pork",
"beef", "vitality", "welfare", "wool", "work", "zinc", "zoology", "yeast", "wisdom", "width", "butter", "lightning",
"land", "fame", "envy", "dignity", "peace", "spaghetti", "travel", "silk", "perfume", "cream", "advice", "barley"]




freq_prenom_adj = ["sadistic", "metal", "wild", "domesticated", "abnormal", "medicated", "cocky", "massive", "disrespectful", "impressive",
"out of control", "internet worthy", "hilarious", "sexy", "hot", "very tactful", "bearded", "violent", "slimy", "insanely creepy",
"self-centered", "naked", "angry", "shaky", "deep", "sticky", "fluffy", "frozen", "unholy", "painfully honest", "filthy", "harsh", "frisky",
"greedy", "insane", "hideous", "ungodly", "abusive", "drunken", "hateful", "idiotic", "twisted", "useless", "magical", "indecent", "arrogant",
"confused", "high-end", "insecure", "slippery", "stubborn", "vengeful", "sinister", "cowardly", "startled", "alcoholic", "offensive",
"adulterous", "hyperactive", "territorial", "mischievous", "cruel-hearted", "narrow-minded", "self-absorbed", "bat-shit-crazy",
"fiercely-loyal", "out-of-control", "bat shit crazy", "mentally impaired", "absent-minded", "adventurous", "affectionate", "agile",
"agreeable", "ambitious", "amiable", "analytical", "angelic", "apathetic", "apprehensive", "ardent", "artificial", "artistic", "assertive",
"attentive", "average", "awesome", "awful", "balanced", "beautiful", "blue", "boisterous", "brave", "bright", "brilliant", "callous",
"candid", "cantankerous", "capable", "careful", "careless", "caustic", "cautious", "charming", "childish", "cheerful", "chic", "civil",
"clean", "clever", "clumsy", "coherent", "cold", "competent", "composed", "conceited", "condescending", "confident", "confused",
"conscientious", "considerate", "content", "cool", "cool-headed", "co-operative", "cordial", "courageous", "cowardly", "crabby", "crafty",
"cranky", "crass", "critical", "cruel", "curious", "cynical", "dainty", "decisive", "deep", "deft", "delicate", "demonic", "dependent",
"delightful", "demure", "depressed", "devoted", "dextrous", "diligent", "direct", "dirty", "disagreeable", "discreet", "disruptive",
"distant", "distraught", "distrustful", "dowdy", "dramatic", "dreary", "drowsy", "drugged", "drunk", "dull", "dutiful", "eager",
"earnest", "easy-going", "efficient", "egotistical", "elfin", "emotional", "energetic", "enterprising", "enthusiastic", "evasive",
"even-tempered", "exacting", "excellent", "excitable", "experienced", "fabulous", "fastidious", "ferocious", "fervent", "fiery",
"flabby", "flaky", "flashy", "frank", "friendly", "funny", "fussy", "generous", "gentle", "gloomy", "glutinous", "good", "grave",
"great", "groggy", "grouchy", "guarded", "hateful", "hearty", "helpful", "hesitant", "hot-headed", "hyper-critical", "hysterical",
"idiotic", "idle", "illogical", "imaginative", "immature", "immodest", "impatient", "imperturbable", "impetuous", "impractical",
"impressionable", "impressive", "impulsive", "inactive", "incisive", "incompetent", "inconsiderate", "inconsistent", "independent",
"indiscreet", "indolent", "indefatigable", "industrious", "inexperienced", "insensitive", "inspiring", "intelligent", "interesting",
"intolerant", "inventive", "irritable", "jocular", "jovial", "joyous", "judgmental", "keen", "kind", "lame", "lazy", "lean",
"lethargic", "level-headed", "listless", "lively", "local", "logical", "long-winded", "lovable", "love-lorn", "lovely", "maternal",
"mature", "mean", "meddlesome", "methodical", "meticulous", "mild", "miserable", "modest", "moronic", "morose", "motivated",
"musical", "naive", "nasty", "natural", "naughty", "negative", "nervous", "noisy", "normal", "nosy", "numb", "obnoxious",
"old-fashioned", "one-sided", "orderly", "ostentatious", "outgoing", "outspoken", "passionate", "passive", "paternal",
"paternalistic", "patient", "peaceful", "peevish", "pensive", "petulant", "picky", "plain", "playful", "pleasant", "plucky",
"polite", "popular", "positive", "powerful", "practical", "prejudiced", "pretty", "proficient", "proud", "provocative",
"prudent", "punctual", "quarrelsome", "querulous", "quick", "quick-tempered", "quiet", "realistic", "reclusive", "reliable",
"reluctant", "resentful", "reserved", "resigned", "resourceful", "respected", "respectful", "responsible", "restless", "revered",
"ridiculous", "sad", "sassy", "saucy", "self-assured", "selfish", "sensible", "sensitive", "sentimental", "serene", "serious",
"sharp", "short-tempered", "shrewd", "shy", "silly", "sincere", "sleepy", "slight", "sloppy", "slothful", "slovenly", "slow",
"smart", "snazzy", "snobby", "somber", "sober", "sophisticated", "soulful", "soulless", "sour", "spirited", "spiteful",
"stable", "staid", "steady", "stern", "stoic", "strong", "stupid", "sturdy", "subtle", "sullen", "sulky", "supercilious",
"superficial", "suspicious", "sweet", "tactful", "tactless", "talented", "testy", "thoughtful", "thoughtless", "timid", "tired",
"ghoulishly delightful", "organically produced", "critically acclaimed", "obsessive-compulsive", "perfectly balanced",
"mentally impaired", "ready-for-action", "thirst-quenching", "state-of-the-art", "easy-to-maintain", "verbally abusive",
"well-intentioned", "self-disciplined", "top-of-the-line", "family-friendly", "social-oriented", "quick-to-set-up",
"confrontational", "ready-to-please", "eager-to-please", "unsophisticated", "family-oriented", "water-resistant",
"two-dimensional", "straight-forward", "custom-designed", "people-friendly", "fair-and-square", "world-renowned",
"freshly brewed", "quintessential", "blood-curdling", "odor-resistant", "short-tempered", "fiercely-loyal", "well-respected",
"fear-inspiring", "hallucinogenic", "spoiled rotten", "impressionable", "well-developed", "quick-tempered", "half-obedient",
"non-alcoholic", "easy-to-train", "irresponsible", "absent-minded", "unpredictable", "well-balanced", "inspirational", "disturbing",
"eerie", "frightening", "hideous", "dead", "haunted", "rude", "low", "creepy", "deceased", "defiant", "foul", "sinful",
"bereftoflife", "horrid", "divine", "black", "cold", "up-to-no-good", "holy", "phantasmal", "direful", "ungodly", "slimy",
"ignominious", "indecent", "degrading", "strange", "pitiful", "gross", "spooky", "gruesome", "grievous", "distasteful",
"horrible", "pagan", "unearthly", "terrifying", "weird", "reprehensible", "dark", "frightful", "alarming", "nauseating",
"abusive", "nasty", "disreputable", "supernatural", "scary", "corpse-like", "obnoxious", "abhorrent", "monstrous",
"fearful", "deadly", "shocking", "superstitious", "annoying", "intense", "contemptible", "beastly", "pale", "minacious",
"irritating", "distressing", "irreverent", "dirty", "uncanny", "ghost-like", "terrible", "dire", "bad", "disguised",
"godless", "no-good", "phantom", "repulsive", "illusory", "rotten", "biting", "masked", "bloody", "appalling", "dreadful",
"sordid", "formidable", "off-color", "odious", "detestable", "mean", "insolent", "frozen", "vampiric", "spooked", "infamous",
"moon-lit"]



#pay attention to capitalization
characters = ["Ant-Man", "Captain America", "Black Widow", "Batman", "Thor", "Wonder Woman", "Wolverine", "Ironman",
"Supergirl", "Hulk", "Aquaman", "Jesus Christ", "God", "Moses", "Black Panther", "Adolf Hitler", "Donald Trump", "Hawkeye",
"Marilyn Manroe", "Muhammad Ali", "Charles Darwin", "Vincent van Gogh", "Dalai Lama", "The pope", "Buddha", "Confucius",
"Genghis Khan", "Joan of Arc", "Oscar Wilde", "Gandhi", "Albert Einstein", "Chairman Mao", "Mother Teresa", "Cleopatra",
"Marie Curie", "Anne Frank", "Audrey Hepburn", "Madonna", "Diana", "J.K. Rowling", "James Bond", "Joker", "Bruce Lee",
"The Terminator", "The Little Mermaid", "Queen Elsa", "Snow White", "Cinderella", "Mulan"]


occupations = ["asparagus harvester", "astronaut", "auctioneer", "baker", "bar-keeper", "beautician", "bee-keeper", "bicycle messenger",
"biologist", "bookseller", "bouncer", "boxer", "brick-layer", "butcher", "call-centre agent", "cameraman", "captain", "carpenter",
"cemetery gardener", "chancellor", "chef", "chemist", "chimney sweep", "coder", "computer scientist", "concrete worker", "conductor",
"creative director", "dentist", "diet counsellor", "director", "disc jockey", "doorkeeper", "dressmaker", "driving instructor", "educator",
"electrician", "energy consultant", "estate agent", "event manager", "firefighter", "florist", "gardener", "geriatric nurse", "goldsmith",
"headhunter", "high school teacher", "housewife", "househusband", "human resources manager", "hunter", "ice-cream vendor",
"interior designer", "interpreter", "jazz musician", "journalist", "judge", "lawyer", "legal expert", "librarian", "lifeguard",
"market researcher", "marriage counsellor", "masseur", "meteorologist", "minister of defense", "model", "mountaineer", "music teacher",
"nurse", "obstetrician", "optician", "painter", "pathologist", "pharmacist", "photographer", "physician", "physicist", "piano maker",
"pilot", "plumber", "priest", "puppeteer", "roofer", "salesperson", "santa", "shepherd", "ship-builder", "soccer referee",
"speech-writer", "tennis instructor", "stonemason", "stuntman", "swimming pool attendant", "taxi driver", "tour guide", "train driver",
"veterinarian", "violin-maker", "watchmaker", "cowboy", "nun", "primary school principal"]
