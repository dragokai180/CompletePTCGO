from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01a956fb-6689-5504-8862-fa74b9d37a4c',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name',
    display_name='Lunala',
    searchable_by=['Lunala', 'Stage 2', 'Lunala'],
    subtypes=['Stage 2'],
    collector_number=80,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=789,
    abilities=[
        Attack(
            title='Midnight Ray',
            game_text='This attack does 20 more damage for each Energy card in your discard pile.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Lunar Blast',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
