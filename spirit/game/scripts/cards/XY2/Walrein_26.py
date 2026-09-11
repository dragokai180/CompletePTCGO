from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea548117-c5e1-54d4-96e1-280fe1b8c87f',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name',
    display_name='Walrein',
    searchable_by=['Walrein', 'Stage 2', 'Walrein'],
    subtypes=['Stage 2'],
    collector_number=26,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name',
    family_id=363,
    abilities=[
        Attack(
            title='Powder Snow',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Big Tusk',
            game_text='This attack does 120 damage minus 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
