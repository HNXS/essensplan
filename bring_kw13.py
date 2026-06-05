#!/usr/bin/env python3
"""Add KW13 (21-27 March 2026) shopping items to Bring! list."""

import asyncio
import aiohttp
from bring_api import Bring

EMAIL = "tim.schellschmidt@googlemail.com"
PASSWORD = "cutmaJ-retmej-9paqwy"
LIST_UUID = "4e7ff9d4-4bf7-45fb-bc13-7bfe51b5b89d"

# Consolidated shopping list - (item_name, specification)
ITEMS = [
    # Fisch
    ("Lachsfilet", "400g"),
    # Gemüse & Obst
    ("Brokkoli", "1 Kopf"),
    ("Lauch", "2 Stangen"),
    ("Kartoffeln", "1kg festkochend"),
    ("Paprika", "2 Stück (rot + gelb)"),
    ("Zucchini", "2 Stück"),
    ("Aubergine", "1 Stück"),
    ("Champignons", "250g"),
    ("Kirschtomaten", "1 Packung"),
    ("Zwiebeln", "3 Stück"),
    ("Knoblauch", "1 Knolle"),
    ("Frühlingszwiebeln", "1 Bund"),
    ("Blattspinat TK", "500g"),
    ("Bananen", ""),
    ("Beeren", "frisch oder TK"),
    ("Basilikum", "frisch, 1 Topf"),
    ("Zitronen", "2 Stück"),
    ("Gurke", "1 Stück (Frühstück)"),
    # Milch/Eier
    ("Eier", "12 Stück"),
    ("Milch", "1 Liter"),
    ("Sahne", "200ml"),
    ("Schmand", "200g"),
    ("Feta", "200g"),
    ("Ricotta", "250g"),
    ("Mozzarella", "200g"),
    ("Joghurt natur", "500g"),
    ("Butter", ""),
    ("Parmesan", ""),
    ("Frischkäse", ""),
    ("Granola", ""),
    # Brot/Backwaren
    ("Baguette", "1 Stück"),
    ("Flammkuchen-Böden", "3 Stück"),
    ("Toastbrot", "oder Brioche (French Toast)"),
    # Nudeln/Reis
    ("Spaghetti", "500g"),
    ("Tagliatelle", "500g (oder Penne)"),
    ("Couscous", "1 Packung"),
    ("Basmatireis", ""),
    ("Lasagneplatten", "1 Packung"),
    # Dosen
    ("Passierte Tomaten", "500ml"),
    ("Stückige Tomaten", "1 Dose"),
    ("Kichererbsen", "1 Dose (optional, für Hummus)"),
    # Vorrat
    ("Haferflocken", ""),
    ("Mehl", ""),
    ("Ahornsirup", ""),
    ("Honig", ""),
    ("Sojasauce", ""),
    ("Olivenöl", ""),
    ("Gemüsebrühe", ""),
    ("Hummus", "1 Glas"),
]


async def main():
    async with aiohttp.ClientSession() as session:
        bring = Bring(session, EMAIL, PASSWORD)
        await bring.login()
        print(f"✅ Logged in as {EMAIL}")
        
        # Get lists to verify
        lists = await bring.load_lists()
        target_list = None
        for lst in lists.lists:
            if lst.listUuid == LIST_UUID:
                target_list = lst
                break
        
        if not target_list:
            print(f"❌ List {LIST_UUID} not found!")
            return
        
        print(f"📋 Found list: {target_list.name}")
        
        # Add items
        added = 0
        for item_name, spec in ITEMS:
            try:
                await bring.save_item(LIST_UUID, item_name, spec)
                added += 1
                print(f"  ✅ {item_name} ({spec})" if spec else f"  ✅ {item_name}")
            except Exception as e:
                print(f"  ❌ {item_name}: {e}")
        
        print(f"\n🛒 {added}/{len(ITEMS)} items added to '{target_list.name}'!")


if __name__ == "__main__":
    asyncio.run(main())
