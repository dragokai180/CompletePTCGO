from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16316e6f-1ee2-57f1-b82b-b99869e538f0',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name',
    display_name='Chimecho',
    searchable_by=['Chimecho', 'Basic', 'Chimecho'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=358,
    abilities=[
        Attack(
            title='Bell of Silence',
            game_text="Your opponent can't play any Pokémon that has an Ability from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
