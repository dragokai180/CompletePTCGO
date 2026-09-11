from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f24a1753-8ab7-5141-8f99-0346c941d334',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name',
    display_name='Gogoat',
    searchable_by=['Gogoat', 'Stage 1', 'Gogoat'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    family_id=672,
    abilities=[
        Attack(
            title='Milk Drink',
            game_text='Flip 2 coins. For each heads, heal 40 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
