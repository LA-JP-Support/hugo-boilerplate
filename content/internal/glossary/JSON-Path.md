+++
title = "JSON Path"
translationKey = "json-path"
description = "JSON Path je dotazovací syntaxe pro extrakci, vyhledávání a manipulaci s konkrétními hodnotami ze složitých struktur dat JSON pomocí stručných cestových výrazů."
keywords = ["JSON Path", "JSON data", "dotazovací syntaxe", "extrakce dat", "API testování"]
category = "AI Chatbot & Automatizace"
type = "glosář"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/JSON-Path/"

+++
## Co je JSON Path?

JSON Path je dotazovací jazyk navržený pro navigaci, extrakci a vyhodnocování prvků v rámci dokumentů JSON (JavaScript Object Notation). Je analogií k XPath pro XML a umožňuje cílené získávání dat z libovolné hloubky struktury JSON pomocí standardizované, čitelné syntaxe. JSON Path je široce využíván v programování, automatizaci, testování API, datovém inženýrství a správě konfigurace — je nezbytným nástrojem pro každého, kdo potřebuje efektivně pracovat s JSON daty.

- **Standardizace:**JSON Path byl standardizován v [RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535) organizací IETF, což poskytuje jednotnou syntaxi a sémantiku pro dotazovací výrazy JSONPath.
- **Podpora v různých jazycích:**JSON Path je implementován v mnoha programovacích jazycích (např. JavaScript, Python, Java, PHP a SQL databáze).
- **Použití:**Testování API, validace, extrakce dat, ETL procesy (Extract, Transform, Load), správa konfigurace a automatizace chatbotů.

**Příklad JSON:**```json
{
  "user": {
    "id": 123,
    "profile": {
      "name": "Alice",
      "roles": ["admin", "editor"]
    }
  }
}
```
**Extrakce ID uživatele:**```jsonpath
$.user.id
// Výsledek: 123
```
## Proč používat JSON Path?

JSON Path dramaticky zjednodušuje extrakci nebo ověřování dat ve vnořených dokumentech JSON. Umožňuje:

- Psát stručné dotazy pro získání dat v libovolné úrovni zanoření.
- Filtrovat pole a objekty na základě hodnot vlastností.
- Vybrat, transformovat nebo validovat data v odpovědích API, konfiguračních souborech, protokolech a databázích.
- Automatizovat opakované úlohy extrakce dat v programování, testování a analytice.

**Běžné scénáře použití:**- **Testování API & automatizace:**Ověření a validace konkrétních polí v odpovědích REST API (např. Postman, Rest-Assured).
- **Datové zpracovatelské toky:**Extrakce cílených dat z JSON protokolů nebo datových jezer pro analytiku a ETL.
- **Integrace s databází:**Dotazování na JSON sloupce v databázích (SQL Server, PostgreSQL, MongoDB).
- **Správa konfigurace:**Získání nebo úprava nastavení v JSON konfiguračních souborech.
- **AI Chatboti:**Parsování atributů uživatelů, záměrů nebo historie zpráv v JSON-formátovaných konverzacích.

## Syntaxe a operátory JSON Path

### Základní prvky syntaxe

Výrazy JSON Path se skládají z selektorů a operátorů pro procházení a filtrování JSON dat. Kompletní referenci najdete v [dokumentaci SmartBear JSONPath Syntax](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html) a [RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535).

#### 1. **Kořenový objekt (`$`)**- Označuje kořen dokumentu JSON.
- Příklad: `$.store` vybere objekt `store` na kořeni.

#### 2. **Operátory pro potomky (`.` a `[]`)**- Tečková notace (`.`): Přístup k podřízeným vlastnostem (např. `$.user.name`).
- Závorková notace (`['property']`): Pro názvy vlastností s mezerami, speciálními znaky nebo rezervovanými slovy (např. `$['user']['profile']`). Vždy se používají jednoduché uvozovky.

#### 3. **Přístup k poli**- Index (`[n]`): Vybere n-tý (od nuly) prvek (`$.store.book[0]`).
- Více indexů (`[n,m]`): Vybere více prvků (`$.store.book[0,2]`).

#### 4. **Operátor výřezu pole (`[start:end:step]`)**- Vybere rozsah prvků pole (ve stylu Pythonu).
- Příklady: `$.store.book[0:2]` vybere první dvě knihy; `$.store.book[::2]` každou druhou knihu.

#### 5. **Zástupný znak (`*`)**- Vybere všechny prvky na aktuální úrovni.
- Příklad: `$.store.book[*].author` získá všechny autory v poli knih.

#### 6. **Rekurzivní sestup (`..`)**- Vybere všechny odpovídající prvky v libovolné hloubce pod aktuálním uzlem.
- Příklad: `$..price` najde všechna pole `price` kdekoli v dokumentu.

#### 7. **Filtrační výrazy (`[?(...)]`)**- Filtrování prvků pole podle podmínky.
- Příklad: `$.store.book[?(@.price < 10)]` vybere knihy s cenou pod 10.
- `@` odkazuje na aktuální prvek, `$` na kořen dokumentu.

