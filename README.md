# Alfred Fakum #

Generate fake test data in Alfred for testing.

![][demo]

## Download ##

Get the workflow from [GitHub][gh-releases] or [Packal][packal].

## Usage ##

- `fake [<query>]` — List/filter available fake data types
    - `↩`, `⌘+C` or `⌘+NUM` — Copy one fake datum to clipboard
    - `⌘+↩` — Paste fake datum into frontmost app
    - `⇥` — Specify number of datasets to copy to clipboard
    - `⌘+L` — Show generated data in Alfred's Large Text window
- `fakeconfig [<query>]` — Activate and deactivate locales for fake data
    - `↩` — Toggle selected locale on or off

If you specify multiple data, e.g. `fake Name ⟩ 10` for 10 names, the data
will be separated by newlines (`\n`).

In the case of `Paragraph` and `Address` types, the data will be separated
by two newlines (`\n\n`).

## Supported data types ##

|          Name         |                 Example                  |
|-----------------------|------------------------------------------|
| Name                  | Dean Bartoletti                          |
| First Name            | Aubrey                                   |
| Last Name             | Pinilla                                  |
| Email                 | trapp.teona@jopich.de                    |
| Email (corporate)     | eden83@oberbrunner.biz                   |
| Email (free)          | faylinn24@yahoo.de                       |
| Email (safe)          | paffrath.michel@example.net              |
| Email domain (free)   | hotmail.com                              |
| Address               | PSC 5021, Box 4004 APO AP 93413-5259     |
| Street                | Incrocio Martinelli 3                    |
| Street Name           | Callejón Eric Galván                     |
| City                  | Rothenburg oberauber                     |
| State                 | Asturias                                 |
| State abbr.           | PA                                       |
| Country               | Gibraltar                                |
| TLD                   | com                                      |
| Domain Name           | adams-baumbach.com                       |
| Domain Word           | albers                                   |
| IP Address (IPv4)     | 251.230.26.56                            |
| IP Address (IPv6)     | 6b64:501e:659d:8ebb:e4a4:c922:93dc:7fd3  |
| URI                   | http://www.vara-escribano.net/faq.jsp    |
| URI path              | categories/list/tags                     |
| URL                   | http://effertz.info/                     |
| Corporate BS          | revolutionize bleeding-edge partnerships |
| Corporate catchphrase | Synchronised hybrid adapter              |
| Company               | Barone-Piras SPA                         |
| Company suffix        | and Sons                                 |
| Sentence              | At illum eum rerum qui.                  |
| Word                  | dolorum                                  |
| Date                  | 2002-01-12                               |
| Datetime              | 1971-08-12 21:03:27                      |
| ISO 8601 Datetime     | 1992-07-31T06:39:02                      |
| Time                  | 06:28:44                                 |
| Timezone              | Pacific/Efate                            |
| UNIX timestamp        | 886420512                                |



## Supported locales ##

**Note**: Not all locales support all data types.

- Bulgarian
- Czech
- German
- Danish
- Greek
- English (CA)
- English (GB)
- English (US)
- Spanish (ES)
- Spanish (MX)
- Persian
- Finnish
- French
- Hindi
- Italian
- Korean
- Lithuanian
- Latvian
- Dutch
- Polish
- Portuguese (BR)
- Russian
- Slovenian
- Chinese (CN)
- Chinese (TW)

## Licensing, thanks ##

Icons are from [Font Awesome][font-awesome] ([SIL OFL 1.1 Licence][sil]).

Alfred Fakum uses the following libraries:

- [Faker][faker] ([licence][faker-licence])
- [docopt][docopt] ([MIT Licence][mit])
- [Alfred-Workflow][alfred-workflow] ([MIT Licence][mit])

[gh-releases]: https://github.com/deanishe/alfred-fakeum/releases
[packal]: http://www.packal.org/workflow/fakeum
[mit]: http://opensource.org/licenses/MIT
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[font-awesome]: http://fortawesome.github.io/Font-Awesome/
[docopt]: http://docopt.org/
[faker]: http://www.joke2k.net/faker/
[faker-licence]: https://github.com/joke2k/faker/blob/master/LICENSE.txt
[sil]: http://scripts.sil.org/OFL
[demo]: https://raw.githubusercontent.com/deanishe/alfred-fakeum/master/demo.gif
