from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='458cea29-944e-5397-962e-fc4a6610ec9e',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name',
    display_name='Floatzel',
    searchable_by=['Floatzel', 'Stage 1', 'Floatzel'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    family_id=418,
    abilities=[
        Attack(
            title='Swirling Tail',
            game_text="Flip a coin. If heads, put your opponent's Active Pokémon and all attached cards into your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
