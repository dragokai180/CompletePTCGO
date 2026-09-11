from spirit.game.data_utils import Attack, PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import g_scope, genesect_ex_only

card = PokemonToolCardDef(
    guid="32390efa-0cf4-5f8d-9e91-ddc3cd5d0b81", key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GScope.Name",
    display_name="G Scope", searchable_by=["G Scope", "Pokémon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pokémon Tool", "ACE SPEC", "Team Plasma"], collector_number=93,
    set_code="BW10", rarity=Rarities.Ace,
    granted_abilities=[Attack(
        title="G Scope",
        game_text="This attack does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
        cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
        condition=genesect_ex_only, effect=g_scope,
    )],
)
