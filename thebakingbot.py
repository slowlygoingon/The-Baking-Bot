# Copyright 2018 slowlygoingon, Chanku/Sapein
import discord
import asyncio
import random
import requests
import io
import time
import datetime
import aiohttp
from discord.ext import commands


bot = commands.Bot(description="The Baking Bot is the amazing official bot for the community & mental health server The Baking Spot. As of now, it has very basic commands, but we hope to implement more of them in the future!", command_prefix="tbs!")
client = discord.Client()
timenow = datetime.datetime.utcnow()

bot.remove_command('help')

@bot.event
async def on_ready():
    readymessage = ("Hello, I'm ready! It is " + str(timenow))
    uptimedict['timeuptime'] = timenow
    print(readymessage)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with a cake"))



blacklistn = ["nsfw", "porn", "explicit"]
blacklistg = ["gore", "violence", "horror", "screamer", "jumpscare"]

uptimedict = {'timeuptime': 0}

@bot.command(pass_context=True, aliases=["say", "talk"])
async def echo(ctx, *, message):
    error = discord.Embed(title="Error!", description="Don't ping with bot commands, thank you.", colour=discord.Colour.red())
    errorm = discord.Embed(title="Error!", description="Did you seriously just try to mass-ping?", colour=discord.Colour.red())
    messagetosend = ("{0.author} just tried to mass-ping.".format(ctx.message))
    if ('@') in ctx.message.content and ('@someone' not in ctx.message.content):
        await bot.say(embed=error)
    if ('@everyone') in ctx.message.content:
        await bot.say(embed=errorm)
        await bot.send_message(await bot.get_user_info("345307151989997568"), messagetosend)
    if ('@') not in ctx.message.content or ('@someone' in ctx.message.content):
        await bot.say(message)

@bot.command(pass_context=True, aliases=["urgentreport", "reporturgent"])
async def urgent(ctx, *, message):
    messagetosend = """User **{0.author}** sent the following report:

'""".format(ctx.message) + message + "'"
    await bot.delete_message(ctx.message)
    await bot.send_message(await bot.get_user_info("345307151989997568"), messagetosend)
    await bot.send_message(await bot.get_user_info("295612342274621442"), messagetosend)
    await bot.send_message(await bot.get_user_info("369984506809155586"), messagetosend)
    await bot.send_message(await bot.get_user_info("152190605970112512"), messagetosend)
    await bot.send_message(await bot.get_user_info("339886120407924736"), messagetosend)


@bot.command(pass_context=True, aliases=["suggest", "report"])
async def suggestion(ctx, *, message):
    messagetosend = """User **{0.author}** suggested/reported the following:

'""".format(ctx.message) + message + "'"
    channel = bot.get_channel("427219707683405844")
    await bot.send_message(channel, messagetosend)
    await bot.delete_message(ctx.message)

    

class Moderating:


    @commands.command(pass_context = True, aliases=["prune", "purge", "delete"])
    @commands.has_role("Staff")
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        for amount in range(int(amount), 0, -100):
            await bot.purge_from(channel, limit=int(amount))

    @commands.command(pass_context = True)
    @commands.has_role("Staff")
    async def gifblacklistg(self, ctx, something):
        n = 0
        confirm = something + " has been added to the blacklist."
        if len(str(something)) > n:
            list.append(blacklistg, something)
            await bot.say(confirm)
        else:
            em = discord.Embed(title="Error", description="Please input a keyword.", colour=discord.Colour.red())
            await bot.say(embed=em)


    @commands.command(pass_context = True)
    @commands.has_role("Staff")
    async def gifblacklistn(self, ctx, something=None):
        n = 0
        if something is None:
            em = discord.Embed(title="Error", description="Please input a keyword.", colour=discord.Colour.red())
            await bot.say(embed=em)
        elif len(str(something)) > n:
            confirm = something + " has been added to the blacklist."
            list.append(blacklistn, something)
            await bot.say(confirm)


