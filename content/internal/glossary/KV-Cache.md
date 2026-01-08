+++
title = "KV Cache"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "kv-cache"
description = "KV Cache je optimalizace pro inference u Transformer modelů a LLM, ukládající Key a Value tenzory pro dramatické zrychlení autoregresivní generace tokenů a snížení výpočetních nákladů."
keywords = ["KV Cache", "LLMs", "Transformer modely", "inference optimalizace", "generování tokenů"]
category = "AI Infrastruktura & Nasazení"
type = "glossary"
draft = false
url = "/internal/glossary/KV-Cache/"

+++
## Co je KV Cache?

**KV Cache**(Key-Value Cache) je optimalizace pro inference u transformer modelů, zejména *velkých jazykových modelů* (LLMs), která ukládá key (K) a value (V) tenzory vypočtené během attention pro všechny dříve zpracované tokeny. Místo opakovaného výpočtu těchto tenzorů pro každý token při každém kroku inference model znovu použije hodnoty z cache a vypočítá pouze K a V pro nový token. Tento přístup je základem efektivní, rychlé autoregresivní generace textu.

**Stručně:**> KV Cache je pomocná paměť uchovávající mezivýsledky key a value tenzorů z předchozích tokenů, takže při generování nových tokenů stačí vypočítat a přidat pouze K a V pro nový token. Všechny předchozí K/V jsou okamžitě dostupné z cache.

### Autoritativní zdroje:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Sebastian Raschka: Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## Jak se KV Cache používá?

KV Cache se používá výhradně při inference v transformerových modelech pro generování textu po jednotlivých tokenech.

### Základní vzor použití:
- **Autoregresivní generování:**LLM generují text po jednom tokenu, přičemž každý predikovaný token závisí na všech předchozích tokenech.
- **Při každém kroku inference:**Model potřebuje K a V pro celou dosavadní sekvenci, aby vypočítal attention pro další token.
- **S KV Cache:**Namísto opakovaného výpočtu K a V pro všechny předchozí tokeny při každém kroku se vypočítá a přidá do cache pouze K a V pro nový token.
- **Výsledek:**Dramaticky nižší výpočty, nižší [latence](/en/glossary/latency/) a výrazné úspory nákladů při inference – zejména u dlouhých sekvencí.

### Typické kontexty použití:
- Generování textu pomocí LLM (např. GPT, Llama, Claude, Gemini)
- Chatboti a konverzační agenti
- Doplňování kódu a asistenti pro programování
- Reálné i dávkové inference nasazení

#### Další čtení:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Transformers Documentation: Generation Strategies - KV Caching](https://huggingface.co/docs/transformers/main/en/generation_strategies#kv-caching)

## Proč je KV Cache důležitá u velkých jazykových modelů (LLMs)?

### Problém bez KV Cache

Attention mechanismus v transformeru zahrnuje tři projekce na token:
- **Query (Q):**Co aktuální token „chce vědět“.
- **Key (K):**„Adresa“ každého tokenu.
- **Value (V):**„Obsah“ každého tokenu.

Při inference zpracovávají LLM vstup po jednom tokenu. Standardní inference opakovaně počítá K a V pro každý token v aktuální sekvenci, včetně těch, které už byly zpracovány. To je u dlouhých sekvencí velmi neefektivní.

#### Příklad neefektivity:
Představte si generování „The cat sits“:
- Generování „The“: výpočet K/V pro „The“.
- Generování „The cat“: opět výpočet K/V pro „The“ a „cat“.
- Generování „The cat sits“: opět výpočet K/V pro všechny tři tokeny.

#### S KV Cache:
- Pro „The“ vypočítáme K/V jednou a uložíme.
- Pro „cat“ vypočítáme K/V jen pro „cat“ a přidáme do cache.
- Pro „sits“ vypočítáme K/V jen pro „sits“ a přidáme do cache; K/V pro „The“ a „cat“ se znovu využijí.

**Optimalizace je klíčová pro:**- **Rychlost:**Zrychlení inference až 5–20×.
- **Náklady:**Výrazné snížení výpočetních a API nákladů.
- **Škálovatelnost:**Umožňuje dlouhý kontext i víceotáčkové konverzace.

