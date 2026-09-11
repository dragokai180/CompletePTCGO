from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a47c5352-2e3f-533d-ab48-7e519eeb0dea',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    display_name='Growlithe',
    searchable_by=['Growlithe', 'Basic', 'Growlithe'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=58,
    abilities=[
        Attack(
            title='Take Down',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
