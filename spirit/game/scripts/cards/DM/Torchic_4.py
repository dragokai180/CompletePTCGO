from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4627ff9-8564-5a90-8596-dbb09e555c57',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    display_name='Torchic',
    searchable_by=['Torchic', 'Basic', 'Torchic'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=255,
    abilities=[
        Attack(
            title='Singe',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
