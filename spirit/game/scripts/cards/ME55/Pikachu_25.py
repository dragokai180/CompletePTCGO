from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='39449e23-51bd-5454-a706-58b3c26a371d',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Spark',
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
