from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc1787a4-d738-5e24-9953-a62f328e4d49',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    display_name='Vigoroth',
    searchable_by=['Vigoroth', 'Stage 1', 'Vigoroth'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    family_id=287,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Reckless Charge',
            game_text='Flip a coin. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
