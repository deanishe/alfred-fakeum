Alfred Fakeum
=============

Generate fake test data in Alfred for testing.

![][demo]


Download & installation
-----------------------

Download the workflow from [GitHub][gh-releases], then double-click to install.

**Note**: Files with the extension `alfred3workflow` are not compatible with Alfred 2.


Usage
-----

- `fake [<query>]` — List/filter available fake data types
    - `↩`, `⌘+C` or `⌘+NUM` — Copy one fake datum to clipboard
    - `⌘+↩` — Paste fake datum into frontmost app
    - `⇥` — Specify number of datasets to copy to clipboard
    - `⌘+L` — Show generated data in Alfred's Large Text window
- `fakeconfig [<query>]` — Edit workflow settings
    - `An update is available` / `Check for update` — Check for and/or install an updated version of the workflow
    - `Notifications` — Turn notifications on/off
        - `↩` — Toggle on/off
    - `Locales` — Turn locales for fake data on/off
        - `↩` — Show & edit active locales
            - `[<query>]` — Filter locales
            - `↩` — Toggle locale on/off
    - `Documentation` — Open GitHub README in your browser
    - `Report Problem` — Open the issue tracker in your brower
    - `Get Help` — Open the workflow's thread on AlfredForum.com in your browser

If you specify multiple data, e.g. `fake Name ✕ 10` for 10 names, the data will be separated by newlines (`\n`).

In the case of `Paragraph` and `Address` types, the data will be separated by two newlines (`\n\n`).

There is also a **Snippet Trigger** (`xxfake` by default) to insert fake data directly into other applications.


## Supported data types ##

|           Name           |                                                                                           Example                                                                                            |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                     | Dr. Venie Mayer DVM                                                                                                                                                                          |
| First Name               | Mercedes                                                                                                                                                                                     |
| Last Name                | Greco                                                                                                                                                                                        |
| Email                    | jan.hettinger@yahoo.com                                                                                                                                                                      |
| Email (corporate)        | kaul.kurt@mitschke.org                                                                                                                                                                       |
| Email (free)             | xpardo@hotmail.com                                                                                                                                                                           |
| Email (safe)             | fabio.pellegrino@example.org                                                                                                                                                                 |
| Email domain (free)      | yahoo.de                                                                                                                                                                                     |
| Social Security No.      | 079-87-3633                                                                                                                                                                                  |
| Phone No.                | +49(0)7060869380                                                                                                                                                                             |
| MSISDN                   | 4839636333647                                                                                                                                                                                |
| Address                  | C. de Aya Fernandez 34<br/>Palencia, 60850                                                                                                                                                   |
| Street                   | Vicolo Rudy 4                                                                                                                                                                                |
| Street Name              | Pasadizo Miranda Rivero                                                                                                                                                                      |
| City                     | Witzenhausen                                                                                                                                                                                 |
| Postcode                 | 73068                                                                                                                                                                                        |
| State                    | Almería                                                                                                                                                                                      |
| State abbr.              | TN                                                                                                                                                                                           |
| Country                  | Bangladesh                                                                                                                                                                                   |
| TLD                      | net                                                                                                                                                                                          |
| Domain Name              | feeney.net                                                                                                                                                                                   |
| Domain Word              | milani                                                                                                                                                                                       |
| IP Address (IPv4)        | 177.119.72.157                                                                                                                                                                               |
| IP Address (IPv6)        | 4f17:280f:7cdb:0834:dac1:3841:9520:a42f                                                                                                                                                      |
| URI                      | http://greco-piras.org/search.htm                                                                                                                                                            |
| URI path                 | app/posts/main                                                                                                                                                                               |
| URL                      | http://www.soeding.de/                                                                                                                                                                       |
| User-Agent               | Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 6.1; Trident/3.0)                                                                                                                              |
| Corporate BS             | orchestrate magnetic eyeballs                                                                                                                                                                |
| Corporate catchphrase    | Versatile global productivity                                                                                                                                                                |
| Company                  | De luca, Russo e Piras s.r.l.                                                                                                                                                                |
| Company suffix           | LLC                                                                                                                                                                                          |
| Paragraph                | Vitae atque sed soluta vero culpa ut. Vero occaecati quaerat voluptas quidem at et fugit voluptas. Quam est labore vitae consequatur. Facilis deleniti quisquam accusantium quas est magnam. |
| Sentence                 | Tempore distinctio quia est nam neque.                                                                                                                                                       |
| Word                     | quia                                                                                                                                                                                         |
| Date                     | 2009-09-11                                                                                                                                                                                   |
| Datetime                 | 2014-11-07 10:26:03                                                                                                                                                                          |
| ISO 8601 Datetime        | 1983-08-30T00:44:16                                                                                                                                                                          |
| Time                     | 23:17:05                                                                                                                                                                                     |
| Timezone                 | Africa/Porto-Novo                                                                                                                                                                            |
| UNIX timestamp           | 1171262842                                                                                                                                                                                   |
| Credit Card Provider     | JCB 16 digit                                                                                                                                                                                 |
| Credit Card No.          | 4843693411367621                                                                                                                                                                             |
| Credit Card Expiry Date  | 11/27                                                                                                                                                                                        |
| Credit Card Full         | VISA 16 digit<br>Silja Gorlitz<br>4286433476525894<br>10/23<br>CVC: 973                                                                                                                      |
| Credit Card Security No. | 046                                                                                                                                                                                          |
| IBAN                     | DE60876246778887942622                                                                                                                                                                       |
| BBAN                     | 946840452091737213                                                                                                                                                                           |
| Bank Country Code        | DE                                                                                                                                                                                           |
| Currency                 | Qatari riyal                                                                                                                                                                                 |
| Currency Code            | MWK                                                                                                                                                                                          |
| Cryptocurrency           | Ethereum                                                                                                                                                                                     |
| Cryptocurrency Code      | PPC                                                                                                                                                                                          |
| EAN                      | 1089881348813                                                                                                                                                                                |
| EAN 8                    | 94266566                                                                                                                                                                                     |
| EAN 13                   | 1308583144852                                                                                                                                                                                |
| ISBN 10                  | 0-7288-0074-8                                                                                                                                                                                |
| ISBN 13                  | 978-0-7208-4271-5                                                                                                                                                                            |
| Colour Name              | MediumOrchid                                                                                                                                                                                 |
| Colour Name (Safe)       | silver                                                                                                                                                                                       |
| Hex Colour               | #64c47e                                                                                                                                                                                      |
| Hex Colour (Safe)        | #662200                                                                                                                                                                                      |
| RGB Colour               | 21,132,215                                                                                                                                                                                   |
| RGB CSS Colour           | rgb(187,70,174)                                                                                                                                                                              |
| Profession               | Animator                                                                                                                                                                                     |
| Licence Plate            | LU-XH-464                                                                                                                                                                                    |
| MD5 Hash                 | c9d4c30b62ede6a7a8a49a18355531a6                                                                                                                                                             |
| SHA1 Hash                | 134c12855595f5f10c2c4051d657f066aba5963e                                                                                                                                                     |
| SHA256 Hash              | 8ce283e129c02d4e669ba1bd8f79d0ce8de38bf26e80a8f2f8bf932ac3039086                                                                                                                             |
| Locale                   | hi_IN                                                                                                                                                                                        |
| Language Code            | nr                                                                                                                                                                                           |
| UUID4                    | 5dcc0030-d216-418c-863d-bd3946594970                                                                                                                                                         |
| Password (not secure!!)  | +AU86ZEs&X                                                                                                                                                                                   |



