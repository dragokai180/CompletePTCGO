from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c8c1f46-216b-5ef9-ab9c-179d80cc30a4',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name',
    display_name='Rayquaza-EX',
    searchable_by=['Rayquaza-EX', 'Basic', 'EX', 'RayquazaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=60,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Dragon Strike',
            game_text="Flip a coin. If tails, this Pokémon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
