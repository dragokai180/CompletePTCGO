from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be1534dd-f2ff-5a0b-8038-01a308349534',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name',
    display_name='Galvantula',
    searchable_by=['Galvantula', 'Stage 1', 'Galvantula'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    family_id=595,
    abilities=[
        Attack(
            title='Electrobullet',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
