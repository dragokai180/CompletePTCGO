from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd997e15-a4d3-5f44-8323-5b4a8c6f4223',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name',
    display_name='Pawmo',
    searchable_by=['Pawmo', 'Stage 1', 'Pawmo'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    family_id=921,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title='Electrobullet',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