#### 8. **Skriptové výrazy**- Některé implementace podporují funkce jako `length`, `max` nebo `min` (nejsou součástí RFC standardu).
- Příklad: `$.store.book[?(@.author =~ /Evelyn.*/)]` vybere autory začínající na "Evelyn".

#### 9. **Unie (`[,]`)**- Vybere sjednocení více vlastností nebo indexů pole.
- Příklad: `$.store.book[0,1]` vybere první a druhou knihu.

#### 10. **Aktuální objekt (`@`)**- Uvnitř filtrů pro odkaz na aktuální položku.
- Příklad: `$.store.book[?(@.category == 'fiction')]`

#### 11. **Rozlišování velikosti písmen**- JSON Path rozlišuje velikost písmen u názvů vlastností i hodnot.

## Tahák na syntaxi JSON Path

| Operátor           | Popis                                               | Příklad                                 |
|--------------------|-----------------------------------------------------|-----------------------------------------|
| `$`                | Kořenový objekt                                     | `$.store`                               |
| `.` / `['name']`   | Přístup k podřízené vlastnosti                      | `$.user.name`, `$['user']['profile']`   |
| `[*]`              | Zástupný znak (všechny prvky)                       | `$.company.employees[*].name`           |
| `..`               | Rekurzivní sestup (všichni potomci)                 | `$..price`                              |
| `[n]`              | Přístup k indexu pole                               | `$.books[0]`                            |
| `[n,m]`            | Více indexů (unie)                                  | `$.books[0,2]`                          |
| `[start:end:step]` | Výřez pole                                          | `$.books[1:3]`                          |
| `[?()]`            | Filtrační výraz                                     | `$.books[?(@.price < 10)]`              |
| `@`                | Aktuální objekt ve filtru                           | `@.price > 20`                          |
| `*`                | Zástupný znak (všechny klíče nebo hodnoty v úrovni) | `$.store.*`                             |

## Praktické příklady

**Ukázkový JSON:**```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  },
  "expensive": 10
}
```

### Příklady dotazů

1. **Získání všech názvů knih**```jsonpath
   $.store.book[*].title
   // Výsledek: ["Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings"]
   ```

2. **Získání všech autorů beletristických knih**```jsonpath
   $.store.book[?(@.category == 'fiction')].author
   // Výsledek: ["Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"]
   ```

3. **Najít všechny knihy s cenou pod 10**```jsonpath
   $.store.book[?(@.price < 10)]
   // Výsledek: [ ... dva objekty knih ... ]
   ```

4. **Získat všechny ceny ve store (knihy i kolo)**```jsonpath
   $.store..price
   // Výsledek: [8.95, 12.99, 8.99, 22.99, 19.95]
   ```

5. **Vybrat poslední knihu v poli**```jsonpath
   $.store.book[-1]
   // Výsledek: { ... Tolkienova kniha ... }
   ```

6. **Získat názvy prvních dvou knih**```jsonpath
   $.store.book[0:2].title
   // Výsledek: ["Sayings of the Century", "Sword of Honour"]
   ```

7. **Získat všechna ISBN ve store**```jsonpath
   $.store.book[*].isbn
   // Výsledek: ["0-553-21311-3", "0-395-19395-8"]
   ```

8. **Získat všechny položky ve store (knihy a kolo) pomocí zástupného znaku**```jsonpath
   $.store.*
   // Výsledek: [pole knih, objekt kola]
   ```

9. **Rekurzivní sestup pro získání všech cen v dokumentu**```jsonpath
   $..price
   // Výsledek: [8.95, 12.99, 8.99, 22.99, 19.95, 10]
   ```

## Operátory a filtry JSON Path (pokročilé)

### Podporované operátory ([dokumentace SmartBear](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html#filters))

| Operátor | Popis                                        | Příklad                                               |
|----------|----------------------------------------------|-------------------------------------------------------|
| `==`     | Rovná se                                     | `[?(@.color=='red')]`                                 |
| `!=`     | Nerovná se                                   | `[?(@.color!='red')]`                                 |
| `>`      | Větší než                                    | `[?(@.price>10)]`                                     |
| `>=`     | Větší nebo rovno                             | `[?(@.price>=10)]`                                    |
| `<`      | Menší než                                    | `[?(@.price<10)]`                                     |
| `<=`     | Menší nebo rovno                             | `[?(@.price<=10)]`                                    |
| `=~`     | Regulární výraz (závislé na implementaci)    | `[?(@.author =~ /Evelyn.*/)]`                         |
| `&&`     | Logické AND                                  | `[?(@.category=='fiction' && @.price < 10)]`          |
| `||`     | Logické OR                                   | `[?(@.category=='fiction' || @.price < 10)]`          |
| `in`     | Hodnota je v poli                            | `[?(@.size in ['M','L'])]` (SmartBear TestEngine)     |
| `nin`    | Hodnota NENÍ v poli                          | `[?(@.size nin ['M','L'])]` (SmartBear TestEngine)    |
| `subsetof` | Pole je podmnožinou jiného pole            | `[?(@.sizes subsetof ['M','L'])]` (jen TestEngine)    |
| `contains` | Řetězec nebo pole obsahuje hodnotu         | `[?(@.name contains 'Alex')]` (jen TestEngine)        |
| `size`   | Pole nebo řetězec má konkrétní délku         | `[?(@.name size 4)]` (jen TestEngine)                 |
| `empty true/false` | Je/nebo není prázdné               | `[?(@.name empty true)]` (jen TestEngine)             |

