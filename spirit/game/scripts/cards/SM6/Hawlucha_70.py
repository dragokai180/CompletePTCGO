from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='081037d2-91b4-5ff8-9219-5ac667e6b939',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name',
    display_name='Hawlucha',
    searchable_by=['Hawlucha', 'Basic', 'Hawlucha'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Attack(
            title='High Jump Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='Sky Drop',
            game_text="This attack does 20 less damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
