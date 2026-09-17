from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16329077-e131-5a4c-8477-5a46ce6f31ff',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name',
    display_name='Cresselia',
    searchable_by=['Cresselia', 'Basic', 'Cresselia'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=488,
    abilities=[
        Attack(
            title='Aurora Gain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Lunar Blast',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
