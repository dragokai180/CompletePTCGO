from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e66586c-bda2-5d16-a5a5-d79753af66b0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name',
    display_name='Victreebel',
    searchable_by=['Victreebel', 'Stage 2', 'Victreebel'],
    subtypes=['Stage 2'],
    collector_number=15,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Reactive Poison',
            game_text="This attack does 60 more damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Gastro Acid',
            game_text='The Defending Pokémon has no Abilities until the end of your next turn.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
