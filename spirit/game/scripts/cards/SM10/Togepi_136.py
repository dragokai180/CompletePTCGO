from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e61285ee-b0fb-5fcb-b573-c5c631c4f457',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name',
    display_name='Togepi',
    searchable_by=['Togepi', 'Basic', 'Togepi'],
    subtypes=['Basic'],
    collector_number=136,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=175,
    abilities=[
        Attack(
            title='Daunt',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
