from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed654e17-1d29-5b41-8aed-d092d64a7041',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    display_name='Jangmo-o',
    searchable_by=['Jangmo-o', 'Basic', 'Jangmoo'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=782,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
