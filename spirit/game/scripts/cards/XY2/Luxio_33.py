from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d5fabdc-187c-5173-b271-97458211df89',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    display_name='Luxio',
    searchable_by=['Luxio', 'Stage 1', 'Luxio'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    family_id=403,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title='Electricounter',
            game_text='This attack does 40 damage times the number of Prize cards your opponent has taken.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
