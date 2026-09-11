from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9c8d9bc-05f7-5adf-9eeb-35eaf67b657c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name',
    display_name='Servine',
    searchable_by=['Servine', 'Stage 1', 'Servine'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name',
    family_id=495,
    abilities=[
        Ability(
            title='Serpentine Strangle',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
