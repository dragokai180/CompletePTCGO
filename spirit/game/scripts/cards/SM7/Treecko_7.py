from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a2531f66-5a27-599a-bafb-ee9c3639a9de',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    display_name='Treecko',
    searchable_by=['Treecko', 'Basic', 'Treecko'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=252,
    abilities=[
        Attack(
            title='Sleep Poison',
            game_text="Your opponent's Active Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
