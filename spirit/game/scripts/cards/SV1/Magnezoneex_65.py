from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d54d109f-0eb5-5bb9-b73a-8c1b7c7c8e23',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezoneex.Name',
    display_name='Magnezone ex',
    searchable_by=['Magnezone ex', 'Stage 2', 'ex', 'Magnezoneex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=65,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    family_id=81,
    abilities=[
        Attack(
            title='Energy Crush',
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Pulse Launcher',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
