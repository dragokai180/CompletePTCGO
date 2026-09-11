from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22367390-1ced-5f74-817d-fd8b68a137c7',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name',
    display_name='Magcargo',
    searchable_by=['Magcargo', 'Stage 1', 'Magcargo'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Indomitable Blaze',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.'),
)
