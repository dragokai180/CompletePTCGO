from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='185f7e9f-1135-5a0b-ab51-3e579fc65e75',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name',
    display_name='Braviary',
    searchable_by=['Braviary', 'Stage 1', 'Braviary'],
    subtypes=['Stage 1'],
    collector_number=93,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name',
    family_id=627,
    abilities=[
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 50 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Sky Drop',
            game_text="This attack does 120 damage minus 20 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
