from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f9f4a954-43d9-5973-90a2-815fd7ea6766',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aegislashex.Name',
    display_name='Aegislash ex',
    searchable_by=['Aegislash ex', 'Stage 2', 'ex', 'Aegislashex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=135,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Peerless Edge',
            game_text='This attack does 70 damage for each Prize card you have taken.',
            cost={PokemonTypes.METAL: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edged Slash',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.METAL: 2},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
