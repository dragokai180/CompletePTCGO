from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='982095b1-a0ad-5320-b161-997441223598',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name',
    display_name='Floatzel',
    searchable_by=['Floatzel', 'Stage 1', 'Floatzel'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    family_id=418,
    abilities=[
        Attack(
            title='Rescue',
            game_text='Shuffle 3 Pokémon from your discard pile into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Screw Tail',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
