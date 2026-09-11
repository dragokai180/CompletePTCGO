from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='727df9b8-616e-552a-8be3-82d2156ec6dd',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    display_name='Nuzleaf',
    searchable_by=['Nuzleaf', 'Stage 1', 'Nuzleaf'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    family_id=273,
    abilities=[
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title='Razor Wind',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
