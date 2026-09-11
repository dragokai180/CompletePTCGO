from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b9fda36-e326-5a80-8774-25b8fc420064',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    display_name='Weepinbell',
    searchable_by=['Weepinbell', 'Stage 1', 'Weepinbell'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Muddy Acid',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
