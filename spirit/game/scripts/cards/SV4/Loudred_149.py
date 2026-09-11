from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4ca0967-f194-53a5-96c6-5c0f2fd5a87c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    display_name='Loudred',
    searchable_by=['Loudred', 'Stage 1', 'Loudred'],
    subtypes=['Stage 1'],
    collector_number=149,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Body Slam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Mega Impact',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
