from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04d2bdf3-d089-51b9-9e88-6477bd189b19',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    display_name='Charmander',
    searchable_by=['Charmander', 'Basic', 'Charmander'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=4,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Reprisal',
            game_text='This attack does 20 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
