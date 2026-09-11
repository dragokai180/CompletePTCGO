from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='382c1054-c839-5fd1-afc1-6f04f5714e2e',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name',
    display_name='Furfrou',
    searchable_by=['Furfrou', 'Basic', 'Furfrou'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=676,
    abilities=[
        Attack(
            title='Return',
            game_text='You may draw cards until you have 5 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
