from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='658bbf04-c56e-53d8-b856-5d467c9849ce',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name',
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Flame Tail',
            cost={PokemonTypes.FIRE: 1},
            damage=60,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
