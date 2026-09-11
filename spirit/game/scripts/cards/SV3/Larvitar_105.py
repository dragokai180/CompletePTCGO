from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f9d73845-66a2-56cf-91fd-c0051eeed425',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    display_name='Larvitar',
    searchable_by=['Larvitar', 'Basic', 'Larvitar'],
    subtypes=['Basic'],
    collector_number=105,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=246,
    abilities=[
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Confront',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
