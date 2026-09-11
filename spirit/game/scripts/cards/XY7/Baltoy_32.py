from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df3c3948-bbbe-5a99-851a-48364afb9c49',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name',
    display_name='Baltoy',
    searchable_by=['Baltoy', 'Basic', 'Baltoy'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=343,
    abilities=[
        Attack(
            title='Future Spin',
            game_text="Look at the top 3 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
