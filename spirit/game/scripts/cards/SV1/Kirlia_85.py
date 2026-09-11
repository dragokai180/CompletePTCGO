from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='773506c5-ea17-50f9-af42-fe81321c66a7',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    display_name='Kirlia',
    searchable_by=['Kirlia', 'Stage 1', 'Kirlia'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    family_id=280,
    abilities=[
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
