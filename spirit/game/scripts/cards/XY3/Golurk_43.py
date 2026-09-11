from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db4ee41e-c8d1-5812-ab7f-30a295270375',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name',
    display_name='Golurk',
    searchable_by=['Golurk', 'Stage 1', 'Golurk'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name',
    family_id=622,
    abilities=[
        Attack(
            title='Wreck',
            game_text='If there is any Stadium card in play, this attack does 60 more damage. Discard that Stadium card.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Golurk Hammer',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
