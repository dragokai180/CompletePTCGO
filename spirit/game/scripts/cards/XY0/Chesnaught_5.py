from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec9ecc4b-8509-5770-ac48-14790cd78696',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name',
    display_name='Chesnaught',
    searchable_by=['Chesnaught', 'Stage 2', 'Chesnaught'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name',
    family_id=650,
    abilities=[
        Attack(
            title='Needle Arm',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Tumbling Attack',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