Supported locales
-----------------

**Note**: Not all locales support all data types.

- English
- German
- Spanish
- French
- Arabic
- Arabic (Egypt)
- Arabic (Jordan)
- Arabic (Palestine)
- Arabic (Saudi Arabia)
- Bosnian
- Bulgarian
- Chinese (China)
- Chinese (Taiwan)
- Croatian
- Czech
- Danish
- Dutch
- Dutch (Belgium)
- English (Australia)
- English (Canada)
- English (Great Britain)
- English (Thailand)
- English (United States)
- Estonian
- Finnish
- French (Switzerland)
- Georgian
- German (Austria)
- Ghanaian
- Greek
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Korean
- Latin
- Latvian
- Lithuanian
- Nepali
- Norwegian
- Persian
- Polish
- Portuguese (Brazil)
- Portuguese (Portugal)
- Russian
- Slovakian
- Slovenian
- Spanish (Mexico)
- Spanish (Spain)
- Swedish
- Thai
- Turkish
- Ukranian


Licensing, thanks
-----------------

Icons are from [Font Awesome][font-awesome] and [Material Design Iconic Font](material-icons) (both [SIL OFL 1.1 Licence][sil]).

Alfred Fakum uses the following libraries:

- [Faker][faker] ([MIT Licence][faker-licence])
- [docopt][docopt] ([MIT Licence][mit])
- [Alfred-Workflow][alfred-workflow] ([MIT Licence][mit])

[gh-releases]: https://github.com/deanishe/alfred-fakeum/releases/latest
[mit]: http://opensource.org/licenses/MIT
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[font-awesome]: http://fortawesome.github.io/Font-Awesome/
[material-icons]: http://zavoloklom.github.io/material-design-iconic-font/
[docopt]: http://docopt.org/
[faker]: http://www.joke2k.net/faker/
[faker-licence]: https://github.com/joke2k/faker/blob/master/LICENSE.txt
[sil]: http://scripts.sil.org/OFL
[demo]: https://raw.githubusercontent.com/deanishe/alfred-fakeum/master/demo.gif
