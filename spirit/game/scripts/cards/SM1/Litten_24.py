from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='240912ab-6965-58ec-9670-f88bb3340476',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    display_name='Litten',
    searchable_by=['Litten', 'Basic', 'Litten'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=725,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
