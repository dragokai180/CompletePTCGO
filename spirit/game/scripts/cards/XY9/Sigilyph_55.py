from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f36dd67-7c1d-5aa2-96e1-16db5548fd03',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name',
    display_name='Sigilyph',
    searchable_by=['Sigilyph', 'Basic', 'Sigilyph'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Attack(
            title='Reflective Shield',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put 5 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psy Report',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
