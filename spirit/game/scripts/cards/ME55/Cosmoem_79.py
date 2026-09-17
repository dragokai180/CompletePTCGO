from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7d148b4-6428-58e1-82a2-447be1db349a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    display_name='Cosmoem',
    searchable_by=['Cosmoem', 'Stage 1', 'Cosmoem'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    family_id=789,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
