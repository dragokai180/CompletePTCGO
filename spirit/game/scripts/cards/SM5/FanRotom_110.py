from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0fad44c1-06e9-52f1-baa3-52393f1103fc',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FanRotom.Name',
    display_name='Fan Rotom',
    searchable_by=['Fan Rotom', 'Basic', 'FanRotom'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Ability(
            title='Roto Motor',
            game_text="If you have 9 or more Pokémon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
            usable_from='discard',
        ),
        Attack(
            title='Spinning Fan',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
