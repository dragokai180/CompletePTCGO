from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71a1b163-837d-5bed-993b-9f82813666ab',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Hang Down',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Zap Kick',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
