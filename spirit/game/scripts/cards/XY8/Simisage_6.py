from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0825d732-7ca9-51a1-8fdb-797fecb108e6',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name',
    display_name='Simisage',
    searchable_by=['Simisage', 'Stage 1', 'Simisage'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name',
    family_id=511,
    abilities=[
        Attack(
            title='Fire Fling',
            game_text='Put 3 Fire Energy cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hand Fling',
            game_text='This attack does 10 damage times the number of cards in your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
