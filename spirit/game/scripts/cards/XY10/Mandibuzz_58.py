from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb965dbe-39e1-522e-b9fc-b2ff67b6863d',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name',
    display_name='Mandibuzz',
    searchable_by=['Mandibuzz', 'Stage 1', 'Mandibuzz'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name',
    family_id=629,
    abilities=[
        Attack(
            title='Bone Drop',
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon that has an Ability. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cutting Wind',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
