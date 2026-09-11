from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e00b1ee2-6483-507e-8f86-895d40fdca18",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFireex.Name",
    display_name="Gouging Fire ex",
    searchable_by=["Gouging Fire ex", "Basic", "ex", "Ancient", "GougingFireex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=38,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=1020,
    abilities=[
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Blaze Blitz",
            game_text="This Pokémon can't use Blaze Blitz again until it leaves the Active Spot.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=standard_attack,
        ),
    ],
)
