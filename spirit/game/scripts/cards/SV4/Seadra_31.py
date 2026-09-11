from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c23e919d-b8a3-57f4-bee4-fba6c2f9a04e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    display_name='Seadra',
    searchable_by=['Seadra', 'Stage 1', 'Seadra'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Bubble Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
