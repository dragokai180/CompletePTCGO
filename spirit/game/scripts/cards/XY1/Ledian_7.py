from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c55f2a37-d381-51a8-854e-db9dca99dbd7',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name',
    display_name='Ledian',
    searchable_by=['Ledian', 'Stage 1', 'Ledian'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name',
    family_id=165,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Mach Punch',
            game_text="This attack does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
