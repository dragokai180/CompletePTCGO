from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61274a62-2f5d-50c6-9fe9-68bbdc015626',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    display_name='Porygon',
    searchable_by=['Porygon', 'Basic', 'Porygon'],
    subtypes=['Basic'],
    collector_number=154,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=137,
    abilities=[
        Attack(
            title='Digicharge',
            game_text='Flip 3 coins. For each heads, search your deck for an Energy card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Point',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
