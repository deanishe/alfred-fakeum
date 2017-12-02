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

## Supported data types ##

|          Name         |                                                                                           Example                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                  | Dr. Venie Mayer DVM                                                                                                                                                                          |
| First Name            | Mercedes                                                                                                                                                                                     |
| Last Name             | Greco                                                                                                                                                                                        |
| Email                 | jan.hettinger@yahoo.com                                                                                                                                                                      |
| Email (corporate)     | kaul.kurt@mitschke.org                                                                                                                                                                       |
| Email (free)          | xpardo@hotmail.com                                                                                                                                                                           |
| Email (safe)          | fabio.pellegrino@example.org                                                                                                                                                                 |
| Email domain (free)   | yahoo.de                                                                                                                                                                                     |
| Address               | C. de Aya Fernandez 34<br/>Palencia, 60850                                                                                                                                                   |
| Street                | Vicolo Rudy 4                                                                                                                                                                                |
| Street Name           | Pasadizo Miranda Rivero                                                                                                                                                                      |
| City                  | Witzenhausen                                                                                                                                                                                 |
| State                 | Almería                                                                                                                                                                                      |
| State abbr.           | TN                                                                                                                                                                                           |
| Country               | Bangladesh                                                                                                                                                                                   |
| TLD                   | net                                                                                                                                                                                          |
| Domain Name           | feeney.net                                                                                                                                                                                   |
| Domain Word           | milani                                                                                                                                                                                       |
| IP Address (IPv4)     | 177.119.72.157                                                                                                                                                                               |
| IP Address (IPv6)     | 4f17:280f:7cdb:0834:dac1:3841:9520:a42f                                                                                                                                                      |
| URI                   | http://greco-piras.org/search.htm                                                                                                                                                            |
| URI path              | app/posts/main                                                                                                                                                                               |
| URL                   | http://www.soeding.de/                                                                                                                                                                       |
| Corporate BS          | orchestrate magnetic eyeballs                                                                                                                                                                |
| Corporate catchphrase | Versatile global productivity                                                                                                                                                                |
| Company               | De luca, Russo e Piras s.r.l.                                                                                                                                                                |
| Company suffix        | LLC                                                                                                                                                                                          |
| Paragraph             | Vitae atque sed soluta vero culpa ut. Vero occaecati quaerat voluptas quidem at et fugit voluptas. Quam est labore vitae consequatur. Facilis deleniti quisquam accusantium quas est magnam. |
| Sentence              | Tempore distinctio quia est nam neque.                                                                                                                                                       |
| Word                  | quia                                                                                                                                                                                         |
| Date                  | 2009-09-11                                                                                                                                                                                   |
| Datetime              | 2014-11-07 10:26:03                                                                                                                                                                          |
| ISO 8601 Datetime     | 1983-08-30T00:44:16                                                                                                                                                                          |
| Time                  | 23:17:05                                                                                                                                                                                     |
| Timezone              | Africa/Porto-Novo                                                                                                                                                                            |
| UNIX timestamp        | 1171262842                                                                                                                                                                                   |




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
