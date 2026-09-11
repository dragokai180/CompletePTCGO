from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9036af98-68bc-5642-9568-0be7829b05cc',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    display_name='Bunnelby',
    searchable_by=['Bunnelby', 'Basic', 'Bunnelby'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=659,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
