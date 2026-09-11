from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34b671e8-73f8-5e56-9625-7e48a48a09a5',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name',
    display_name='Yanmega',
    searchable_by=['Yanmega', 'Stage 1', 'Yanmega'],
    subtypes=['Stage 1'],
    collector_number=3,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    family_id=193,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Air Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