class Info:

    @commands.command()
    async def uptime(self):
        uptimemessage = ("I've been online since " + str(uptimedict['timeuptime']) + " UTC.")
        await bot.say(uptimemessage)

    @commands.command()
    async def ping(self):
        await bot.say("Pong!")


    @commands.command(aliases=["about"])
    async def info(self):
        uptimemessage = ("I've been online since " + str(uptimedict['timeuptime']) + " UTC.")
        em = discord.Embed(title="About this bot", description="All about The Baking Bot.", colour=discord.Colour.green())
        em.add_field(name="Developers", value="Slowly#1846, Chanku#4372", inline=False)
        em.add_field(name="Thank-yous", value="Special thanks to Sebi's Bot Tutorial, this bot wouldn't have been possible without your help.", inline=False)
        em.add_field(name="Uptime", value=uptimemessage, inline=False)
        em.add_field(name="Version", value="Still in development.", inline=False)
        await bot.say(embed=em)

    @commands.command()
    async def tumblr(self):
        await bot.say("""Here is our official tumblr.
https://thebakingspot.tumblr.com/""")

    @commands.command()
    async def faq(self):
        await bot.say("""Here is a link with all FAQ's.
https://thebakingspot.tumblr.com/faq""")

    @commands.command(aliases=["app", "staffapp", "staffapps", "application"])
    async def apps(self):
        await bot.say("""Here is the app to become event manager.
https://goo.gl/forms/JDNVlMFNb34vk2Ko2
Here is the app to become staff.
https://goo.gl/forms/u8EuMf6RiBSFjxqy1""")


    @commands.command(aliases=["feedbackform"])
    async def feedback(self):
        await bot.say("""Send a completely anonymous report or feedback regarding the server, other members, or Staff.
https://goo.gl/forms/2pO3gDoxKz45mNh92""")


    @commands.command()
    async def invite(self):
        await bot.say("https://discord.io/thebakingspot")


    @commands.command(aliases=["help", "cmds", "commandlist", "commandslist"])
    async def commands(self):
        em = discord.Embed(description="""These are all the commands of The Baking Bot, the official bot for The Baking Spot.
The words in [] are aliases.
If you need help with mental health, please check the Mental Health section on the server and in this message.

•  •  •  •  •  •  •  •""", colour=discord.Colour.green())
        em.add_field(name="INFO", value="""**info**   -   Shows basic info about the bot. [about]
**uptime**   -   Shows the bot's uptime.
**commands**   -   Shows this message. [help, commandslist]
**ping**   -   Are you alive, bot?""", inline=False)
        em.add_field(name="MENTAL HEALTH", value="""**anxiety**   -   Breathing gif. [anxious, breathing, calm]
**grounding**   -   Grounding exercises. [dissociation, panic, flashbacks]
**emergency**   -   Links to a page with emergency resources. Use this in case of serious suicidal ideation.
**support**   -   If you need help or advice urgently, check this out. [getsupport, gethelp]
**positivity**   -   Displays a random nice little gif! [positive]
**therapy**   -   So you're looking for therapy? [therapist, counsellor, counselling]
**cheaptherapy**   -   If you're looking for low-cost/online therapy. [onlinetherapy, lowcosttherapy]
**database**   -   Various databases for group therapy, therapists, and so on. [therapydatabase]
""", inline=False)
        em.add_field(name="FUN AND MISC.", value="""**say**   -   Bot repeats what you say. [echo]
**compliment**   -   Displays a random compliment or says something reassuring. [randomcompliment, reassuring]
**dice**   -   Throws a dice. [dicethrow, throwdice]
**coinflip**   -   Flips a coin. [coin, flipcoin]
**question**   -   Ask the bot a yes or no question. [ask]
**randomgif**   -   Sends a random gif from giphy. [gifrandom, gif]
**dessert**   -   Displays a random gif of a dessert.
**cornyjoke**   -   Makes a corny joke. [joke, pun, randomjoke, randompun]""", inline=False)
        em.add_field(name="MODERATING (Staff only)", value="""**clear**   -   Delete messages. [prune, purge, delete]
**gifblacklistn**   -   Adds a word to the NSFW blacklist.
**gifblacklistg**   -   Adds a word to the violence blacklist.
""", inline=False)
        em.add_field(name="SERVER-RELATED", value="""**faq**   -   Displays link to our FAQ page on Tumblr.
**tumblr**   -   Link to the official Tumblr.
**staffapp**   -   Link to all the application forms. [apps]
**report**   -   Send a (non-urgent) report or suggestion to Staff, regular members will NOT see your message. [suggestion]
**urgentreport**   -   Send an __urgent__ report to Staff, regular members will NOT see your message. __Do not abuse this command.__ [urgent, reporturgent]
**feedback**   -   Send feedback, suggestions, or reports through an anonymous form. Nobody, not even Staff, will know who sent it. [feedbackform]
**invite**   -   Permanent invite to The Baking Spot!""")
        await bot.say (embed=em)


