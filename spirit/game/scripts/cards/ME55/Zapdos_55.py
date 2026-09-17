from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a051fe28-fd7d-5f20-887b-5c62e516a224',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name',
    display_name='Zapdos',
    searchable_by=['Zapdos', 'Basic', 'Zapdos'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=145,
    abilities=[
        Ability(
            title='Flash-Pop Flapping',
            game_text='Once during your turn, if you have Moltres and Articuno in play, you may use this Ability. Attach a Basic Lightning Energy card from your hand to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Thundering Lightning',
            game_text='This Pokémon also does 60 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
