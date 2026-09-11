from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='951cd7a4-7557-5e6c-8636-311ade4a0bc5',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    display_name='Skiddo',
    searchable_by=['Skiddo', 'Basic', 'Skiddo'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=672,
    abilities=[
        Attack(
            title='Growth',
            game_text='Attach a Grass Energy card from your hand to this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
