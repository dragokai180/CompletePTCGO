from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6101caa9-84a5-578a-8e24-c6090ec91089',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name',
    display_name='Espeon',
    searchable_by=['Espeon', 'Stage 1', 'Espeon'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Solar Suggestion',
            game_text="Move up to 4 damage counters from any of your Pokémon to any of your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psybeam',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
