from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3100c5ac-7e89-5f7f-bc85-0a945da7ba6c',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    display_name='Pancham',
    searchable_by=['Pancham', 'Basic', 'Pancham'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=674,
    abilities=[
        Attack(
            title='Arm Thrust',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
