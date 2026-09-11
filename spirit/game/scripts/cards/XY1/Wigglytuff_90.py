from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='902081cd-dc24-54a0-a8bd-657118e41f64',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name',
    display_name='Wigglytuff',
    searchable_by=['Wigglytuff', 'Stage 1', 'Wigglytuff'],
    subtypes=['Stage 1'],
    collector_number=90,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    family_id=39,
    abilities=[
        Attack(
            title='Balloon Barrage',
            game_text='This attack does 20 damage times the amount of Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
