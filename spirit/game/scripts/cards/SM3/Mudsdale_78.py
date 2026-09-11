from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e8d9d8e-3c80-518c-941e-f1fc0b171043',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name',
    display_name='Mudsdale',
    searchable_by=['Mudsdale', 'Stage 1', 'Mudsdale'],
    subtypes=['Stage 1'],
    collector_number=78,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name',
    family_id=749,
    abilities=[
        Attack(
            title='Kick Away',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Vigorous Dash',
            game_text="This Pokémon does 30 damage to itself. This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
