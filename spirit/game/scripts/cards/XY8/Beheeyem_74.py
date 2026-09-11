from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79c69323-1630-550c-b0e1-147551a0eb1c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name',
    display_name='Beheeyem',
    searchable_by=['Beheeyem', 'Stage 1', 'Beheeyem'],
    subtypes=['Stage 1'],
    collector_number=74,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name',
    family_id=605,
    abilities=[
        Attack(
            title='Mind Bullet',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon times the amount of Energy attached to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
