from spirit.game.data_utils import Attack, PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import g_booster, genesect_ex_only

card = PokemonToolCardDef(
    guid="9f942b95-906b-59dc-8b63-2af80c264569", key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GBooster.Name",
    display_name="G Booster", searchable_by=["G Booster", "Pokémon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pokémon Tool", "ACE SPEC", "Team Plasma"], collector_number=92,
    set_code="BW10", rarity=Rarities.Ace,
    granted_abilities=[Attack(
        title="G Booster",
        game_text="Discard 2 Energy attached to this Pokémon. This attack's damage isn't affected by any effects on the Defending Pokémon.",
        cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=200,
        condition=genesect_ex_only, effect=g_booster,
    )],
)
