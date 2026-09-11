from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56936fe7-4e2e-5db4-8a63-517bc3d02351',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    display_name='Shuppet',
    searchable_by=['Shuppet', 'Basic', 'Shuppet'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=353,
    abilities=[
        Attack(
            title='Disable',
            game_text="Flip a coin. If heads, choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Haunt',
            game_text='Put 1 damage counter on the Defending Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
