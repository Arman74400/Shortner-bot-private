from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi, Admins

I Am Linksmoney.in, Bulk Link Converter. I Can Convert Links Directly From Your Linksmoney Account,

1. Go To 👉 https://linksmoney.in/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)

/api(space)API Key 
(See Example.👇)
Example: /api de303d5270f481aec928f39883da7b7f9a8812ac 

➕ Hit 👉 /help To Know More Features Of This Bot.
➕ Hit 👉 /header To Get Help About Adding your Custom Header to bot.
➕ Hit 👉 /banner To Get Help About Adding your Custom Banner in posts.
➕ Hit 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You Want Any Other Shortner Link Converter Bot Instead Of linksmoney.in than contact at 👉 @netflix_india_007 (all shortners support available.)
"""

HELP_MESSAGE = """Hey there! My name is Linksmoney Bulk Converter Bot and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.

I have a ton of handy features to help you out, such as:

- Hyperlink support 🔗
- Button conversion support 🔘
- Domain inclusion and exclusion options 🌐
- Header and footer text support 📝
- Replace username function 📎
- Banner image support 🖼️
- Batch conversion for channel admins only 📊
- Channel support for admins only 📢

Useful commands:

- /start: Start me up! You probably already used this.
- /batch -100xxx: To shorten or convert all posts in your channel
"""

ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
`👨‍💻 Developer:` [Dev](t.me/badal6667rai)
`📢 Support:` [ADMIN](https://t.me/RIPLINKER)
"""


METHOD_MESSAGE = """
Current Method: SHORTENER
    
Methods Available:

NO METHODS AVAILABLE CONTACT @netflix_india_007
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("👈 Back", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("👈 Back", callback_data="start_command"),
        ],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help ✍️", callback_data="help_command"),
            InlineKeyboardButton("About 📢", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Connect Your Linksmoney Api 🖇️", url="https://Linksmoney.in/member/tools/api"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Connect Your KrishnaLink Api", url="https://krishnalink.com/member/tools/api"),
        ],
    ]
)


BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Supported website: Linksmoney.in

- 🔌 Your connected API: {shortener_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api 6LZq851sXoPHugiKQq`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Riplinker.in API, 
`/api [api]`
            
Ex: `/api 6LZq851sXofffPHugiKQq`

Supported Website: Linksmoney.in

Current Connected API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
