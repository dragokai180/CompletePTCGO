from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='507d6af5-a0a8-583f-81ee-d3c24b493b42',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name',
    display_name='Hydreigon',
    searchable_by=['Hydreigon', 'Stage 2', 'Hydreigon'],
    subtypes=['Stage 2'],
    collector_number=99,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    family_id=633,
    abilities=[
        Attack(
            title='Three-Headed Bite',
            game_text="Flip 3 coins. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pitch-Black Fangs',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
