from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8be763ff-1896-5896-877b-ab9e28865f0c',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name',
    display_name='Seismitoad',
    searchable_by=['Seismitoad', 'Stage 2', 'Seismitoad'],
    subtypes=['Stage 2'],
    collector_number=84,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name',
    family_id=537,
    abilities=[
        Attack(
            title='Quaking Fist',
            game_text="During your opponent's next turn, whenever they try to use a Trainer card from their hand, they flip a coin. If tails, your opponent discards that Trainer card instead of using it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Mega Punch',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
