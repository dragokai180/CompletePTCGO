from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33014c67-8b4b-5d3f-9293-d759b7543095',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    display_name='Alolan Grimer',
    searchable_by=['Alolan Grimer', 'Basic', 'AlolanGrimer'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=88,
    abilities=[
        Attack(
            title='Chemical Breath',
            game_text="This attack does 50 more damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
