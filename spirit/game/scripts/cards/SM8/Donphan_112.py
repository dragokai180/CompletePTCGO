from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2aa0a45d-6b7c-5abb-9620-45942ca3c19e',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name',
    display_name='Donphan',
    searchable_by=['Donphan', 'Stage 1', 'Donphan'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    family_id=231,
    abilities=[
        Ability(
            title='Sturdy',
            game_text='If this Pokémon has full HP and would be Knocked Out by damage from an attack, this Pokémon is not Knocked Out, and its remaining HP becomes 10.',
            passive=standard_passive('If this Pokémon has full HP and would be Knocked Out by damage from an attack, this Pokémon is not Knocked Out, and its remaining HP becomes 10.'),
        ),
        Attack(
            title='Rolling Spin',
            game_text="During your next turn, this Pokémon's Rolling Spin attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
