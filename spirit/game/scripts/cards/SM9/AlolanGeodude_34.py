from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64fd77a7-b873-51bb-b307-99412f31c437',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name',
    display_name='Alolan Geodude',
    searchable_by=['Alolan Geodude', 'Basic', 'AlolanGeodude'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title='Self-Destruct',
            game_text='This Pokémon does 60 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
