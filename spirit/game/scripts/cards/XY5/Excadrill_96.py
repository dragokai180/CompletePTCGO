from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d82d717f-45ff-56af-8d91-97ee8eea2886',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name',
    display_name='Excadrill',
    searchable_by=['Excadrill', 'Stage 1', 'Excadrill'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    family_id=529,
    abilities=[
        Attack(
            title='Drill Run',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Straight Claw',
            game_text='You may discard an Energy attached to this Pokémon. If you do, this attack does 30 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