##### Další autority:
- [Neptune: Transformers Key-Value Caching Explained](https://neptune.ai/blog/transformers-key-value-caching)
- [Hugging Face Blog: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)

## Detailní příklad: Jak KV Cache funguje

### Generování tokenů krok za krokem

#### Bez KV Cache:
Pro prompt: `["The", "cat", "sits"]`
- Každý krok znovu počítá K a V pro všechny tokeny v sekvenci.

**Diagram:**```
Krok 1: "The"           --> K1, V1    (vypočteno)
Krok 2: "The cat"       --> K1, V1, K2, V2  (K1, V1 znovu)
Krok 3: "The cat sits"  --> K1, V1, K2, V2, K3, V3 (K1, V1, K2, V2 znovu)
```

#### S KV Cache:
- Každý krok vypočítá/přidá K/V jen pro nový token; cache drží předchozí K/V.

**Diagram:**```
Krok 1: "The"      --> K1, V1    (uloženo do cache)
Krok 2: "cat"      --> K2, V2    (přidáno do cache)
Krok 3: "sits"     --> K3, V3    (přidáno do cache)
```
**Cache po kroku 3:**```
K-cache: [K1, K2, K3]
V-cache: [V1, V2, V3]
```

##### Vizuální ilustrace:
![KV Cache Illustration](https://cdn-uploads.huggingface.co/production/uploads/6527e89a8808d80ccff88b7a/ZiRajz9XfXiPT3NIM05FS.png)
[Zdroj: Hugging Face Blog](https://huggingface.co/blog/not-lain/kv-caching#how-does-kv-caching-work)

## Technické detaily: Implementace KV Cache

### Matematická formulace

Pro sekvenci n vstupních tokenů transformerová vrstva počítá:
\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right)V
\]

- **Při tréninku:**Všechny Q, K, V tokenů se počítají paralelně.
- **Při inference s KV cache:**Počítají se jen Q, K, V pro nový token; předchozí K a V se načítají z cache.

### Příklad KV Cache v PyTorch

```python
class KVCache:
    def __init__(self):
        self.cache = {"key": None, "value": None}

    def update(self, key, value):
        if self.cache["key"] is None:
            self.cache["key"] = key
            self.cache["value"] = value
        else:
            self.cache["key"] = torch.cat([self.cache["key"], key], dim=1)
            self.cache["value"] = torch.cat([self.cache["value"], value], dim=1)

    def get_cache(self):
        return self.cache
```

### Použití v Hugging Face Transformers

Většina moderních knihoven zajišťuje KV cache automaticky.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')

tokens = tokenizer.encode("The cat sits", return_tensors="pt")
output = model.generate(tokens, max_new_tokens=10, use_cache=True)
print(tokenizer.decode(output[0]))
```
- Parametr `use_cache` povoluje KV caching (výchozí: `True`).

#### Další kód & vysvětlení:
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- [Hugging Face Blog: Practical Implementation](https://huggingface.co/blog/not-lain/kv-caching#practical-implementation)

## Výkon: rychlost, paměť a nákladová efektivita

### Kvantitativní dopad

| Funkce                | Standardní inference                | KV caching                          |
|-----------------------|-------------------------------------|-------------------------------------|
| Výpočty na slovo      | Opakované výpočty                   | Znovupoužití uložených hodnot       |
| Využití paměti        | Menší na krok, roste s textem       | Navíc pro cache, ale efektivní      |
| Rychlost              | Pomalejší s delším textem           | Stále rychlá i u dlouhých textů     |
| Náklady               | Vysoký výpočet, vyšší latence       | Nižší výpočet, snížená latence      |

#### Benchmarky:
- Na GPU T4 (SmolLM2-1.7B):
    - Standardní inference (bez KV cache): **61 sekund**- S KV cache: **11,7 sekundy**- **~5,2× zrychlení**- Mnoho API poskytovatelů (např. Anthropic, OpenAI) účtuje méně za cacheované tokeny. Ty mohou být až 10× levnější (např. $0,30 za milion vs $3 za milion).

##### Zdroj:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching#comparison-kv-caching-vs-standard-inference)
- [Sebastian Raschka: KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## Osvědčené postupy pro maximální efektivitu KV Cache

### Prompt engineering & správa kontextu

- **Stabilní prefix promptu:**Prefixy promptu musí být mezi tahy identické. Jakákoli změna (i jeden token) přeruší cache od tohoto bodu dál.
- **Pouze přidávání kontextu:**Vždy pouze přidávejte nové informace; nikdy nepřepisujte nebo nepřeuspořádávejte předchozí kontext.
- **Deterministické pořadí:**Strukturovaná data musí mít konzistentní pořadí, aby nedošlo k nechtěné invalidaci cache.
- **Explicitní body přerušení cache:**U víceotáčkových agentů označte místa změny kontextu, aby frameworky udržely efektivitu.

### Správa cache v produkci

- **Velikost cache:**K/V tenzory rostou lineárně s délkou kontextu. U velmi dlouhých sekvencí může být limitem paměť.
- **Životnost cache:**Invalidační/vypršení cache při změně kontextu nebo nutnosti uvolnit paměť.
- **Paralelnost:**Každý paralelní požadavek může potřebovat vlastní prostor pro cache.

**Tip:**> Pro maximální efektivitu cache udržujte prefix promptu stabilní a kontext pouze přidávejte. Vyhněte se dynamickému kontextu, který mění staré položky.

##### Další čtení:
- [Hugging Face: How Does KV Caching Work?](https://huggingface.co/blog/not-lain/kv-caching#how-does-kv-caching-work)

## Pokročilé techniky KV Cache

### Paged Attention
- Dělí kontext na „stránky“ (chunky).
- V rychlé paměti jsou jen relevantní stránky; staré se odkládají nebo znovu počítají dle potřeby.
- Umožňuje zpracovat velmi dlouhé kontexty (desítky tisíc tokenů) bez vyčerpání GPU paměti.

### Radix Attention
- Ukládá tokeny v cache do radix stromu.
- Logaritmické škálování: attention na skupiny tokenů hierarchicky.

### Multi-Query Attention
- Snižuje paměť pro KV cache sdílením key/value napříč attention heady.

#### Nové trendy
- **Prediktivní zahřívání cache:**Předvyplnění cache podle očekávaných potřeb.
- **Hierarchické cache:**Víceúrovňové strategie (GPU, CPU, disk).
- **Dynamická velikost cache:**Úprava velikosti cache v reálném čase.

##### Více:
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## Použití a aplikace v praxi

### Chatboti a konverzační agenti
- Víceotáčkové konverzace opakovaně využívají prefixy promptů.
- KV cache snižuje TTFT (time-to-first-token) i celkovou latenci.

### Generování a doplňování kódu
- Asistenti pro kódování (např. Copilot) využívají KV cache pro okamžité doplňování.

### Automatizace zákaznické podpory
- Kontextové historie chatů jsou efektivně spravovány pro rychlé odpovědi.

### Generování dokumentů a obsahu
- Tvorba dlouhých textů těží z cacheování promptů, což umožňuje efektivní editaci a iterativní práci.

### Hry a interaktivní storytelling
- Herní dialogové enginy cacheují kontext příběhu pro plynulé, rychlé reakce hráče.

**Case study:**API Claude od Anthropic účtuje 10× méně za cacheované tokeny. Udržení stabilního prefixu v chatbotech zákaznické podpory snižuje provozní náklady a zvyšuje rychlost odezvy.

## Omezení a výzvy

- **Růst paměti:**K/V cache roste lineárně s kontextem. Velmi dlouhé kontexty mohou vyčerpat GPU paměť.
- **Invalidace cache:**Jakákoli změna předchozích tokenů (editace promptu, změna kontextu) invaliduje část/celou cache.
- **Složitá správa:**Multi-user/multi-turn systémy vyžadují pečlivou správu cache.
- **Nepoužívá se při trénování:**KV cache je optimalizace pouze pro inference.

##### Autority:
- [Hugging Face: Standard Inference and the Rise of KV Caching](https://huggingface.co/blog/not-lain/kv-caching#standard-inference-and-the-rise-of-kv-caching)
- [Sebastian Raschka: KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)


## Reference & další čtení

- [Hugging Face Blog: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Neptune: Transformers Key-Value Caching Explained](https://neptune.ai/blog/transformers-key-value-caching)
- [Sebastian Raschka: Understanding and Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- [Data Science Dojo: Unlocking the Power of KV Cache](https://datasciencedojo.com/blog/kv-cache-how-to-speed-up-llm-inference/)
- [Kapil Sharma: KV Caching Illustrated](https://kapilsh.github.io/posts/kv-caching-visualized/)
- [Akira AI: KV Caches and Time-to-First-Token](https://www.akira.ai/blog/kv-caches-and-time-to-first-token)
- [Andrew Szot: KV Cache](https://www.andrewszot.com/posts/kv_cache/)
- [Transformers Documentation: Generation Strategies - KV Caching](https://huggingface.co/docs/transformers/main/en/generation_strategies#kv-caching)
- [Joaolages: KV Caching Explained](https://medium.com/@joaolages/kv-caching-explained-276520203249)

## Další průzkum

Pro více informací o vnitřnostech transformerů, prompt engineeringu a optimalizaci LLM viz reference výše a prozkoumejte další zdroje o pokročilých attention mechanismech a správě kontextu.

*Každá implementace či návrhové rozhodnutí kolem KV cache by měla vycházet z nejnovějších produkčních technik LLM a autoritativních zdrojů uvedených výše. Pro nejhlubší technické detaily – včetně diagramů, PyTorch kódu a okrajových případů – studujte:*

- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)