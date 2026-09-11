from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2dc22be-93d6-5f6a-befc-f3ebfd906a50',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    display_name='Gible',
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=94,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=443,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
