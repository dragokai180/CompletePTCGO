from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='710be6ab-9eef-5bc8-8d2f-824988c86e5f',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name',
    display_name='Victreebel',
    searchable_by=['Victreebel', 'Stage 2', 'Victreebel'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='SM2',
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
            title='Pollen Hazard',
            game_text="Your opponent's Active Pokémon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Stick and Absorb',
            game_text="Heal 20 damage from this Pokémon. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
