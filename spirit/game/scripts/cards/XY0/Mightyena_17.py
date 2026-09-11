from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d2ee75f-e961-560d-acbd-b8a7121df9e1',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name',
    display_name='Mightyena',
    searchable_by=['Mightyena', 'Stage 1', 'Mightyena'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name',
    family_id=261,
    abilities=[
        Attack(
            title='Hard Bite',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