**Poznámka:**Podpora operátorů se může lišit podle použité knihovny. Viz [RFC 9535 sekce 2.3.5](https://datatracker.ietf.org/doc/html/rfc9535#section-2.3.5) pro standardizaci.

## Jak se JSON Path používá v praxi

### 1. Automatizace a testování API

- **Validace odpovědí API**pomocí JSONPath v nástrojích jako [Postman](https://learning.postman.com/docs/writing-scripts/script-references/variables-list/), [Rest-Assured](https://toolsqa.com/rest-assured/jsonpath-and-query-json-using-jsonpath/) nebo [SoapUI](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html).
- **Příklad:**Ověření, že e-mail vráceného uživatele odpovídá očekávané hodnotě:
  ```javascript
  // Postman
  pm.expect(pm.response.json().user.email).to.eql("test@example.com");
  // S JSONPath
  const email = jsonpath.query(response, '$.user.email')[0];
  ```

### 2. Transformace dat a ETL

- Extrakce vnořených atributů z JSON logů či souborů pro analytiku pomocí knihoven jako [jsonpath-ng](https://github.com/h2non/jsonpath-ng) (Python).
  ```python
  from jsonpath_ng import parse
  errors = [match.value for match in parse('$..errors[*].message').find(log_data)]
  ```

### 3. Dotazy na databázi

- Dotazování na JSON sloupce v SQL Server nebo PostgreSQL pomocí JSONPath.
  - **SQL Server:**[JSON Path Expressions in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-path-expressions-sql-server?view=sql-server-ver17)
  - **Příklad:**```sql
    SELECT *
    FROM OPENJSON(@json, '$.store.book[?(@.price < 10)]')
    ```

### 4. AI chatboti a automatizace

- Parsování uživatelských atributů, záměrů nebo historie konverzací v JSON-formátovaných chatech.
  ```jsonpath
  $.conversation[*].user_message
  ```

### 5. Správa konfigurace

- Dynamická aktualizace nebo čtení hodnot konfigurace v JSON souborech pomocí JSONPath update metod.
  ```javascript
  jsonpath.value(config, '$.env.mode', 'production');
  ```

## Porovnání s XPath

| Vlastnost       | JSON Path           | XPath         |
|-----------------|--------------------|--------------|
| Formát dat      | JSON               | XML          |
| Syntaxe         | Cestová, `$..`     | Cestová, `//`, `/` |
| Filtry          | `[?(podmínka)]`    | `[podmínka]` |
| Rekurze         | `..`               | `//`         |
| Standardizace?  | Ano (RFC 9535)     | Ano          |
| Rodič/Sourozenec| Nepodporováno      | Podporováno  |

- JSON Path je pro JSON, XPath je pro XML.
- JSON Path neumí navigaci na rodiče/sourozence jako XPath.

## JSON Path v kódu: příklady v různých jazycích

### JavaScript (Node.js)
- [jsonpath](https://github.com/dchester/jsonpath)
```javascript
const jsonpath = require('jsonpath');
const data = require('./data.json');

// Získat všechny názvy knih
const titles = jsonpath.query(data, '$.store.book[*].title');
console.log(titles);

// Filtrovat knihy levnější než 10
const cheapBooks = jsonpath.query(data, '$.store.book[?(@.price < 10)]');
console.log(cheapBooks);
```

### Python
- [jsonpath-ng](https://github.com/h2non/jsonpath-ng)
```python
import json
from jsonpath_ng import parse

with open('data.json') as file:
    data = json.load(file)

titles = [match.value for match in parse('$.store.book[*].title').find(data)]
print(titles)
```

### Java
- [JsonPath](https://github.com/json-path/JsonPath)
```java
import com.jayway.jsonpath.JsonPath;

String json = new String(Files.readAllBytes(Paths.get("data.json")));
DocumentContext ctx = JsonPath.parse(json);

List<String> titles = ctx.read("$.store.book[*].title");
```

### PHP
- [Flow\JSONPath](https://github.com/Flow-Communications/JSONPath)
```php
use Flow\JSONPath\JSONPath;

$data = json_decode(file_get_contents('data.json'), true);

$titles = (new JSONPath($data))->find('$.store.book[*].title');
print_r($titles->data());
```

## Nejlepší postupy a tipy

- **Strict vs. Lax Mode:**Některé implementace (např. SQL Server) nabízejí strict/lax režimy pro zpracování chyb při chybějících cestách.
- **Bracket Not