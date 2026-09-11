from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb5367d3-48c2-5611-b1c9-aac2a6891150',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name',
    display_name='Charizard ex',
    searchable_by=['Charizard ex', 'Stage 2', 'ex', 'Charizardex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=6,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Brave Wing',
            game_text='If this Pokémon has any damage counters on it, this attack does 100 more damage.',
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Explosive Vortex',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 4},
            damage=330,
            effect=standard_attack,
        ),
    ],
)
