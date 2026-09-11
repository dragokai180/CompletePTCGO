from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1834d977-16a9-5458-aaa4-cbdafeb1cd89',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name',
    display_name='Sawk',
    searchable_by=['Sawk', 'Basic', 'Sawk'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=539,
    abilities=[
        Attack(
            title='Quick Guard',
            game_text="Prevent all damage done to this Pokémon by attacks from Basic Pokémon during your opponent's next turn. This Pokémon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Brick Break',
            game_text="This attack's damage isn't affected by Resistance or any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
