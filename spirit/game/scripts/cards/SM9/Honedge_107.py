from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3fa284ec-bc38-5270-be95-5c1dd6396f08',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    display_name='Honedge',
    searchable_by=['Honedge', 'Basic', 'Honedge'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title='Cut Down',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
    ],
)
