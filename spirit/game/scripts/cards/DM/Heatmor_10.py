from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='264cac51-6e4c-5770-b9b2-7918d1cb997f',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name',
    display_name='Heatmor',
    searchable_by=['Heatmor', 'Basic', 'Heatmor'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=631,
    abilities=[
        Attack(
            title='Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Charring Breath',
            game_text="If your opponent's Active Pokémon isn't Burned, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
