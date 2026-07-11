from validator import valid
from shortener import generate
from storage import save, all_links
from sample_links import LINKS

print("=" * 35)
print("LOCAL URL SHORTENER")
print("=" * 35)

for url in LINKS:

    if valid(url):

        alias = generate(url)

        save(alias, url)

for alias, url in all_links().items():

    print(url)
    print("→", alias)
    print()

print(f"Stored URLs: {len(all_links())}")
