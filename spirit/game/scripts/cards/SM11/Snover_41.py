from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8b30d9a-da3f-5a2b-b159-1510594878fe',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    display_name='Snover',
    searchable_by=['Snover', 'Basic', 'Snover'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=459,
    abilities=[
        Attack(
            title='Powder Snow',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
