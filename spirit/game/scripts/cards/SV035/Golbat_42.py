from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc38b5bc-4bc7-54e5-9080-089340ba83ef',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    display_name='Golbat',
    searchable_by=['Golbat', 'Stage 1', 'Golbat'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Skill Dive',
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