class MentalHealth:

    @commands.command(aliases=["positive"])
    async def positivity(self):
        pos = random.choice(["""Hey there, here's your daily nice gif.
        https://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4""", """Hey there, here's your daily nice gif. (source: teenypinkbunny)
        https://78.media.tumblr.com/8b468c1f9c20ca5f9483da6753460ec2/tumblr_onfpirBibx1tyggbco1_1280.gif""", """Hey there, here's your daily nice gif.
        https://giphy.com/gifs/chuber-turtle-hang-in-there-l1J3zw3sgJ6Ye6I4E""", """Hey there, here's your daily nice gif.
        https://78.media.tumblr.com/c0a1ffdef8c5b710769595cdf1119356/tumblr_on4s1k5Gru1w7ymkuo1_500.gif""", """Hey there, here's your daily nice gif. (source: fuwaprince)
        https://78.media.tumblr.com/8317376ec2f138b962d7dec63d479c46/tumblr_os6c25dzp21w4zse0o1_r1_500.gif""", """Hey there, here's your daily nice gif. (source: gogh-save-the-bees)
        https://78.media.tumblr.com/a92282dfc57d01e2e29184e3ed12fa5d/tumblr_otngozhihv1ut0lfho1_400.gif""", """Hey there, here's your daily nice gif.
        https://78.media.tumblr.com/7ba86c4cbc0b0f8fc981ca780fe8bb61/tumblr_osdkc2EJZL1w4zse0o1_1280.gif""", """Hey there, here's your daily nice gif. (source: positiveupwardspiral)
        https://78.media.tumblr.com/3914e99610371d427989d5146c42b85e/tumblr_p0981oKsrJ1vimk88o1_400.gif""", """Hey there, here's your daily nice gif. (source: fuwaprince)
        https://78.media.tumblr.com/2bbe256eba6d07ea6df9698dd20dfa65/tumblr_ot4afrYG181w4zse0o1_500.gif""", """Hey there, here's your daily nice gif. (source: fuwaprince)
        https://78.media.tumblr.com/6acf4ed92328f675ae8890df51b23794/tumblr_os27xwOzXz1w4zse0o1_500.gif""", """Hey there, here's your daily nice gif. (source: vanish)
        https://78.media.tumblr.com/ca9372839569a8406c0709bcc50a15ec/tumblr_p2iebnGUZr1sga7ujo1_500.gif""", """Hey there, here's your daily nice gif.
        https://78.media.tumblr.com/e0e093271b5657b75000f693bb48d877/tumblr_opy7xzfkJS1tssyz8o1_500.gif""", """Hey there, here's your daily nice gif. (source: positiveupwardspiral)
        https://78.media.tumblr.com/91fbd29211a1c7b06e7a16adf2deae50/tumblr_ozl7ooyZxQ1vimk88o1_400.gif""", """Hey there, here's your daily nice gif. (source: positiveupwardspiral)
        https://78.media.tumblr.com/dd5e45b3690ac2e979bc694ea473cf0b/tumblr_oyo1zfEii61vimk88o1_400.gif""", """Hey there, here's your daily nice gif. (source: gogh-save-the-bees)
        https://78.media.tumblr.com/4b8c9b079cd3da2d74275d3063d83b72/tumblr_oxidf7tQjz1ut0lfho1_500.gif""", """Hey there, here's your daily nice gif. (source: magical-latte)
        https://78.media.tumblr.com/d2fa0d7d4ca67af23750bb79a674d5c2/tumblr_p67f6ugJp91x69labo1_500.gif""", """Hey there, here's your daily nice gif.
        https://78.media.tumblr.com/85efdd7380284bd7279a0839e9674f96/tumblr_oqish5aNqX1ufccs2o1_500.gif""", """Hey there, here's your daily nice gif. (source: faiemagick)
        https://78.media.tumblr.com/bf7cad140e3e113cd4062b0377842ca3/tumblr_otogrpArAo1wo3hpco1_1280.gif"""])
        await bot.say(pos)

    @commands.command(aliases=["breathing", "calm", "anxious", "breathe"])
    async def anxiety(self):
        image = random.choice(["""Hello there, here's a gif for a breathing exercise.
https://media.giphy.com/media/3oxQNhjjZKLPs26Mve/giphy.gif""", """Hello there, here's a gif for a breathing exercise.
https://i.imgur.com/XbH6gP4.gif""", """Hello there, here's a gif for a breathing exercise.
https://media.giphy.com/media/8YfwmT1T8PsfC/giphy.gif""", """Hello there, here's a gif for a breathing exercise.
http://karlolabs.com/wp-content/uploads/2017/01/breathing.gif""", """Hello there, here's a gif for a breathing exercise.
http://i67.tinypic.com/2qant76.gif""", """Hello there, here's a gif for a breathing exercise.
https://media.boingboing.net/wp-content/uploads/2016/11/tumblr_og31bxrtOn1qls18ho6_400.gif"""])
        await bot.say(image)

    @commands.command(aliases=["ground", "dissociation", "panic", "flashbacks", "flashback"])
    async def grounding(self):
        ground = random.choice(["""Hey there, here are a few ideas to ground yourself.
These can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.
    - Choose a letter of the alphabet and try and come up with as many examples of a category you choose as you can. For example, animals that start with D: dog, deer, dingo, donkey, etc. Or vegetables that start with C: cucumber, cauliflower, celery, etc.
    - Count backwards from 100 by 3s, 6s, or 7s.
    - Describe an every day event or process in great detail, listing all of the steps in order and as thoroughly as possible (e.g., how to cook a meal)
    - Say or think to yourself: "My name is (...). I am safe right now. I am (...) years old and currently at (place). The date is (...). If I need help, I can contact (...). Everything is going to be alright, I can handle this."
    - Name five things that you see, four that you can touch, three that you hear, and two that you smell or taste, and then one thing that you like about yourself.
    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more.""",
    """Hey there, here are a few ideas to ground yourself.
These can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.
    - Touch and hold objects around you. Compare the feel, weight, temperature, textures, colors, and materials, describe them to yourself.
    - Squeeze a pillow, stuffed animal, or rubber ball, touch sandpaper (gently), sponges, denim, pop bubble wrap, rip up paper, run lukewarm water on your hands or splash your face with it (be careful).
    - Picture yourself breathing in relaxation/positive feelings/strength and breathing out negativity. You can also imagine you're breathing in soothing colors (blue, purple, green) and out intense colors (red, black).
    - Put your feet on the floor, gently squeeze or rub your legs and sit upright. 'Push' with your feet, almost as if you wanted to stand up, but do *not* stand up. Notice how your muscles work and how your body tenses.
    - If possible, crack a window and notice the cold air, the new sounds, and all the smells. Describe them to yourself.
    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more.""",
    """Hey there, here are a few ideas to ground yourself.
These can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.
    - Ask a friend for a reality-test. If you aren’t sure if something you’re feeling, seeing, hearing or thinking is real, ask a safe friend to help you decide what is fact, what is fiction, what is a flashback, and so on.
    - Do a few jumping jacks, sit-ups, or push-ups.
    - Try counting by 3's or 7's up to 200, then try multiplying by them.
    - Play with a tangle or a fidget cube. (Fidget spinners are not recommended!)
    - Remind yourself that extreme emotions, panic/anxiety attacks, flashbacks, or dissociation will go away just as they came. They cannot "hurt" you.
    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more."""])
        await bot.say(ground)


    @commands.command(aliases=["gethelp", "getsupport"])
    async def support(self):
            websites = """If you need advice/help or to vent, here are some links for you.
<https://www.7cups.com>
<https://mellowtalk.com/>
<http://blahtherapy.com/chat-hub/>
<https://ginger.io/>
<https://kooth.com/>
<https://www.iprevail.com/>
<https://www.imalive.org/>
<https://www.reddit.com/r/KindVoice/>
<https://thebakingspot.tumblr.com/ineedhelp>"""
            await bot.say(websites)

    @commands.command(aliases=["cheaptherapy", "lowcosttherapy", "onlinetherapy"])
    async def freetherapy(self):
            websites = """Here are some places to get free or low-cost professional help online.
We also recommend you try the `tbs!database` command.

<https://www.talkspace.com/>
<http://blahtherapy.com/>
<https://www.betterhelp.com/>
<https://www.iprevail.com/>
<https://trauma-crocodile.tumblr.com/supportmentalhealth>"""
            await bot.say(websites)

    @commands.command(aliases=["counsellor", "therapist", "counselling"])
    async def therapy(self):
        message = discord.Embed(title="Commands", description ="""Hello! If you are looking for low-cost or free therapy, please use
the command `tbs!freetherapy`.
If you're looking for therapist databases instead, please use
the command `tbs!database`.""", colour=discord.Colour.green())
        await bot.say(embed=message)
            

    @commands.command(aliases=["database", "databasetherapy"])
    async def therapydatabase(self):
            websites = """Here are some databases to find a therapist (counsellor, psychologist, psychiatrist, LMFT, etc.) or other types of treatment, such as support groups or facilities.

**International or multiple countries**
<https://members.nielasher.com/>
<http://www.therapistlocator.net/imis15/tl/Default.aspx>
<https://www.therapytribe.com/>
<https://www.onlinecounselling.com/therapist-finder/>
<https://www.goodtherapy.org/international-search.html>
<https://help.recoverywarriors.com/listings/?search_keywords=&search_location=&search_radius=500&search_lat=0&search_lng=0&search_region=>

**USA & Canada**
<https://www.sidran.org/help-desk/get-help/>
<https://anxietydepressionassoc.site-ym.com/?page=FATMain>
<https://www.networktherapy.com/directory/find_therapist.asp>
<https://www.psychologytoday.com/us/therapists/>
<http://www.findcbt.org/xFAT/index.cfm>
<http://www.isst-d.org/default.asp?contentID=18>

**UK**
<https://www.bps.org.uk/public/find-psychologist>
<https://www.psychotherapy.org.uk/>
<https://www.bacp.co.uk/>
<https://www.nhs.uk/Service-Search/Psychological%20therapies%20(IAPT)/LocationSearch/10008>
<http://www.callhelpline.org.uk/Help.asp#search>
<http://www.gofal.org.uk/journeys/>
<https://www.bpdworld.org/therapeutic-communities.html>
<https://www.beateatingdisorders.org.uk/support-services/online-groups>

**Australia**
<https://www.1800respect.org.au/services/>
<http://www.oneinthree.com.au/servicesandresources/>
<https://lysnhealth.com.au/>
<https://www.psychology.org.au/Find-a-Psychologist>
"""
            await bot.say(websites)


