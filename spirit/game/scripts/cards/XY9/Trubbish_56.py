from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d7cbb46-359d-5973-b9cd-f8ff8e1dea59',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name',
    display_name='Trubbish',
    searchable_by=['Trubbish', 'Basic', 'Trubbish'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=568,
    abilities=[
        Attack(
            title='Acid Spray',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
