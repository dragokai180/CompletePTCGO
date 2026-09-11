from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='589cda6d-cf8f-5120-9766-0f80057d6e7e',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name',
    display_name='Hawlucha',
    searchable_by=['Hawlucha', 'Basic', 'Hawlucha'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Ability(
            title='Shining Spirit',
            game_text="Damage from this Pokémon's attacks isn't affected by Weakness or Resistance.",
            passive=standard_passive("Damage from this Pokémon's attacks isn't affected by Weakness or Resistance."),
        ),
        Attack(
            title='Flying Press',
            game_text="If your opponent's Active Pokémon isn't a Pokémon-EX, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
