from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ba4f345-6bc1-5645-8558-7b6996823d4b',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name',
    display_name='Moltres',
    searchable_by=['Moltres', 'Basic', 'Moltres'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=146,
    abilities=[
        Ability(
            title='Fiery Flapping',
            game_text='Once during your turn, if you have Articuno and Zapdos in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Fire Spin',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
