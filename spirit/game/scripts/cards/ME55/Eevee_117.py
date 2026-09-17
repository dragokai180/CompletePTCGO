from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ee3e386-08d5-576e-bd41-2689ce6b76fb',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    display_name='Eevee',
    searchable_by=['Eevee', 'Basic', 'Eevee'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
