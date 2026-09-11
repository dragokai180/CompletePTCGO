from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e83e9074-3969-52c3-add2-f3aa06ea8f44',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pheromosa.Name',
    display_name='Pheromosa',
    searchable_by=['Pheromosa', 'Basic', 'Ultra Beast', 'Pheromosa'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=115,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=795,
    abilities=[
        Attack(
            title='High Jump Kick',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='White Ray',
            game_text='If you have only 1 Prize card remaining, this attack does 90 more damage.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
