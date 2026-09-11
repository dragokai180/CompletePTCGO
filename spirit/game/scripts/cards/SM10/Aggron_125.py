from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='182c6bcb-d68d-5ac7-8f88-7eb6c5a58392',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name',
    display_name='Aggron',
    searchable_by=['Aggron', 'Stage 2', 'Aggron'],
    subtypes=['Stage 2'],
    collector_number=125,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Extra-Tight Press',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Giga Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
