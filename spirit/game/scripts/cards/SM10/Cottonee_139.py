from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1eebbdd-b9a5-5c0a-8d76-21049a51cecf',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    display_name='Cottonee',
    searchable_by=['Cottonee', 'Basic', 'Cottonee'],
    subtypes=['Basic'],
    collector_number=139,
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
    family_id=546,
    abilities=[
        Attack(
            title='Expand',
            game_text="During your opponent's next turn, this Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
