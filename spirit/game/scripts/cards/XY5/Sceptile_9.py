from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ed35fc5-7131-5f97-ac68-91569ecd533b',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name',
    display_name='Sceptile',
    searchable_by=['Sceptile', 'Stage 2', 'Sceptile'],
    subtypes=['Stage 2'],
    collector_number=9,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    family_id=252,
    abilities=[
        Attack(
            title='Leaf Blade',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Power Poison',
            game_text="Discard 1 Energy attached to this Pokémon. Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.'),
)
