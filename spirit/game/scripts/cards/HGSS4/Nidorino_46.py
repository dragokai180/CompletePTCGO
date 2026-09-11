from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3bf3530-85c3-5e38-8a6b-cc0997e82ed2',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    display_name='Nidorino',
    searchable_by=['Nidorino', 'Stage 1', 'Nidorino'],
    subtypes=['Stage 1'],
    collector_number=46,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=32,
    abilities=[
        Attack(
            title='Horn Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Lunge',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
