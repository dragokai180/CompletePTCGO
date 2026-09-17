from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca26bb32-40ce-522d-806a-ec2e2bfd304c',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name',
    display_name='Reshiram',
    searchable_by=['Reshiram', 'Basic', 'Reshiram'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Laser Flame',
            game_text='If this Pokémon has any Lightning Energy attached, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