class Fun:


    @commands.command(aliases=["coin", "flip", "flipcoin"])
    async def coinflip(self):
        choices = random.choice(['Heads!', 'Tails!'])
        await bot.say(choices)

    @commands.command(aliases=["reassuring", "randomcompliment", "comfort", "comforting"])
    async def compliment(self):
        randomcomp = random.choice(["You're so resourceful.", "You're such a strong person.",
                                "Your light shines so brightly.", "You matter, and a lot.",
                                "You are so brave.", "You have an incredible talent even if you don't see it.",
                                "You are deserving of a hug right now.", "You're more helpful than you realize.",
                                "You can inspire people.", "I bet you do the crossword puzzle in ink.",
                                "You're someone's reason to smile, even if you don't realize it.",
                                "It's so great to see you're doing your best.", "Your smile can make someone's day.",
                                "You've always ben able to always figure out how to pick yourself up.", "Your ideas matter.",
                                "Your feelings matter.", "Your emotions matter.", "Your opinions matter.", "Your needs matter.",
                                "Your own vision of the world is unique and interesting.",
                                "Even if you were cloned, you'd still be one of a kind. (And the better one between the two.)",
                                "You are more unique and wonderful than the smell of a new book.",
                                "You're great at being you! No one can replace you - so keep it up.",
                                "You can get through this.", "If you're going through something, remember: this too shall pass.",
                                "You deserve to get help if you need it.", "You - yes you - are valid.", "You are more than enough.",
                                "Your presence is appreciated.", "You can become whoever you want to be.", "You deserve to be listened to.",
                                "You deserve to be heard.", "You deserve to be respected.", "You're an absolute bean.",
                                "You’re trying your best and everyone sees that.",
                                "Even if you feel like you're getting nowhere you're still one step ahead of yesterday - and that's still progress.",
                                "You're growing so much, and if you can't see it now, you certainly will in a few months.",
                                "You're strong for going on even when it's so hard."])
        await bot.say(randomcomp)


    @commands.command(aliases=["throwdice", "dicethrow", "throw"])
    async def dice(self):
        throw = random.choice(['1.', '2.', '3.', '4.', '5.', '6.'])
        await bot.say(throw)




    @commands.command(pass_context=True)
    async def emergency(self, ctx):
        await bot.say("""Hey there {0}, if anyone you know is in any kind of emergency, please visit the following page:
https://thebakingspot.tumblr.com/ineedhelp
I suggest you also try the `tbs!help`, `tbs!support` and `tbs!therapy` commands - in the appropriate bot channel.""".format(ctx.message.author.mention))


    @commands.command(aliases=["joke", "jokes", "cheesyjoke", "randomjoke", "pun", "randompun", "cheesypun", "cornypun", "puns"])
    async def cornyjoke(self):
        randomjoke = random.choice(["What do you call a thieving alligator? A crookodile.",
                                    "What did the watermelon say to the cantaloupe? You're one in a melon.",
                                    "How do you put a baby alien to sleep? You rocket.",
                                    "How do you throw a space party? You planet.",
                                    "What do you call a bear with no teeth? A gummybear.",
                                    "What happens if you eat too much Eastern food? You falafel.",
                                    "What does a house wear? Address.",
                                    "Why is it hard to be in a relationship with a thief? Because they always take things... literally.",
                                    "Why can't a bycicle stand on its own? Because it's two tired.",
                                    "Do french people play videogames? Wii.",
                                    "Did you hear about the joke about German sausages? It's the wurst.",
                                    "What does a falling star say to start a fight? Comet me bro.",
                                    "What did E.T.'s mother say to him when he got home? 'Where on Earth have you been?!'."
                                    "Why are calendars so popular? They have lots of dates.",
                                    "Why do musicians always get good grades? They have lots of notes.",
                                    "What did the traffic light say to the car? Don’t look! I’m about to change.",
                                    "Why was the little strawberry crying? Its mom was in a jam.",
                                    "Why are frogs so happy? They eat whatever bugs them.",
                                    "What do you call a guy with a rubber toe? Roberto.",
                                    "What do you call a bee that’s having a bad hair day? A frisbee.",
                                    "Why wouldn’t the shrimp share his treasure? Because it was a little shellfish.",
                                    "If a seagull flies over the sea, what flies over the bay? A bagel.",
                                    "What happens to deposed kings? They get throne away.", "What kind of tree do fingers grow on? A palm tree.",
                                    "What do you call a rabbit with fleas? Bugs Bunny.", "What happens to illegally parked frogs? They get toad away.",
                                    "What do you call a fish with no eyes? A fsh.", "What do prisoners use to call each other? Cell phones.",
                                    "What happens when a clock's hungry? It goes back four seconds.",
                                    "How was Rome split in two? With a pair of Ceasars.",
                                    "What did the corn say in response to a compliment? Aw, shucks.",
                                    "What do you tell maize on graduation day? Corn-gratulations.",
                                    "What do you call a beautiful pumpkin? GOURDgeous.", "What did the buffalo say to his son? Bison.",
                                    "What do you call a fake noodle? An impasta.", "How do trees access the internet? They log on.",
                                    "What do you call a pirate who sells corn? A buccaneer.",
                                    "Want to hear a pizza joke? Actually never mind, it’s too cheesy.",
                                    "Why shouldn’t you trust atoms? They make up everything."])
        await bot.say(randomjoke)

    @commands.command(aliases=["ask"])
    async def question(self):
        quest = random.choice(['Yes.', 'No.', 'Yes!', 'No!', 'What? No!', 'Probably not.',
                                   'Maybe...', 'Always.', 'Never.', 'Sometimes...', 'Almost certainly.',
                                   'I hope not!', 'Yep!', 'Yes...?', 'No...?', 'Always!', 'Never!',
                                   'Not sure...', 'Of course!', 'Of course not!', 'Of course.', 'DUH!',
                                   'Why not?', "Why though?"])
        await bot.say(quest)



    @commands.command(aliases=["randomdessert"])
    async def dessert(self):
        dessert = random.choice(["""Here's your random dessert.
https://giphy.com/gifs/animation-illustration-birthday-l0Iy4ppWvwQ4SXPxK""", """Here's your random dessert.
https://giphy.com/gifs/huffingtonpost-food-cake-dessert-QWS2I0L6UssF2""", """Here's your random dessert.
https://giphy.com/gifs/cake-food-anime-kfMGD3KwdIrpm""", """Here's your random dessert.
https://giphy.com/gifs/banana-pkBEq1dfFIT8A""", """Here's your random dessert.
https://giphy.com/gifs/food-delicious-cupcake-VW5GUg86EaX2E""", """Here's your random dessert.
https://giphy.com/gifs/shakingfoodgifs-food-kawaii-shaking-qLzDdOe6D483m""", """Here's your random dessert.
https://giphy.com/gifs/is-reasons-superior-UAzaYopok9PsQ""", """Here's your random dessert.
https://giphy.com/gifs/is-reasons-superior-oDJss7tbDEzZu""", """Here's your random dessert.
https://giphy.com/gifs/dessert-rpNkH3RAwkTXW""", """Here's your random dessert.
https://giphy.com/gifs/cake-dessert-43o1oy5xdOfL2""", """Here's your random dessert.
https://giphy.com/gifs/is-reasons-superior-E5efe2XtMUdTq""", """Here's your random dessert.
https://giphy.com/gifs/food-chocolate-dessert-111oCumklJpuJW""", """Here's your random dessert.
https://giphy.com/gifs/waffles-tDnKZAsxCZHRC""", """Here's your random dessert.
https://giphy.com/gifs/food-dessert-macaroons-KnfnufBkPtGAo""", """Here's your random dessert.
https://giphy.com/gifs/fruit-7z4lmNtTmuREI""", """Here's your random dessert.
https://giphy.com/gifs/shakingfoodgifs-food-dessert-pie-pdfnRGpNQzePC""", """Here's your random dessert.
https://giphy.com/gifs/white-dessert-sphere-rczvneQ6Ziwx2""", """Here's your random dessert.
https://giphy.com/gifs/donut-drool-enchanting-arEGphwGhT7dC""", """Here's your random dessert.
https://giphy.com/gifs/dessert-ice-cream-food-ApRorrZknEPw4"""])
        await bot.say(dessert)


    @commands.command(pass_context=True, no_pm=True, aliases=["randomgif", "gif"])
    async def gifrandom(self, ctx, *keyword):
        messagetosendn = ("{0.author} just tried to search for a NSFW gif.".format(ctx.message))
        messagetosendg = ("{0.author} just tried to search for a gore/horror gif.".format(ctx.message))
        errorn = discord.Embed(title="Error!", description="Don't use this to search NSFW gifs.", colour=discord.Colour.red())
        errorg = discord.Embed(title="Error!", description="Don't use this to search gore, violence, or horror. This is against rules.", colour=discord.Colour.red())
        keyword = "+".join(keyword)
        if keyword in blacklistn:
            await bot.say(embed=errorn)
            await bot.send_message(await bot.get_user_info("345307151989997568"), messagetosendn)
            return

        if keyword in blacklistg:
            await bot.say(embed=errorg)
            await bot.send_message(await bot.get_user_info("345307151989997568"), messagetosendg)
            return


        elif keyword:
            keyword = "+".join(keyword)

            url = ("http://api.giphy.com/v1/gifs/random?&api_key={}&tag={}".format(GIPHY_API_KEY, keyword))

            async with aiohttp.get(url) as r:
                result = await r.json()
                if r.status == 200:
                    if result["data"]:
                        await bot.say(result["data"]["url"])

        else:
            em = discord.Embed(title="Error", description="Please input a keyword.", colour=discord.Colour.red())
            await bot.say(embed=em)




def secrets_check():
    secrets = ""
    try:
        with open('secrets.txt', 'r') as secret:
            secrets = secret.read()
        discord_key = secrets.split("discord_client_key =")[1].split("\n")[0].strip(" ")
        giphy_api_key = secrets.split("giphy_api_key =")[1].split("\n")[0].strip(" ")
        if not discord_key or not giphy_api_key:
            raise SyntaxError("Missing discord_key or giphy_api_key!")
    except FileNotFoundError:
        with open('secrets.txt', 'w') as secret:
            secret.write("discord_client_key = \n")
            secret.write("giphy_api_key = \n")
        raise SyntaxError("Fill in secrets.txt and then re-run!")
    return discord_key, giphy_api_key

bot.add_cog(Info())
bot.add_cog(Fun())
bot.add_cog(MentalHealth())
bot.add_cog(Moderating())

discord_key, giphy = secrets_check()
GIPHY_API_KEY = giphy
bot.run(discord_key)
