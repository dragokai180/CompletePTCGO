from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='894968eb-75bc-5d46-a31a-252cf86c4fcd',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    display_name='Weepinbell',
    searchable_by=['Weepinbell', 'Stage 1', 'Weepinbell'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='SM10',
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
            title='Burning Venom',
            game_text="Your opponent's Active Pokémon is now Burned and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
