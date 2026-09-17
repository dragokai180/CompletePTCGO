from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b4885a6b-1f35-55fa-8f8c-9dc40e2aeecb',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name',
    display_name='Tropius',
    searchable_by=['Tropius', 'Basic', 'Tropius'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=357,
    abilities=[
        Attack(
            title='Rally Back',
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Cutting Wind',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
