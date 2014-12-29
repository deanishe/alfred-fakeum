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

 |          Name         |                                                                Example                                                                |
 |-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
 | Name                  | Arabella Hahn-Matthäi                                                                                                                 |
 | First Name            | Jeffrey                                                                                                                               |
 | Last Name             | Renner                                                                                                                                |
 | Email                 | augustina.braun@ratke-hamill.org                                                                                                      |
 | Email (corporate)     | fridolin68@schueler.de                                                                                                                |
 | Email (free)          | gkautzer@gmail.com                                                                                                                    |
 | Email (safe)          | cruickshank.hymen@example.com                                                                                                         |
 | Email domain (free)   | hotmail.com                                                                                                                           |
 | Address               | Ronda de Claudia Alegre 9<br>Melilla, 57359                                                                                           |
 | Street                | Paseo Lila Roca 52                                                                                                                    |
 | Street Name           | Cuesta Mauricio Sotelo                                                                                                                |
 | City                  | León                                                                                                                                  |
 | State                 | Vizcaya                                                                                                                               |
 | State abbr.           | WA                                                                                                                                    |
 | Country               | Albanien                                                                                                                              |
 | TLD                   | de                                                                                                                                    |
 | Domain Name           | ankunding.org                                                                                                                         |
 | Domain Word           | tormo-vazquez                                                                                                                         |
 | IP Address (IPv4)     | 23.1.170.203                                                                                                                          |
 | IP Address (IPv6)     | 9144:9c8a:e1b3:db99:df20:be35:8fd0:1ab2                                                                                               |
 | URI                   | http://cummerata-kuvalis.com/app/category/register.php                                                                                |
 | URI path              | tags                                                                                                                                  |
 | URL                   | http://pollich-rath.com/                                                                                                              |
 | Corporate BS          | revolutionize virtual e-markets                                                                                                       |
 | Corporate catchphrase | Optional executive leverage                                                                                                           |
 | Company               | Löwer AG                                                                                                                              |
 | Company suffix        | LLC                                                                                                                                   |
 | Paragraph             | Error culpa amet voluptatem et delectus labore. Facilis deserunt quae aliquid mollitia. Aut esse qui totam dolor consequatur dolorem. |
 | Sentence              | Provident vel quod dolorem in.                                                                                                        |
 | Word                  | sint                                                                                                                                  |
 | Date                  | 1985-05-14                                                                                                                            |
 | Datetime              | 1981-01-28 14:37:06                                                                                                                   |
 | ISO 8601 Datetime     | 1990-07-30T08:41:53                                                                                                                   |
 | Time                  | 00:42:12                                                                                                                              |
 | Timezone              | Europe/Istanbul                                                                                                                       |
 | UNIX timestamp        | 261754578                                                                                                                             |


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
