from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8ebe1aa-095b-5a13-9d34-8f358edd5465',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name',
    display_name='Zeraora',
    searchable_by=['Zeraora', 'Basic', 'Zeraora'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=807,
    abilities=[
        Attack(
            title='Rapid Draw',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Electrobullet',
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
