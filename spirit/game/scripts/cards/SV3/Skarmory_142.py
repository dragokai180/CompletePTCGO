from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24979a11-37d0-5800-95e5-a8243c91a711',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name',
    display_name='Skarmory',
    searchable_by=['Skarmory', 'Basic', 'Skarmory'],
    subtypes=['Basic'],
    collector_number=142,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=227,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Slashing Steel',
            game_text="During your next turn, this Pokémon can't use Slashing Steel.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
