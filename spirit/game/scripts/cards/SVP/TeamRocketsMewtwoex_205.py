from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="63979ca7-f5b1-50d1-b891-770904449f58",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMewtwoex.Name",
    display_name="Team Rocket's Mewtwo ex",
    searchable_by=["Team Rocket's Mewtwo ex", "Basic", "ex", "TeamRocketsMewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=205,
    set_code="SVP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="This Pokémon can't attack unless you have 4 or more Team Rocket's Pokémon in play.",
            passive=standard_passive("This Pokémon can't attack unless you have 4 or more Team Rocket's Pokémon in play."),
        ),
        Attack(
            title="Erasure Ball",
            game_text="You may discard up to 2 Energy from your Benched Pokémon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
