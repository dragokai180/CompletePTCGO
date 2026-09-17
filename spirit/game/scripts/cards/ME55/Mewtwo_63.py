from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2216012e-1102-57c0-bb16-8f733bfa65bf',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name',
    display_name='Mewtwo',
    searchable_by=['Mewtwo', 'Basic', 'Mewtwo'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=150,
    abilities=[
        Attack(
            title='Empower',
            game_text='Attach up to 2 Basic Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psydrive',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
