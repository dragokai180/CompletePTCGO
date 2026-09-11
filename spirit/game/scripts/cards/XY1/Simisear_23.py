from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b0ac1cc1-0fb6-5587-8d53-a62279d29d92',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name',
    display_name='Simisear',
    searchable_by=['Simisear', 'Stage 1', 'Simisear'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name',
    family_id=513,
    abilities=[
        Attack(
            title='Yawn',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
