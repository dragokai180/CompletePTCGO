from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='99f308b9-74bf-51e3-a9ef-3913ccae51f7',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name',
    display_name='Vivillon',
    searchable_by=['Vivillon', 'Stage 2', 'Vivillon'],
    subtypes=['Stage 2'],
    collector_number=8,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    family_id=666,
    abilities=[
        Ability(
            title='Guiding Dance',
            game_text='Once during your turn, you may use this Ability. Flip a coin. If heads, search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Poison Powder',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
