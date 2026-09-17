from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37232ced-9db2-5da2-8c82-54ae5237e671',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name',
    display_name='Zekrom',
    searchable_by=['Zekrom', 'Basic', 'Zekrom'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=644,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Nitro Thunder',
            game_text='If this Pokémon has any Fire Energy attached, this attack does 80 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
