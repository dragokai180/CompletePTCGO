from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3d0d3fe-2045-557c-ab25-24a3c79fc25a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Overwriting Bolt',
            game_text="The Defending Pokémon's Weakness is now Lightning until the end of your next turn. (Apply Weakness as x2.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
