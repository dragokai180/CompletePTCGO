from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d52a079-73a3-5e2d-af25-278c7dfb94aa',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    display_name='Misdreavus',
    searchable_by=['Misdreavus', 'Basic', 'Misdreavus'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=200,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
