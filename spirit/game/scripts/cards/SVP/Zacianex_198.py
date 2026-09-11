from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="29c58481-ed25-5cb7-94b2-5448e9c115d4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacianex.Name",
    display_name="Zacian ex",
    searchable_by=["Zacian ex", "Basic", "ex", "Zacianex"],
    subtypes=["Basic", "ex"],
    collector_number=198,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title="Steel Armament",
            game_text="Search your deck for a Basic Metal Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pokémon can't use Slashing Strike.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
