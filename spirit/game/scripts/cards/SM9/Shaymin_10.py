from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4145e449-1c98-5342-9b5d-83cacf6fb872',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    display_name='Shaymin ◇',
    searchable_by=['Shaymin ◇', 'Basic', 'Prism Star', 'Shaymin'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=10,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=492,
    abilities=[
        Attack(
            title='Flower Storm',
            game_text='This attack does 30 damage times the amount of basic Energy attached to all of your Pokémon.',
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
