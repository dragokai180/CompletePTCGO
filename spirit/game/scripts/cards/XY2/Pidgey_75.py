from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93b354df-4191-559e-85ba-10ac9c34d686',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name',
    display_name='Pidgey',
    searchable_by=['Pidgey', 'Basic', 'Pidgey'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(
            title='Peck Off',
            game_text="Before doing damage, discard all Pokémon Tool cards attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
