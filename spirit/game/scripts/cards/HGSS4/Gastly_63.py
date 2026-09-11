from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='acc99fcf-3ee0-5ac0-9a25-16eed0690492',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    display_name='Gastly',
    searchable_by=['Gastly', 'Basic', 'Gastly'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Attack(
            title='Sneaky Placement',
            game_text="Put 1 damage counter on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
