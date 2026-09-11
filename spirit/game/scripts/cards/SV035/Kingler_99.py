from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df1bea7a-46c3-5bd6-95b3-cad6af80d5bf',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name',
    display_name='Kingler',
    searchable_by=['Kingler', 'Stage 1', 'Kingler'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name',
    family_id=98,
    abilities=[
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 3},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Guillotine',
            cost={PokemonTypes.WATER: 4},
            damage=220,
        ),
    ],
)
