from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='299ce6b8-8592-5e41-82d1-8c809d17beb6',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name',
    display_name='Cherubi',
    searchable_by=['Cherubi', 'Basic', 'Cherubi'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=420,
    abilities=[
        Attack(
            title='Hide',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
