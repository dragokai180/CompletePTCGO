from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cff5a514-dcb0-5f0d-a33b-9689f8281c8c',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name',
    display_name='Kyogre',
    searchable_by=['Kyogre', 'Basic', 'Kyogre'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title='Hydro Pump',
            game_text='This attack does 30 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
