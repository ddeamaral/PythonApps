import urllib2
import os

response = urllib2.urlopen('http://localhost:5000')
html = response.read()


pokedex = {
           1:'bulbasaur', 2:'ivysaur', 3:'venusaur', 4:'charmander',5:'charmeleon', 6:"charizard",
           7:'squirtle',8:'wartortle',9:'Blastoise',10:'caterpie',11:'metapod',12:'butterfree',13:'weedle',
           14:'kakuna',15:'beedrill',16:'pidgey',17:'pidgeotto',18:'pidgeot',19:'rattata',20:'raticate',
           21:'spearow',22:'fearow',23:'ekans',24:'arbok',25:'pikachu',26:'raichu',27:'sandshrew',28:'sandslash',
           29:'nidoran',30:'nidorina',31:'nidoqueen',32:'nidoran',33:'nidorino',34:'nidoking',35:'clefairy',36:'clefable',
           37:'vulpix',38:'ninetales',39:'jigglypuff',40:'wigglytuff',41:'zubat',42:'golbat',43:'oddish',44:'gloom',45:'vileplume',
           46:'paras',47:'parasect',48:'venonat',49:'venomoth',50:'diglett',51:'dugtrio',52:'meowth',53:'persian',54:'psyduck',55:'golduck',
           56:'mankey',57:'primeape',58:'growlithe',59:'arcanine',60:'poliwag',61:'poliwhirl',62:'poliwrath',
           63:'abra',64:'kadabra',65:'alakazam',66:'machop',67:'machoke',68:'machamp',69:'bellsprout',70:'weepinbell',71:'victreebel',
           72:'tentacool',73:'tentacruel',74:'geodude',75:'graveler',76:'golem',77:'ponyta',78:'rapidash',79:'slowpoke',80:'slowbro',
           81:'magnemite',82:'magneton',83:'farfetchd',84:'doduo',85:'dodrio',86:'seel',87:'dewgong',88:'grimer',89:'muk',90:'shellder',
           91:'cloyster',92:'gastly',93:'haunter',94:'gengar',95:'onix',96:'drowzee',97:'hypno',98:'krabby',99:'kingler',100:'voltorb',
           101:'electrode',102:'exeggcute',103:'exeggutor',104:'cubone',105:'marowak',106:'hitmonlee',107:'hitmonchan',108:'lickitung',
           109:'koffing',110:'weezing',111:'rhyhorn',112:'rhydon',113:'chansey',114:'tangela',115:'kangaskhan',116:'horsea',117:'seadra',
           118:'goldeen',119:'seaking',120:'staryu',121:'starmie',122:'mr. mime',123:'scyther',124:'jynx',125:'electabuzz',126:'magmar',127:'pinsir',
           128:'tauros',129:'magikarp',130:'gyarados',131:'lapras',132:'ditto',133:'eevee',134:'vaporeon',135:'jolteon',136:'flareon',
           137:'porygon',138:'omanyte',139:'omastar',140:'kabuto',141:'kabutops',142:'aerodactyl',143:'snorlax',144:'articuno',145:'zapdos',
           146:'moltres',147:'dratini',148:'dragonair',149:'dragonite',150:'mewtwo',151:'mew'}

pokedex_gen2 = {152:'chikorita',153:'bayleef',154:'meganium',155:'cyndaquil',156:'quilava',157:'typhlosion',158:'totodile',
            159:'croconaw',160:'feraligatr',161:'sentret',162:'furret',163:'hoothoot',164:'noctowl',165:'ledyba',
            166:'ledian',167:'spinarak',168:'ariados',169:'crobat',170:'chinchou',171:'lanturn',172:'pichu',173:'cleffa',174:'igglybuff',
            175:'togepi',176:'togetic',177:'natu',178:'xatu',179:'mareep',180:'flaaffy',181:'ampharos',182:'bellossom',183:'marill',184:'azumarill',
            185:'sudowoodo',186:'politoed',187:'hoppip',188:'skiploom',189:'jumpluff',190:'aipom',191:'sunkern',192:'sunflora',193:'yanma',
            194:'wooper',195:'quagsire',196:'espeon',197:'umbreon',198:'murkrow',199:'slowking',200:'misdreavus',201:'unown',202:'wobbuffet',
            203:'girafarig',204:'pineco',205:'forretress',206:'dunsparce',207:'gligar',208:'steelix',209:'snubbull',210:'granbull',211:'qwilfish',
            212:'scizor',213:'shuckle',214:'heracross',215:'sneasel',216:'teddiursa',217:'ursaring',218:'slugma',219:'magcargo',
            220:'swinub',221:'piloswine',222:'corsola',223:'remoraid',224:'octillery',225:'delibird',226:'mantine',227:'skarmory',
            228:'houndour',229:'houndoom',230:'kingdra',231:'phanpy',232:'donphan',233:'porygon2',234:'stantler',
            235:'smeargle',236:'tyrogue',237:'hitmontop',238:'smoochum',239:'elekid',240:'magby',241:'miltank',242:'blissey',
            243:'raikou',244:'entei',245:'suicune',246:'larvitar',247:'pupitar',248:'tyranitar',249:'lugia',250:'ho-oh',251:'celebi'}

