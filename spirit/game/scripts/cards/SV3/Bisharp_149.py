from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ccddb47-58c7-5315-bc30-5ca99a9e18bb',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    display_name='Bisharp',
    searchable_by=['Bisharp', 'Stage 1', 'Bisharp'],
    subtypes=['Stage 1'],
    collector_number=149,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    family_id=624,
    abilities=[
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title='Fury Cutter',
            game_text='Flip 3 coins. If 1 of them is heads, this attack does 20 more damage. If 2 of them are heads, this attack does 60 more damage. If all of them are heads, this attack does 120 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
