from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82c71c13-dd70-5e6b-bbca-a0a2d70abd4a',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    display_name='Greninja',
    searchable_by=['Greninja', 'Stage 2', 'Greninja'],
    subtypes=['Stage 2'],
    collector_number=9,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=658,
    abilities=[
        Ability(
            title='Evasion Jutsu',
            game_text='If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Furious Shurikens',
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2},
            effect=standard_attack,
        ),
    ],
)