pokedex_gen3 = { 252:'treecko',253:'grovyle',254:'sceptile',255:'torchic',256:'combusken',257:'blaziken',258:'mudkip',259:'marshtomp',
                260:'swampert',261:'poochyena',262:'mightyena',263:'zigzagoon',264:'linoone',265:'wurmple',266:'silcoon',267:'beautifly',
                268:'cascoon',269:'dustox',270:'lotad',271:'lombre',272:'ludicolo',273:'seedot',274:'nuzleaf',275:'shiftry',276:'taillow',
                277:'swellow',278:'wingull',279:'pelipper',280:'ralts',281:'kirlia',282:'gardevoir',283:'surskit',284:'masquerain',285:'shroomish',
                286:'breloom',287:'slakoth',288:'vigoroth',289:'slaking',290:'nincada',291:'ninjask',292:'shedinja',293:'whismur',294:'loudred',
                295:'exploud',296:'makuhita',297:'hariyama',298:'azurill',299:'nosepass',300:'skitty',301:'delcatty',302:'sableye',303:'mawile',
                304:'aron',305:'lairon',306:'aggron',307:'meditite',308:'medicham',309:'electrike',310:'manectric',311:'plusle',312:'minun',313:'volbeat',
                314:'illumise',315:'roselia',316:'gulpin',317:'swalot',318:'carvanha',319:'sharpedo',320:'wailmer',321:'wailord',322:'numel',323:'camerupt',
                324:'torkoal',325:'spoink',326:'grumpig',327:'spinda',328:'trapinch',329:'vibrava',330:'flygon',331:'cacnea',332:'cacturne',333:'swablu',
                334:'altaria',335:'zangoose',336:'seviper',337:'lunatone',338:'solrock',339:'barboach',340:'whiscash',341:'corphish',342:'crawdaunt',343:'baltoy',
                344:'claydol',345:'lileep',346:'cradily',347:'anorith',348:'armaldo',349:'feebas',350:'milotic',351:'castform',352:'kecleon',353:'shuppet',354:'banette',
                355:'duskull',356:'dusclops',357:'tropius',358:'chimecho',359:'absol',360:'wynaut',361:'snorunt',362:'glalie',363:'spheal',364:'sealeo',365:'walrein',366:'clamperl',
                367:'huntail',368:'gorebyss',369:'relicanth',370:'luvdisc',371:'bagon',372:'shelgon',373:'salamence',374:'beldum',375:'metang',376:'metagross',
                377:'regirock',378:'regice',379:'registeel',380:'latias',381:'latios',382:'kyogre',383:'groudon',384:'rayquaza',385:'jirachi',
                386:'deoxys'}

complete = False

while(not complete):
    os.system('cls')

    pokemonFound = []
    for pokeNum, pokemon in pokedex.iteritems():

        numOfPokemon = 0

        if html.find(pokemon.capitalize()) > 0:
            numOfPokemon = html.count(pokemon.capitalize())
            pokemonFound.append(pokemon.capitalize() + ': '+ str(numOfPokemon) +  ' found')



    pokemonFound.sort()
    for string in pokemonFound:
        print(string)


    command = raw_input('Are you done? Y or N?')
    if command.lower() == "y":
        complete = True
